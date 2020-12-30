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

Also push the env as config maps. we are going to ignore the sample postgres password and will use secrets for that.

```bash
kubectl create configmap -n first webapp-envs --from-env-file .env
```

create database secret
```
kubectl create secret generic database-password --from-literal=POSTGRES_PASSWORD=asecretvalue -n first
```
