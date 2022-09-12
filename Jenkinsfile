pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        // stage('Pre') { hello from Jenkins!
        //     steps {
        //         sh 'ansible-playbook -v -i /home/jenkins/.jenkins/workspace/FlaskApp/inventory.yaml /home/jenkins/.jenkins/workspace/FlaskApp/playbook.yaml'
        //     }
        // }
        stage('Test') { 
            steps {
                sh 'sudo pytest /home/ubuntu/estio_app/test.py'
            }
        }
        stage('Clean Up') {
            steps {
                sh '''

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi $(docker images -q)

rm -rf estio_app
git clone https://github.com/Doctor-Scott/estio_app.git
cd estio_app

                   '''
            }
            }
        stage('Build') {
            steps {
                sh 'sudo docker-compose build'
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

// pipeline {
//     agent any
//     parameters {
//         booleanParam(name: 'Refresh',
//                     defaultValue: false,
//                     description: 'Read Jenkinsfile and exit.')
//                     }
//     stages {
//         stage('</>') {
//             steps {
//                 sh '</>'
//             }
//         }
//         </>
//     }
//  }