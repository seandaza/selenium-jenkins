node {   

    
 stage('Push image') {
        withDockerRegistry("https://hub.docker.com/","keodevops" ) {
            def dockerImage = docker.build("jhand/myImage")
            dockerImage.push()
        }
    }    
}
   
