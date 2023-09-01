
# Use the official Python image as the base image
FROM python:3.11

WORKDIR /src

# Install ODBC driver and dependencies

# Install ODBC driver
# apt-get install -y msodbcsql17
# apt-get install -y 
# RUN apt-get update &&  apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 msodbcsql17
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev odbcinst odbcinst1debian2 unixodbc-dev



COPY requirements.txt .
COPY src/ .

# Install dependencies
RUN pip install -r requirements.txt



# Expose port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
