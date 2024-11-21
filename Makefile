# Lint
check:
	@echo "Running lint check 🧹"
	-@ ruff check

lint:
	@echo "Running lint format 🧹"
	-@ ruff format & ruff check --fix

lint_unsafe:
	@echo "Running lint unsafe format 🧹"
	-@ ruff format & ruff check --unsafe-fixes --fix


# Test
test_prod:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	--@ cd src && coverage run manage.py test --exclude-tag=WIP
	
	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_prod_parallel:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ cd src && coverage run manage.py test --exclude-tag=WIP --parallel

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_dev:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ cd src && coverage run manage.py test

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_dev_parallel:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ cd src && coverage run manage.py test --parallel

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

# Database
migrate:
	@echo "Running migrations 🚚"
	-@ python src/manage.py migrate

migrations:
	@echo "Creating migrations 🚚"
	-@ python src/manage.py makemigrations

remove_migrations:
	@echo "Removing migrations 🚚"
	-@ rm -rf **/migrations/00*

# Admin
createadmin:
	@echo "Creating admin user 🦸"
	-@ python src/manage.py createsuperuser --email admin@admin.com

createsuperuser:
	@echo "Creating super user 🦸"
	-@ python src/manage.py createsuperuser

# Static files
collectstatic:
	@echo "Collecting static files 📦"
	-@ python src/manage.py collectstatic --noinput

# Infra 
up_prod:
	@echo "Running the project in production mode 🚀"
	-@ docker compose -f infra/docker-compose-prod.yml down
	-@ docker compose -f infra/docker-compose-prod.yml up -d

up_prod_build:
	@echo "Running the project in production mode 🚀"
	-@ docker compose -f infra/docker-compose-prod.yml down
	-@ docker compose -f infra/docker-compose-prod.yml up -d --build

run_prod:
	@echo "Running the project in production mode 🚀"
	-@ docker compose -f infra/docker-compose-prod.yml down
	-@ docker compose -f infra/docker-compose-prod.yml up


down_prod:
	@echo "Stopping the project in production mode 🛑"
	-@ docker compose -f infra/docker-compose-prod.yml down

up_dev:
	@echo "Setting up Application Infrastructure... 🚀"
	-@ docker compose -f infra/docker-compose-dev.yml down
	-@ docker compose -f infra/docker-compose-dev.yml up -d

up_dev_build:
	@echo "Setting up Application Infrastructure... 🚀"
	-@ docker compose -f infra/docker-compose-dev.yml down
	-@ docker compose -f infra/docker-compose-dev.yml up -d --build

run_dev:
	@echo "Running the project in development mode 🚀"
	-@ docker compose -f infra/docker-compose-dev.yml down
	-@ docker compose -f infra/docker-compose-dev.yml up

down_dev:
	@echo "Stopping the project 🛑"
	-@ docker compose -f infra/docker-compose-dev.yml down

clean:
	@echo "Cleaning up the project 🧹"
	-@ sudo rm -rf ./.data

attach:
	@echo "Attaching to the project 🚀"
	-@ docker attach macedo-azevedo-api

connect:
	@echo "Connecting to the project 🚀"
	-@ docker exec -it macedo-azevedo-api /bin/bash

## Build
build:
	@echo "Building the project 🏗️"
	-@ docker build -t macedo-azevedo-api .

build_nginx:
	@echo "Building nginx 🏗️"
	-@ cd infra/nginx && docker build -t macedo-azevedo-api-nginx .

# Nginx
nginx_log_error:
	@echo "Showing nginx error logs 📜"
	-@ docker exec -it macedo-azevedo-api-nginx tail -f /var/log/nginx/error.log

nginx_log_access:
	@echo "Showing nginx access logs 📜"
	-@ docker exec -it macedo-azevedo-api-nginx cat /var/log/nginx/access.log

# Run
run:
	@echo "Running the project in development mode 🚀"
	-@ python src/manage.py runserver

# Setup
setup_dev:
	@echo "Setting up the development environment 🚀"
	-@ uv sync

	@echo "Copying the .env file 🚀"
	-@ cp dotenv_files/.env.sample .env
