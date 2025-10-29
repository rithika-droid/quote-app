pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/rithika-droid/quote-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                python --version
                pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t quoteapp .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat '''
                docker stop quoteapp || echo "Container not running"
                docker rm quoteapp || echo "No container to remove"
                docker run -d -p 5000:5000 --name quoteapp quoteapp
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Quote App deployed successfully!'
        }
        failure {
            echo '❌ Build failed. Check logs for details.'
        }
    }
}
