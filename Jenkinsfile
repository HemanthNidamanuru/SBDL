pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat """
                    echo ==== Installing Pipenv ====
                    pip install pipenv

                    echo ==== Syncing Virtual Environment ====
                    pipenv --python "C:\\Users\\heymo\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" sync
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                    echo ==== Running Pytest ====
                    pipenv run pytest
                """
            }
        }

        stage('Package') {
            when {
                anyOf {
                    branch 'master'
                    branch 'release'
                }
            }
            steps {
                bat """
                    echo ==== Creating Deployment Package ====
                    powershell -Command "Compress-Archive -Force .\\lib sbdl.zip"
                """
            }
        }

        stage('Release') {
            when {
                branch 'release'
            }
            steps {
                bat """
                    echo ==== Deploying to QA Environment ====
                    mkdir C:\\SBDL-Deploy\\QA
                    xcopy /E /Y sbdl.zip C:\\SBDL-Deploy\\QA\\
                    xcopy /E /Y conf C:\\SBDL-Deploy\\QA\\conf\\
                    xcopy /E /Y log4j.properties C:\\SBDL-Deploy\\QA\\
                    xcopy /E /Y sbdl_main.py C:\\SBDL-Deploy\\QA\\
                    xcopy /E /Y sbdl_submit.sh C:\\SBDL-Deploy\\QA\\
                """
            }
        }

        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                bat """
                    echo ==== Deploying to PROD Environment ====
                    mkdir C:\\SBDL-Deploy\\PROD
                    xcopy /E /Y sbdl.zip C:\\SBDL-Deploy\\PROD\\
                    xcopy /E /Y conf C:\\SBDL-Deploy\\PROD\\conf\\
                    xcopy /E /Y log4j.properties C:\\SBDL-Deploy\\PROD\\
                    xcopy /E /Y sbdl_main.py C:\\SBDL-Deploy\\PROD\\
                    xcopy /E /Y sbdl_submit.sh C:\\SBDL-Deploy\\PROD\\
                """
            }
        }
    }

    post {
        success {
            echo "Pipeline Completed Successfully!"
        }
        failure {
            echo "Pipeline Failed!"
        }
    }
}
