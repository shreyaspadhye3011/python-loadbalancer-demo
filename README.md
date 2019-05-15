# About
Welcome to the world of Load Balancer!

This is a simple web server which demos the use of Flask along with a load balancer. The environment is virtually created using Docker.

The app runs at http://localhost/ Also the mongo-express is available at http://localhost:8081

Author: Shreyas Padhye

# Pre-Requisite:
Machine should have Docker installed in it.

# Deploy & Run
One-time setup:
1. Set mongo db credentials that you would want in two separate environment variables using following commands:
    a. export mongo_user= <username>
    b. export mongo_pass= <password>
2. Mount containers: Open root project directory & run `docker-compose up --build`
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
- To test load balancer working, you can keep reloading the home page at http://localhost/ and you'll see the page being served from a different flask server everytime.
(yet to be added)

# Steps of Development
(yet to be added)


# Other useful commands
- docker-compose ps
- mongodump --db myusers -u <username> -p <password> --authenticationDatabase admin

#TODOs / Future Improvements: 
- Change Dockerfile code to use ENV variable to set .ini file & implement through single docker file
- Explore if it can be done through single app.ini file
- Can add checks for DDoS and block IPs


