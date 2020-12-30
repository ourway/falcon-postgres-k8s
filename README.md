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
cd cert
mkcert app.fleetman.com fleetman.com "*.fleetman.com" dev.fleetman.com
mv app.fleetman.com+3-key.pem key.pem
mv app.fleetman.com+3.pem cert.pem
```
and push it to secrets
```bash
kubectl create secret tls app.fleetman.com.tls --key key.pem --cert cert.pem -n first
```

the certs should be ok now
