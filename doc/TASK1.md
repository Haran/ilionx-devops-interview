### Vagrant and application sanity check

- `vagrant up` and `vagrant ssh`
- `cd /projects && ./gradlew clean build`
- `java -jar helloworld/build/libs/helloworld.jar`

Log shows that the Spring Boot app launches Tomcat on 8080, so we want to expose this port. Out of curiosity let's see what it does (from the second terminal):

```
$ telnet localhost 8080
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

> GET / HTTP/1.1
> Host: localhost

< HTTP/1.1 200 
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 12
< Date: Thu, 22 Feb 2024 16:31:41 GMT

< Hello World!
```

Okay, the greeting and status code seems correct, we can proceed

### Packing to docker

```bash
docker build -t ilionx-helloworld .
docker run -d --name ilionx-helloworld ilionx-helloworld
docker rm -f ilionx-helloworld
docker rmi ilionx-helloworld
docker system prune # for housekeeping purposes 
```

### Multistage packing

`docker image ls | grep ilionx` shows us that image is 456MB, it might be reasonable to lower the image size by multistage build. This completes the **Optional** part of **Task 1**, where we build the project inside docker container and pack it to an image. 

```
$ docker rm -f ilionx-helloworld
$ docker rmi ilionx-helloworld
$ docker build -t ilionx-helloworld -f Dockerfile.multistage .
$ docker run -d -p6543:8080 --name ilionx-helloworld ilionx-helloworld

$ telnet localhost 6543
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.

> GET / HTTP/1.1
> Host: localhost

< HTTP/1.1 200 
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 12
< Date: Thu, 22 Feb 2024 17:09:01 GMT

Hello World!

$ docker image ls | grep ilionx | awk '{print $7}'
313MB/t 
```

----

> Time logged here ~20-30 minutes

----

### Building in pipeliens

#### Gitlab CI/CD

- I'm more familiar with Gitlab so will start with it by creating `.gitlab-ci.yml` to use Gitlab DinD
- It's triggered as `manual` in order not to waste resources and rebuild image on every push
- Luckily I haven't spent all my free minutes, don't want to mess with self-hosted runner :)
- Wait for pipeline to succeed, verify Container Registry has new image
- Create personal token and pull-run image locally:
    ```
    $ TOKEN=xxxxxx
    $ docker login registry.gitlab.com -u olegs.capligins --password-stdin <<<$TOKEN
    $ docker run --name ilinox-helloworld -p6543:8080 registry.gitlab.com/olegs.capligins/ilionx-devops-interview/ilionx-helloworld
  
    // same telnet check
    ```
- Fun fact - locally image size shows 313MB, while on Gitlab it is 114.12 MiB, as it is either compressed, or only the last layer. Lies, deception.

#### Github Actions

- Creating workflow
- Also triggered manually
- Here's why I honestly prefer self-hosted Gitlab
  - Github doesn't allow to run actions on newly created branch. In order to mitigate it, was forced to create dummy workflow on `main`, rebase my feature branch and push anew. Unnecessary hassle (sorry for blank PR, thought it might solve the issue, but apparently not)
  - `ERROR: invalid tag "ghcr.io/Haran/helloworld:latest": repository name must be lowercase`. This is clearly the sign of Microsoft acquisition of Github - case sensitive names like in Windows.
- Image is built and can be pulled without login, as the for is public and image is public as well
    ```
    $ docker pull ghcr.io/haran/ilionx-devops-interview:latest
    $ docker run --name ilinox-helloworld -p6543:8080 ghcr.io/haran/ilionx-devops-interview:latest
  
    // same telnet check
    ```

----

> Time logged here ~30 minutes<br>
> Gitlab worked out-of-the-box, but Github took some time due to it's quirks that I rarely encounter

----
