from flask import Flask, request, jsonify, Response
from db.database import initialize_db
from db.Models import Tasks
import json
import re
from markupsafe import escape
import RandomTask
import os

app = Flask(__name__)
host = os.getenv('MONGO_HOST')
db_name = os.getenv('DB_NAME')

app.config["MONGODB_SETTINGS"]= {
    'host':'mongodb://{}/{}'.format(host, db_name)
}

initialize_db(app)

@app.route('/')
def index():
    return jsonify(status=up)

@app.route('/api/task/bulk', methods=['POST'])
def bulk():
    tasks = []

    for i in range(50):
        tasks.append(Tasks(**RandomTask.createTask()))
    
    Tasks.objects.insert(tasks)

    return Response(status=201)

@app.route('/api/task', methods=['POST'])
def addTask():
    body = request.get_json()
    try:
        task = Tasks(**body).save()
        
        return Response(json.dumps({"message":"Task Created"}),mimetype="application/json",status=201)

    except Exception as e:
        print(e)
        return Response(json.dumps({"message":"Interal Error"}),mimetype="application/json",status=500)

@app.route('/api/task',methods=['GET'])
def task():
    status = request.args.get('status').lower()
    status = False if status == 'false' else True
    try:
        task = Tasks.objects(status=status).to_json()
        meessage = "Tasks Completed" if status == True else 'Tasks Pending'
        return Response(json.dumps({"message":meessage,"data":json.loads(task)}), mimetype="application/json", status=200)
    except Exception as e:
        return Response(json.dumps({"message":"Interal Error"}),mimetype="application/json",status=500)

@app.route('/api/task/search',methods=['GET'])
def search():
    q = request.args.get('q')
    print(q)

    qr = re.compile('.*{}.*'.format(q), re.I)

    try:
        task = Tasks.objects(description=qr).to_json()
        return Response(json.dumps({"message":"Search Result","data":json.loads(task)}), mimetype="application/json", status=200)
    except Exception as e:
        return Response(json.dumps({"message":"Interal Error"}),mimetype="application/json",status=500)


@app.route('/api/task/<id_>',methods=['PUT','DELETE'])
def removeAndDelete(id_):
    id_ = escape(id_)

    try:
        task = json.loads(Tasks.objects(id = id_).to_json())
        # print(task)
        if len(task) == 0:
            return Response(mimetype="application/json",status=404)

        if request.method == 'PUT': 
            newtask = request.get_json()
            print(task)
            try:
                if task[0]['status']:
                    return jsonify(message='Task completed, not modified'), 400

                Tasks.objects(id = id_).update(**newtask)

                return Response(json.dumps({"message":"Task Updated"}), mimetype="application/json", status=200)

            except Exception as e:
                return Response(json.dumps({"message":"Interal Error"}),mimetype="application/json",status=500)

        
        if request.method == 'DELETE':
            Tasks.objects(id = id_).delete()

            try:
                return Response(json.dumps({"message":"Task Deleted"}), mimetype="application/json", status=200) 
            except Exception as e:
                return Response(json.dumps({"message":"Interal Error"}),mimetype="application/json",status=500)

    except Exception as err:
            print(err)
            return jsonify(message="Interal Error"), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False)