FROM python:3.6



# Use an official Python runtime as a parent image
FROM python:3.6
WORKDIR /app
ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Default Flask port
EXPOSE 80


# Run app.py when the container launches
ENV PYTHONPATH=.
CMD ["python", "get_git"]


# Pass env variables with -e when doing docker run
