PROJECT_NAME := skynet_ai
ENV_NAME := skynet_ai_env
IMAGE_LOCATION := .

.PHONY: build run kill debug tests clear-docker

build:
	@echo 'Build docker image from Dockerfile'
	docker-compose build
	#docker build -q -t $(PROJECT_NAME):latest $(IMAGE_LOCATION)

run: build
	@echo 'Run docker image as a container'
	docker-compose up
	#docker run --rm --name $(PROJECT_NAME) -p 5000:5000 $(PROJECT_NAME):latest
		# -d

kill:
	@echo 'Kill docker container if running'
	docker kill $(PROJECT_NAME) || true

debug: run
	@echo 'Open shell in container'
	docker exec -it $(PROJECT_NAME) sh

tests: run
	@echo "Lol it's a hackathon"

clear-docker:
	@echo 'Clear all docker images'
	sh scripts/clear_docker.sh > /dev/null

url:
	@echo 'Get url for local server'
	sh scripts/get_ngrok_url.sh