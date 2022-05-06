FROM python:3.8-alpine

COPY test.py /home/arkady/dev/python/test/test.py
COPY text.txt /home/arkady/dev/python/test/text.txt

WORKDIR home/arkady/dev/python/test

CMD ["python3", "./test.py"]
