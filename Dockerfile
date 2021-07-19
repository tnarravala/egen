FROM python:3

COPY . /Users/thejeswarreddynarravala/PycharmProjects/egen-capstone1/DockerFile

WORKDIR /Users/thejeswarreddynarravala/PycharmProjects/egen-capstone1/DockerFile

RUN pip install -r requirements.txt


CMD ["python3","publishtopub.py"]
