pipeline {
    agent any
    stages {
        stage('Test') { 
            steps {
                sh 'sudo pytest code/test.py'
            }
        }
        // stage('Destory running instances') {
        //     steps {
        //         sh '''
        //               docker-compose down
        //               docker system prune -a -f
                      
                     
        //            '''
        //     }
        //     }
        // stage('Build') {
        //     steps {
        //         sh 'sudo docker-compose up -d'
        //     }
        // }
        stage('Deploying') {
            steps {
                sh '''
                    #!/bin/bash
                    sudo ssh -i /home/jenkins/.ssh/Estio-Ubuntu.pem -o StrictHostKeyChecking=no ubuntu@18.130.214.109 << EOF
                    rm -rf estio_app
                    git clone https://github.com/Doctor-Scott/estio_app.git
                    cd estio_app
                    sudo docker-compose down
                    sudo docker system prune -a -f                  
                    sudo docker-compose up --build -d
                    exit 0
                    << EOF
                '''
            }
        }
    }
}
