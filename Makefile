up:
	sudo docker-compose -f docker-compose.yaml up --build -d
down:
	sudo docker-compose -f docker-compose.yaml down

runtest:
	sudo docker-compose -f docker-compose-test.yaml up -d
downtest:
	sudo docker-compose -f docker-compose-test.yaml down

show results:
	sudo docker-compose -f docker-compose-test.yaml logs -f

setup project:
	poetry config virtualenvs.create false \
	&& poetry install --no-dev --no-interaction --no-ansi --no-root
myenv:
	poetry shell
