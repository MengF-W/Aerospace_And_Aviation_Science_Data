# aerospace_and_aviation_science_data
The [National Aeronautics and Space Administration (NASA)](https://www.nasa.gov/) is a U.S. government agency that is responsible for science and technology related to air and space.
It also provide a digital interface, namely the [NASA Open APIs](https://api.nasa.gov/), to programmatically access NASA's extensive datasets. 
The APIs make NASA data, including imagery, eminently accessible to the public. 
It provides a choice of standard web output formats, either JSON or HTML, of response format

This web appilcation provides a Python-wrapper around the JSON API provided by NASA Open APIs. 
At the moment the wrapper only implements the "Astronomy Picture of the Day" JSON API. 
The response is displayed in a web browser. More different JSON API wrapper will be added in this web application in later stage.

# Libraries used
* Django
* requests

# How to Run
- `pip install --no-cache-dir --no-input -r requirements.txt` -Install dependencies under the root directory
- `python manage.py runserver` -Start the application under the root directory 
- Enter the URL 'http://localhost:8000/' in a web browser. The result is then displayed in the web browser

<img width="1893" height="1027" alt="image" src="https://github.com/user-attachments/assets/a5bc8f5b-19c7-4d65-9122-66ed5d688753" />


# Docker Image Command
`docker build -t aerospace_and_aviation_science_data .`    -To build the docker image

# Docker Container Command
`docker-compose up -d`      -To start the docker container from the docker image with the docker compose file configuration  

# Publish
It has been published and can be accessed at https://the-aerospace-and-aviation-science-data.onrender.com/

<img width="1890" height="1022" alt="image" src="https://github.com/user-attachments/assets/d0149edc-88ce-422e-bb29-b29603f7a6e7" />


The host provider might cause delay of loading

<img width="894" height="73" alt="image" src="https://github.com/user-attachments/assets/a2d1a923-f461-4218-a124-21a04649c85d" />
