# poetry-flask-example
### Docker Commands

- Update project and build docker image
  - ```poetry update```
  - ```poetry export > requirements.txt```
  - ```docker build --pull --rm -f "Dockerfile" -t poetryflaskexample:latest "."```

- Running docker image
  - ```docker run -p 80:5000 poetryflaskexample:latest```
