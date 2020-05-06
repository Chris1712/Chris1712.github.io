---
layout: post
title:  "Docker extras"
author: Chris
tags: engineering
---
There are of course plenty of guides on starting with docker, and the basics are very easy to pick up and get going with. So instead of retreading the basics, I'm going to list a few small features of docker I didn't come across until later in my use, but which are interesting and/or useful:

### `docker commit`

[Link to the official documentation](https://docs.docker.com/engine/reference/commandline/commit/)

As per the [storage driver documentation](https://docs.docker.com/storage/storagedriver/), a container's filesystem is effectively another writeable layer on top of the read only image layers. The 'docker commit' command creates an image from the current state of the container, very useful for testing purposes and quick sharing.

### `--network="host"`

[Link to the official documentation](https://docs.docker.com/engine/reference/run/#network-settings)

It's possible to run a container configured to use your host network interface directly - that is, with no explicit port forwarding required, as if you were running the process natively. Again this is useful for testing purposes, but the documentation also suggests this mode for containers where very high network performance is important - removing the virtualisation layer improves performance significantly.

There's a similar option for `--network="none"` which removes all networking, helpful in cases where isolating a container is required.

### `FROM scratch`

[Link to the official documentation](https://docs.docker.com/develop/develop-images/baseimages/#create-a-simple-parent-image-using-scratch)

Generally we build our images from other images provided by docker or the community, but of course it must be possible to start from scratch, right? If you wish to do so, 'scratch' is the minimal docker image top which all others are ultimately based.
