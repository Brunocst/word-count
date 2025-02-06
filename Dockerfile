FROM python:3.11-slim

# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt /
RUN pip3 install --no-cache-dir --upgrade  -r requirements.txt

# Copy all files from folder app to root folder
COPY . /

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["python", "./main.py"] 