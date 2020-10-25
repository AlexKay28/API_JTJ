# API_JTJ (Json-to-Json)
Simple API app with exaples how to create app with API. Input: JSON, output: JSON


### Docker Deployment
It is very easy to install and utilize with a Docker container.

By default, the Docker will expose port 8085, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd API_JTJ
docker build -t my_app_with_api .
```
This will create the docker image and pull in the necessary dependencies. 

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we create container with name "working_app", run in as daemon and simply map port 8085 of the host to port 8085 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8085:8085 --name working_app my_app_with_api
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8086/solve
```
or, which is equal:
```
http://0.0.0.0:8086/solve
```
#### Usage Example
You can check working app by using "usage_example.py" script in dirrectory. Use command:
```
python usage_example.py 
```
### Todos

 - Expand functionality
 - Add tests
 - Made up something else =)
