FROM alpine:latest

USER root

RUN apk add --no-cache \
    python3
