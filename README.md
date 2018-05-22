# chat application python


*Build docker locally
docker build -t local/python -f ./Dockerfile .

to run:
docker run -it -p 8080:8080 local/python:latest

if you want to map a folder to the docker run:
docker run -it -v /Users/behalfusers/PycharmProjects/reporting-appengine/app/shared_resource:/opt/behalf/cto/reporting/data/ -p 8080:8080 local/python:latest
 

to connect
docker exec -it [container] bash

* Installation
pip install virtualenv
virtualenv -p python3 env

Before running or deploying this application, install the dependencies using pip:
pip install -t lib -r requirements.txt

* Deploy
gcloud app deploy

* Running the application (need to be in app folder)
python main.py

by gunicorn:
cd app
gunicorn --access-logfile - -b :8080 wsgi


to test:

curl "http://127.0.0.1:8080/keep-alive"

pip basic commands:
pip list --outdated


virtualenv wrapper

workon



CURL examples:
send message
curl -H "Content-Type:application/raw" -X POST "http://127.0.0.1:8080/chat" -d 'hello world'

get message
return messages should be in the format json:
{"messages": "hello world3", "id": "1"}

curl -H "Content-Type:application/raw" -X GET "http://127.0.0.1:8080/chat/1"
curl -H "Content-Type:application/raw" -X DELETE "http://127.0.0.1:8080/chat/12"

application should have class MessageApp to manage internally all messages with ids

The following endpoints should be supported:
* POST /chat/send (will return id of message)
* GET /chat/<message_id>/peek (will return json of message)
* GET /chat/<message_id>/pop (will return json of message) 

you should have tests for MessageApp and for flask endpoints



