#foreman start -m gateway=1,users=3,timeline=3
gateway:env FLASK_APP=gateway flask run -p $PORT
users: env FLASK_APP=user_api.py flask run -p $PORT
timeline: env FLASK_APP=timeline_api.py flask run -p $PORT
