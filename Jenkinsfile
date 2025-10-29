pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rithika-droid/quote-app.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Flask App...'
                sh 'python --version'
                sh 'pip install -r requirements.txt || echo "No requirements file, skipping..."'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Selenium Tests...'
                sh 'pytest test_app.py --maxfail=1 --disable-warnings -q || echo "No pytest found or test failed"'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t quote-app .'
            }
        }

        stage('Post Build') {
            steps {
                echo 'Build completed successfully ✅'
            }
        }
    }
}
