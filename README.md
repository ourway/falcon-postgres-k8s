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
mkcert app.london-man.com london-man.com "*.london-man.com" dev.london-man.com
mv app.london-man.com+3-key.pem key.pem
mv app.london-man.com+3.pem cert.pem
```
and push it to secrets
```bash
kubectl create secret tls app.london-man.com.tls --key key.pem --cert cert.pem -n first
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

for google cloud, create an ip address:
```bash
gcloud compute addresses create london-man-ip --global
```
and fetch the ip:
```bash
gcloud compute addresses describe london-man-ip --global
```
