---
layout: post
title:  "Postman scripting"
author: Chris
tags: postman
---

One of the tools I use daily when developing our REST API is [Postman](https://www.getpostman.com/). If you've not used Postman before, it's billed as an "API Development Environment", essentially allowing you to send HTTP requests from a flexible and clear GUI, while organising and saving them, and testing the responses received.

On top of the nice presentation Postman also has some features that elevate it beyond what you can do with a basic curl command, in particular the scripting functionality.

Our REST API requires a [bearer token](https://jwt.io/) for most paths; if a request doesn't include this as a header then it'll return a 401 unauthorised response. Postman has some helpful functionality 




Of course, you can do all of this with python, bash, or powershell, if you prefer avoiding to use another tool, but Postman is easy to get up and gives you a really simple, clean workflow for common tasks along with a nice presentation of your saved requests.
