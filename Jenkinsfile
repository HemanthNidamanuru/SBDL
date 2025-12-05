pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat """
                    pip install pipenv
                    pipenv --python "C:\\Users\\heymo\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" sync
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
                powershell "Compress-Archive -Path lib -DestinationPath sbdl.zip -Force"
            }
        }
    }
}
