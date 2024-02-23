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
