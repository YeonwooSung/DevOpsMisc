# Basic commands

## Pull an image

```bash
docker pull <image_name>
```

For example, if you want to pull an image of `ubuntu 18.04`:

```bash
docker pull ubuntu:18.04
```

## Build

```bash
docker build -t <image_name> .
```

## Run

```bash
docker run -it <image_name>
```

- `-i` : interactive mode
- `-t` : terminal mode

To run a container in the background:

```bash
docker run -d <image_name>
```

- `-d` : detached mode

## Enter a container

```bash
docker exec -it <container_id> /bin/bash
```

Instead of `/bin/bash`, you can also use `/bin/sh`.

The `docker attach` command is used to attach to a running container. It is similar to `docker exec` but it is not interactive. It is used to attach to a running container.

```bash
docker attach <container_id>
```

## Check logs

```bash
docker logs <container_id>
```

## List images

```bash
docker images
```

## List all containers

```bash
docker ps -a
```

## Remove a container

```bash
docker rm <container_id>
```

## Remove an image

```bash
docker rmi <image_id>
```
