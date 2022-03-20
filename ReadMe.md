# build image
docker build -t flask-api .

# start container from image
docker run -d -p 5000:5000 --name flask-api flask-api

# start container from image, when connecting exterl db outside this container
docker run -d -p 5000:5000 -e DB_URI='host.docker.internal' --name flask-api flask-api

# start postgres
docker run -d -e POSTGRES_USER='user' \
-e POSTGRES_PASSWORD='pass' \
-e POSTGRES_DB='dbname' \
-p 5432:5432 --name postgres postgres:latest


# modify python file on hot container
docker cp ./app.py flask-api:/usr/src/app
docker restart flask-api