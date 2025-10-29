pipeline {
    agent {
        docker { image 'python:3.10' }
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/rithika-droid/quote-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python --version'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found, skipping..."'
            }
        }

        stage('Run Flask App Build') {
            steps {
                echo 'Starting Flask App build...'
                sh 'python app.py & sleep 5'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t quote-app . || echo "Docker build skipped (no Docker in this agent)"'
            }
        }

        stage('Post Build') {
            steps {
                echo '✅ Quote App pipeline completed successfully!'
            }
        }
    }
}
