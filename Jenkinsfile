pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat """
                    pip install pipenv
                    pipenv --python python sync
                """
            }
        }

        stage('Test') {
            steps {
                bat "pipenv run pytest"
            }
        }

        stage('Package') {
            when {
                anyOf { branch 'master'; branch 'release' }
            }
            steps {
                // Windows does not support "zip -r"
                powershell "Compress-Archive -Path lib -DestinationPath sbdl.zip -Force"
            }
        }
    }
}
