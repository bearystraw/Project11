# Use an official lightweight Python image.
# Alpine Linux is small and well suited for a compact Docker image.
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Command to run on container start
ENTRYPOINT ["python", "./itsv412_cli.py"]