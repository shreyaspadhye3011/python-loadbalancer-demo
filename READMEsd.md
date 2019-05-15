# About
Welcome to the world of Load Balancer!

This is a simple web server which demos the use of Flask along with a load balancer. The environment is virtually created using Docker.

The app runs at http://localhost/ Also the mongo-express is available at http://localhost:8081

If you pass `user_id` as a query paramter in the GET request to `/`, the server responds with the associated `user_key` which it fetches from a mongodb database along with the port number of the service responding, otherwise it simply shows which Flask app is serving your request.

Author: Shreyas Padhye

# Pre-Requisite:
Machine should have Docker installed in it.

# Deploy & Run
One-time setup:
1. Set mongo db credentials that you would want in two separate environment variables using following commands (where `<username>` and `<password>` are values that you want to set):  
    a. `export mongo_user= <username>`  
    b. `export mongo_pass= <password>`
2. Mount containers: Open root project directory  
        run `docker-compose up --build`
3. SSH in docker container: Open a separate terminal in root project directory  
        run `docker exec -it mongo /bin/bash` 
4. Here, create database using dunp:
        In the docker container terminal access created in step 3,  
        run `mongorestore --db myusers dump/myusers -u <username> -p <password> --authenticationDatabase admin`
5. run `exit` to exit shell

For every time you want to run / restart containers:
1. Open terminal in project's root directory and run following commands 
2. `docker-compose build`
3. `docker-compose up` 
or alternatively: `docker-compose up --build`

To stop running services: Press `Ctrl + Z` and RUN `docker-compose stop`

# Test
On Browser:
- To test load balancer working, you can keep reloading the home page at http://localhost/ and you'll see the page being served from a different flask server everytime.
- To test `user_key` retrieval, pass in the `user_id` as a query parameter to '/' route eg `http://localhost/?user_id=1` will return `one@5cdb5896d7c8` as the key. The response will also contain the port of the flask server that is responding.
- If the request does not contain the `user_id` param, it will fallback to a standard response showing only info about which Flask app is serving and on which port
- user_id from 1 to 7 are available in database and more can be added through mongo-express

Additionally, you can use a REST API client like Postman to GET request http://localhost/ with the user_id query param

# Steps of Development
1. Carefully went over the requirement and understood different aspects of the assignment. 
2. Created virtual environment for flask app along with its folder structure and created requirements.txt file so that it can be served through uWSGI
3. Created wsgi config & basic flask routing at '/' and tested working through `flask run`
4. Dockerized flask and nginx
5. Added code to spin off 3 flask servers via docker containers
6. Added load balancer code to share load among the three flask servers
7. Added mongo integration and included dump restore functionality in Readme to ease deployment
8. Implemented query params handling to query mongodb and fetch appropraite key

# Other useful commands
- `docker-compose ps`
- `mongodump --db myusers -u <username> -p <password> --authenticationDatabase admin`

# TODOs / Future Improvements: 
- mongo: add database not found check
- flask: handle route_not_found default mapping
- Change Dockerfile code to use ENV variable to set .ini file & implement through single docker file
- Explore if it can be done through single app.ini file
- Can add checks for DDoS and block IPs

