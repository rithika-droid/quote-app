# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir flask selenium webdriver-manager

# Expose the Flask port
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
