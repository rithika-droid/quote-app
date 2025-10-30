pipeline {
    agent any

    tools {
        maven 'maven'
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/rithika-droid/quote-app.git'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'
            }
        }

        stage('Docker Image') {
            steps {
                bat 'docker build -t ashokit/mavenwebapp .'
            }
        }

        stage('Docker Container') {
            steps {
                bat '''
                docker stop javaapp || echo "Container not running"
                docker rm javaapp || echo "No container to remove"
                docker run -d -p 8081:8080 --name javaapp ashokit/mavenwebapp
                '''
            }
        }
    }
}
