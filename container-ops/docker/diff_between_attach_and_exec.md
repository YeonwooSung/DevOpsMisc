# Difference between attach and exec commands

Both `docker attach` and `docker exec` are used to enter a container. However, they are different in the following aspects:

1. `docker exec`

    - executes a command in a running container
    - is used to enter a running container

2. `docker attach` attaches to a running container

    - is used to attach to a running container

## What does it mean?

The term "attach to a running container" might be confusing.
What it actually means is that you can attach local standard input, output, and error streams to a running container, where `docker exec` simply runs a command in a running container.

However, if the process in the container is not running in the foreground, for example it is a web application process which runs in the background, you cannot attach to it.
In this case, you can use `docker exec` to run a command in the container.
And when the container is paused while running the `docker exec`, the given command will be exited with the error.
