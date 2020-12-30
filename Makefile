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

push: export FAL_VER=19
push:
	@docker build -f Dockerfile.app --target deployment --build-arg FAL_VER=$(FAL_VER) -t farshidashouri/fal:$(FAL_VER) .
	@docker build -f Dockerfile.frontend --target deployment --build-arg FAL_VER=$(FAL_VER) -t farshidashouri/sapper-frontend:$(FAL_VER) .
	@docker push farshidashouri/fal:$(FAL_VER)
	@docker push farshidashouri/sapper-frontend:$(FAL_VER)
	@cat *.yaml | gsed 's/{{FAL_VER}}/$(FAL_VER)/g' | kubectl apply -f - --namespace=first
	@kubectl rollout status --namespace=first deployment webapp
	@kubectl rollout status --namespace=first deployment frontend
	@make status
	@make ping

status:
	@kubectl get deployments,services,ingress -o wide --namespace=first

ping:
	@curl -fsSL app.fleetman.com/api/v1/ping | json_pp

shell:
	@docker-compose exec web bash

db-up:
	@docker-compose exec web alembic upgrade head

db-down:
	@docker-compose exec web alembic downgrade base

db-migration-state:
	@docker-compose exec web alembic current

db-migration-history:
	@docker-compose exec web alembic history --verbose

ipython:
	@docker-compose exec web ipython 

lint:
	@docker-compose exec web pylint -j 2 /app/dev

logs:
	@docker-compose logs -t -f --tail=all web

fmt:
	@docker-compose exec web isort -w 99 -m 3 --trailing-comma .
	@docker-compose exec web black -l 99 .
	@docker-compose exec web mypy /app/dev
	@make frontend-fmt

frontend-fmt:
	@docker-compose exec frontend node node_modules/prettier/bin-prettier.js --write --svelte-sort-order scripts-markup-styles ./**/*.svelte
