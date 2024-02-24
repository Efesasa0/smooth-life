FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . .

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "7860"]
