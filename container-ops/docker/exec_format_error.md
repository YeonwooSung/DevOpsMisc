# exec user process caused "exec format error"

When you build your docker image on a different architecture than the one you are running it on, you may get the following error:

```bash
standard_init_linux.go:211: exec user process caused "exec format error"
```

The reason for this error is that the architecture of the image you are trying to run is different from the one you are running it on.
For example, if you build an image on an x86_64 machine and try to run it on an ARM machine, you will get the error above.
Similarly, if you build an image on an M1 Macbook and try to run it on an Intel x86_64 cloud machine, you will get the same error.

To solve this problem, you need to build your image on the same architecture as the one you are running it on.
Luckily, Docker provides a way to do this by using the `--platform` flag.

```bash
$ docker build --platform linux/amd64 -t <image_name>:<tag> .
```

For clearity, it is better to add the platform infromation at the end of the tag.

```bash
$ docker build --platform linux/amd64 -t <image_name>:<tag>-amd64 .
```
