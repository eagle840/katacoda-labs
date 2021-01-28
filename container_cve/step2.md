# run vulnerabilities scans against images

Lets take a look at the images we have stored on the system

`docker images`{{execute}}

And take a look at a base ubuntu image and some others.


`trivy ubuntu:18.04`{{execute}}

`trivy ubuntu:18.04 | grep Total`{{execute}}

`trivy -s CRITICAL --ignore-unfixed ubuntu:18.04`{{execute}}

Lets take a look at a some other images

`trivy centos:7.6.1810 | grep Total`{{execute}}

`trivy debian:10.2-slim | grep Total`{{execute}}

We can take a look at a much small image and see the reduction is vulnerabilities.

`trivy alpine:3.11`{{execute}}

`trivy jfloff/alpine-python:3.8-slim`{{execute}}

