start:
	@make clean
	@docker-compose up --build --remove-orphans -d
	@echo "waiting 10 seconds to start the server"
	@sleep 10

clean:
	@docker-compose stop
	@docker-compose rm -f
	@docker-compose kill
	@docker volume prune -f
	@docker network prune -f

push: export FAL_VER=9
push:
	@docker build --target deployment --build-arg FAL_VER=$(FAL_VER) -t farshidashouri/fal:$(FAL_VER) .
	@docker push farshidashouri/fal:$(FAL_VER)
	@cat *.yaml | gsed 's/{{FAL_VER}}/$(FAL_VER)/g' | kubectl apply -f - --namespace=first

status:
	@kubectl get deployments,services -o wide --namespace=first

ping:
	@curl -fsSL 192.168.64.20:30009 | json_pp

shell:
	@docker-compose exec web bash
