# setup

#  1 Avoid unnecessary privileges

## 1.1 Rootless containers#1.1 Rootless containers

```
FROM alpine:3.12
# Create user and set ownership and permissions as required
RUN adduser -D myuser && chown -R myuser /myapp-data
# ... copy application files
USER myuser
ENTRYPOINT ["/myapp"]
```

## 1.2 Don’t bind to a specific UID#1.2 Don’t bind to a specific UID

```
RUN mkdir /myapp-tmp-dir && chown -R myuser /myapp-tmp-dir
USER myuser
ENTRYPOINT ["/myapp"]
```

## 1.3 Make executables owned by root and not writable
