pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
               bat 'pipenv --python python3 sync'
            }
        }
        stage('Test') {
            steps {
               bat 'pipenv run pytest'
            }
        }
        stage('Package') {
	    when{
		    anyOf{ branch "master" ; branch 'release' }
	    }
            steps {
               bat 'zip -r sbdl.zip lib'
            }
        }
	
    }
}
