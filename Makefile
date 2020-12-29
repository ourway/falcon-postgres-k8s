push: export FAL_VER=4
push:
	@docker build --build-arg FAL_VER=$(FAL_VER) -t farshidashouri/fal:$(FAL_VER) .
	@docker push farshidashouri/fal:$(FAL_VER)
	@cat *.yaml | gsed 's/{{FAL_VER}}/$(FAL_VER)/g' | kubectl apply -f - --namespace=first

status:
	@kubectl get deployments,services -o wide --namespace=first

ping:
	@curl -fsSL 192.168.64.20:30009 | json_pp
