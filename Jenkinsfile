pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat """
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                    pytest
                """
            }
        }

        stage('Package') {
            when {
                anyOf { branch 'master'; branch 'release' }
            }
            steps {
                powershell "Compress-Archive -Path lib -DestinationPath sbdl.zip -Force"
            }
        }
    }
}
