pip3 install -r requirements.txt
docker run -p 27017:27017 --name mongo -d mongo:latest
python app.py