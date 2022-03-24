pipeline {
  agent {
    node {
      label 'master'
    }
  }
  stages {
    stage('Initialize') {
      steps {
          script{
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin${env.PATH}"

          }
      }
    }
    
    stage('build') {
      agent { docker { image 'python:3.7.2' }}
        steps {
          sh 'pip install numpy && python app.py'
        }
      }
    
    stage('test') {
      steps {
        sh 'python test.py'
      }   
    }
    stage('Docker Image') {
      steps{
        sh 'docker build -t personal-python-test .'
      }
    }
    stage('RUN Image / Container Creation'){
      steps{
        sh 'docker run -p 50000:5000 -d --name primeirocontainer personal-python-test'
      }
    }   
    
  }
}
