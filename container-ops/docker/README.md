# Docker

Docker is a platform designed to help developers build, share, and run modern applications.

## Table of Contents

- [Additional Resources](#additional-resources)
- [What is a Dockerfile?](#what-is-a-dockerfile)
    * [Dockerfile example](#dockerfile-example)
    * [Build an image from a Dockerfile](#build-an-image-from-a-dockerfile)
    * [Run a container from an image](#run-a-container-from-an-image)

## Additional Resources

1. [basic commands](./basic_commands.md)
2. [difference between attach and exec](./diff_between_attach_and_exec.md)

## What is a Dockerfile?

A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. Using docker build users can create an automated build that executes several command-line instructions in succession.

### Dockerfile example

```dockerfile
FROM ubuntu:18.04

COPY . /app

RUN apt-get update && apt-get install -y \
    package-bar \
    package-baz \
    package-foo

WORKDIR /app

ENV LANG ko_KR.UTF-8

EXPOSE 8080

CMD ["./run.sh"]
```

- `FROM` sets the Base Image for subsequent instructions.
- `COPY` copies new files or directories from `<src>` and adds them to the filesystem of the container at the path `<dest>`.
- `RUN` executes any commands in a new layer on top of the current image and commits the results.
- `WORKDIR` sets the working directory for any `RUN`, `CMD`, `ENTRYPOINT`, `COPY` and `ADD` instructions that follow it in the Dockerfile.
- `ENV` sets the environment variable `<key>` to the value `<value>`.
- `EXPOSE` informs Docker that the container listens on the specified network ports at runtime.
- `CMD` provides defaults for an executing container.

### Build an image from a Dockerfile

```bash
# run this command in the directory where the Dockerfile is located
$ docker build -t <image_name>:<tag> .

# example
$ docker build -t myapp:v1.0.0 .
```

To check the image you just built, run the following command:

```bash
$ docker images | grep myapp
```

By using the command above, you could check if the image you just built is in the list.

### Run a container from an image

```bash
$ docker run -it --name <container_name> <image_name>:<tag>
```
