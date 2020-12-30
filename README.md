```bash
brew install kubectl
brew install minikube
brew install gsed
brew install hyperkit
```
after installing minikube, create a cluster:
```bash
inikube config set driver hyperkit
minikube delete
minikube start --vm=true
minikube addons enable ingress 
minikube addons enable ingress-dns
minikube addons enable logviewer
minikube status
```
install certificate related tools
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
rm *.pem
mkcert app.london-man.com london-man.com "*.london-man.com" dev.london-man.com
mv app.london-man.com+3-key.pem key.pem
mv app.london-man.com+3.pem cert.pem
```





for google cloud, create an ip address:
```bash
gcloud compute addresses create london-man-ip --global
```
and fetch the ip:
```bash
gcloud compute addresses describe london-man-ip --global
```
