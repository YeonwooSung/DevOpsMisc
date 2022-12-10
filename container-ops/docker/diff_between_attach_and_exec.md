# Difference between attach and exec commands

Both `docker attach` and `docker exec` are used to enter a container. However, they are different in the following aspects:

1. `docker exec`

    - executes a command in a running container
    - is interactive
    - is used to enter a running container

2. `docker attach` attaches to a running container

    - is not interactive
    - is used to attach to a running container

The term "attach to a running container" might be confusing.
What it actually means is that you can attach local standard input, output, and error streams to a running container, where `docker exec` simply runs a command in a running container.
