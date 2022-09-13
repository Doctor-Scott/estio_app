pipeline {
    agent any
    stages {
        stage('Test') { 
            steps {
                sh 'sudo pytest test.py'
            }
        }
        stage('Destory running instances') {
            steps {
                sh '''
                      docker-compose down
                      docker system prune -a -f
                      
                     
                   '''
            }
            }
        stage('Build') {
            steps {
                sh 'docker-compose deploy -d'
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
