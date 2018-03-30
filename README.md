# wazo-router-confd-client

A python client library to access wazo-router-confd

## Usage

### Creating a client

```python
from wazo_router_confd_client import Client
client = Client('<wazo router hostname>', token='<auth token>')
```

## Config

### Fetching the server config

```python
client.config.get()
```
## Debian package

Follow the following steps to build a debian package for wazo-router-confd-client manually.

1. Copy the source directory to a machine with all dependencies installed

```sh
rsync -av . <builder-host>:~/wazo-router-confd-client
```

2. On the host, increment the changelog

```sh
dch -i
```

3. Build the package

```sh
dpkg-buildpackage -us -uc
```
