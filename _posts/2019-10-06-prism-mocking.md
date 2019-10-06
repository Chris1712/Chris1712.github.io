 ---
layout: post
title:  "OpenAPI mocking with prism"
author: Chris
tags: engineering testing
---
When doing full-stack development as part of a team, adding a new feature often happens in the order:

1. Modify infrastructure (relational database, elastic etc.) to store whatever's required for the new feature
2. Add business layer (e.g. REST API) functionality
3. Update front-end to present the new feature to users.

In general doing steps 2 and 3 will rely on having a version of the previous step available to work on, and this can slow things down - but there are some powerful tools to help break these [schedule dependencies](https://en.wikipedia.org/wiki/Dependency_%28project_management%29).

The example I have today is a tool called [prism](https://stoplight.io/open-source/prism/), which breaks the dependency between steps 2 and 3 when you're using an OpenAPI specification to define your API. Once you've got your endpoints agreed and specified, prism can take your spec file and spin up a server that'll give realistic answers to your requests, which should be enough to let you get going on your front end development straight away.

First, install prism:

`npm install -g @stoplight/prism-cli`

Then, it's as simple as pointing prism at your spec file, here as an example I've used the venerable [petstore.yaml](https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml):

`prism mock petstore.yaml`

![prism mocking stdout]({{ site.url }}/img/prism-startup.png)

Now a curl to the endpoint will generate a response that complies with the spec:

![prism mocking curl resul]({{ site.url }}/img/prism-curl.png)

You can see here that the fields generated aren't particularly realistic, though - for example the string fields are just "string". If needed, you can improve this by adding [examples](https://swagger.io/docs/specification/adding-examples/) to your spec under the response or schema - if they're available then prism will pick from those. This is in general a good idea for improving the clarity of your spec, particularly if you expect it to be widely used, or if you're using it to generate documentation.

So if I edit petstore.yaml to add an example for the fields for the Pet object:

```
components:
  schemas:
    Pet:
      type: object
      required:
        - id
        - name
      properties:
        id:
          type: integer
          format: int64
          example: 5
        name:
          type: string
          example: Louise
        tag:
          type: string
          example: tag1
```

Now once prism is restarted more, the response will look a little saner:

![prism mocking curl resul]({{ site.url }}/img/prism-curl-examples.png)
