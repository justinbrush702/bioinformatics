# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

COPY . .
COPY src/ .
COPY data_files/ .

ADD docker-entrypoint.sh /usr/local/docker-entrypoint.sh

# Start the demo via an entrypoint
RUN ["chmod", "+x", "/usr/local/docker-entrypoint.sh"]
ENTRYPOINT ["/usr/local/docker-entrypoint.sh"]
