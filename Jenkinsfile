pipeline {
    agent any
    stages {
        stage('Test') { 
            steps {
                sh 'sudo pytest test.py'
            }
        }
        stage('Clean Up') {
            steps {
                sh '''
                      sudo docker system prune -a -f
                      sudo docker stop $(docker ps -aq)
                      sudo docker rm $(docker ps -aq)
                      sudo docker rmi $(docker images -q)
                   '''
            }
            }
        stage('Build') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }
        // stage('Deploying') {
        //     steps {
        //         sh '''
        //             ssh -i /home/jenkins/.ssh/Estio-Training-NForester -o StrictHostKeyChecking=no jenkins@10.0.1.10
        //             sudo docker-compose -f /home/ubuntu/APIPrimeAge/docker-compose.yaml down
        //             sudo docker system prune -a -f                  
        //             sudo docker-compose -f /home/ubuntu/APIPrimeAge/docker-compose.yaml build
        //         '''
        //     }
        // }
    }
}
