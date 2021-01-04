# Simple Web Page Hit Counter

Serving a simple web with hit counter printed to screen and 'Reset Count' button.

## Components 

1. Server – Flask 
   
2. Client - Jinja2

3. DB - Sqlite3


## Installation

### Docker 

Run the following to build the image using Docker-compose

      docker-compose up -d --build

Go to http://127.0.0.1:5000/ to see the hit count.


### Docker Volume 
A log file will be written to the host server under the current working directory in the `log` folder.

* Replace in the volume section the desierd folder

        version: '3'
        services:
        web:
            container_name: hit_page
            image: hit_page
            build:
            context: .
            ports:
            - "5000:5000"
            volumes:
            - ./log:/app/log

    ./log  => The host server path
    
    :/app/log => The docker path to the log
