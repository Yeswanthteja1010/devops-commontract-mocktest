# Use Python base image
FROM python:3.5-slim

# Set working directory
WORKDIR /app

# Copy code
COPY . /app

# Install Flask
RUN pip install -r ./requirements.txt

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

