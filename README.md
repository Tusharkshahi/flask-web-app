# flask-web-app
This is a simple flask web app for assessment purpose.


[![Stay Motivated](https://img.shields.io/badge/Stay-Motivated-teal.svg?style=for-the-badge)](https://vikramgithubio.sameerkapil7111999.now.sh/#vikram) 
[![Think Big](https://img.shields.io/badge/Think-Big-orange.svg?style=for-the-badge)](https://vikramgithubio.sameerkapil7111999.now.sh/#vikram)
[![Work Hard](https://img.shields.io/badge/Work-Hard-blue.svg?style=for-the-badge)](https://vikramgithubio.sameerkapil7111999.now.sh/#vikram)

# Triluxo Technologies Task Readme

## Task Description

The task assigned by Triluxo Technologies Private Limited involved the creation of a simple Flask or FastAPI application. The application should have a single endpoint that returns the message "Hello, Azure Web Apps!" when accessed.

## Project Components

### Flask or FastAPI Application

- File:
  - `app.py` 
- Endpoint:
  - `/`
- Response:
  - "Hello, Azure Web Apps!"
 
  Here the simple flask web app is running as per the given assessment :
  


  
![Screenshot (57)](https://github.com/Tusharkshahi/flask-web-app/assets/103762351/a87a7c43-1f9e-4f9b-9565-769849ca5405)





Dockerization (Optional)

In addition to the specified task, I took the initiative to Dockerize the application. This was done to showcase the ability to containerize the application for consistent deployment across various environments.

### Dockerfile

- File:
  - `Dockerfile`
- Purpose:
  - Containerizes the Flask/FastAPI application for consistent deployment across environments.
- Key Features:
  - Pulls an official Python runtime image.
  - Sets up the working directory.
  - Copies application files.
  - Installs dependencies from `requirements.txt`.
  - Defines environment variables.
  - Exposes port 80.
  - Specifies the command to run the application.

## Deployment Instructions

1. Building the Docker Image:
   - Run `docker build -t your-image-name .` in the project directory.
   - Replace `your-image-name` with the desired image name.

2. Running the Docker Container Locally:
   - Execute `docker run -p 80:80 your-image-name` to run the container locally.
   - Access the application at `http://localhost:80/`.

3. Azure Deployment:
   - Push the Docker image to Azure Container Registry.
   - Configure Azure Web App Service to deploy the image.

## Security Considerations

- Secrets:
  - No secrets are hardcoded in the code, adhering to security best practices.

## Additional Notes

- Regularly update dependencies in `requirements.txt`.
- Check environment variables and configurations before deployment.
- Refer to this readme for deployment and project information.

Feel free to reach out for any clarifications or further assistance.



<a href="https://www.linkedin.com/in/tusharkshahi/" target="_blank"><img height="32" width="32" src="https://cdnjs.cloudflare.com/ajax/libs/ionicons/4.5.6/collection/build/ionicons/svg/logo-linkedin.svg" /></a>
