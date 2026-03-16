pipeline {
    agent any

    environment {
        PYTHON = "python3"
        VENV = "venv"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                url: 'https://github.com/PapankaSanjana/ui_automation.git'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Automation Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v --html=report.html
                '''
            }
        }

        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: '*.html', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Automation tests completed successfully!'
        }
        failure {
            echo 'Some tests failed!'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}
