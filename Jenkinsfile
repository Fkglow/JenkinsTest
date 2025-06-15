pipeline {
    agent any

    triggers {
        cron('* * * * *')
    }

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello world!', description: "Message to be displayed.")
    }

    stages {
        stage('Say Message') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }
    }
}