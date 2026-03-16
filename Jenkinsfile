pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/PapankaSanjana/ui_automation.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=report.html'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html'
            }
        }

    }
}
