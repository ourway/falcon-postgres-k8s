install the following:
```bash
brew install nss
brew install mkcert
```
and then
```bash
mkcert --install
```
then restart the browser.

After than, generate the cert in cert folder:
```bash
mkcert app.fleetman.com fleetman.com "*.fleetman.com" app.london-man.com london-man.com "*.london-man.com" example.test localhost 127.0.0.1 ::1
```
rename generated files to simple ones push it to secrets:
```bash
kubectl create secret tls app.fleetman.com.tls --key key.pem --cert cert.pem -n first
```

the certs should be ok now
