up:
	sudo docker-compose -f docker-compose.yaml up --build -d
down:
	sudo docker-compose -f docker-compose.yaml down

run tests:
	sudo docker-compose -f docker-compose-test.yaml up -d
down tests:
	sudo docker-compose -f docker-compose-test.yaml down

setup project:
	poetry shell
	poetry config virtualenvs.create false \
	&& poetry install --no-dev --no-interaction --no-ansi --no-root
