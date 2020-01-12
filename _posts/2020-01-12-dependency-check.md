---
layout: post
title:  "Validating dependencies with DependencyCheck"
author: Chris
tags: engineering CI
---
While securing the code you write yourself is important, it's just as vital to validate the other code that you're shipping - for example a modern Spring Boot project can easily end up including dozens of other jars, any one of which can have vulnerabilities just as severe as anything in your own code.

There are various ways to keep on top of this, the example I have today is a tool called [DependencyCheck](https://jeremylong.github.io/DependencyCheck) - it addresses the issue by scanning your included dependencies against databases of known vulnerabilities. It's vital to include such a tool in your build processes so that you can be aware of when your dependencies need updating or replacing.

It includes checking for Java and .NET dependencies, and has experiemental support for several other languages. And it can be run through the command line, or as a Jenkins plugin, but also as a Maven plugin. I prefer that option since once it's set up you have a configuration that's nicely reproducible between a dev's local environment and your build machines. The rest of this post covers setting up Maven to do this, some basic understanding of Maven and Java will be required.

### Setting up Maven with DependencyCheck

As a first run, `mvn org.owasp:dependency-check-maven:check` will generate a report in target/dependency-check-report.html. Note that in a corporate environment there may be some proxy and https certification issues to address before it'll be able to access the online databases - if necessary, make sure you've got a proxy configured in ~/.m2/settings.xml:

```
<proxies>
  <proxy>
    <id>httpproxy</id>
    <active>true</active>
    <protocol>http</protocol>
    <host>YOUR_PROXY_IP</host>
    <port>YOUR_PROXY_PORT</port>
    <nonProxyHosts>localhost</nonProxyHosts>
  </proxy>
</proxies>
```

You may also need to supply a HTTPS certificate to your JRE using keytool, if your environment uses any kind of custom root certificates for traffic inspection.

Finally, here's an example maven profile that you could use as a stage in a build process, for identifying builds with security issues:

```
<profile>
  <id>DependencyCheck</id>
  <build>
    <plugins>
      <plugin>
        <groupId>org.owasp</groupId>
        <artifactId>dependency-check-maven</artifactId>
        <version>5.2.4</version>
        <configuration>
          <!-- Configure the build to fail if any vulns with CVSS3 score =>7 (High) -->
          <!-- See https://nvd.nist.gov/vuln-metrics/cuss -->
          <failBuildoncvss>7</failBuildonCvss>
          <suppressionFile>dependency-check-suppress.xml</suppressionFile>
        </configuration>
        <executions>
          <execution>
            <goals>
              <goal>check</goal> 
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</profile>
```
