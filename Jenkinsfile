pipeline {
    agent {
        docker {
            image 'python:3.7'
            RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
            RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'ls -la'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python main.py'
            }
        }
    }
}
   