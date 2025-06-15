pipeline {
    agent any

    triggers {
        cron('2 * * * *')
    }

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello world!', description: "Wow! Message is displayed! :) ")
    }

    stages {
        stage('Say Message') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }
    }
}