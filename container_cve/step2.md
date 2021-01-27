# run vulnerabilities scans against images


`docker images`{{execute}}

`trivy ubuntu:18.0`{{execute}}

`trivy ubuntu:18.04`{{execute}}


`trivy ubuntu:18.04 | grep Total`{{execute}}

`trivy -s CRITICAL --ignore-unfixed ubuntu:18.04`{{execute}}

`trivy centos:7.6.1810 | grep Total`{{execute}}

`trivy debian:10.2-slim | grep Total`{{execute}}

`trivy alpine:3.11`{{execute}}

`trivy jfloff/alpine-python:3.8-slim`{{execute}}

`history`{{execute}}