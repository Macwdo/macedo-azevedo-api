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
	-@ coverage run manage.py test --exclude-tag=WIP
	
	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_prod_parallel:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ coverage run manage.py test --exclude-tag=WIP --parallel

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_dev:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ coverage run manage.py test

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html

test_dev_parallel:
	@echo "Cleaning up coverage files 🧹"
	-@ coverage erase

	@echo "Running tests 🧪..."
	-@ coverage run manage.py test --parallel

	@echo "\n\n"
	@echo "Test results 📊..."

	-@ coverage html



# Database

migrate:
	@echo "Running migrations 🚚"
	-@ python manage.py migrate

migrations:
	@echo "Creating migrations 🚚"
	-@ python manage.py makemigrations

remove_migrations:
	@echo "Removing migrations 🚚"
	-@ rm -rf **/migrations/00*

# Admin

createadmin:
	@echo "Creating admin user 🦸"
	-@ python manage.py createsuperuser --email admin@admin.com


createsuperuser:
	@echo "Creating super user 🦸"
	-@ python manage.py createsuperuser


# Static files
collectstatic:
	@echo "Collecting static files 📦"
	-@ python manage.py collectstatic --noinput

# Infra 
build:
	@echo "Building the project 🏗️"
	-@ docker build -t macedo-azevedo-api .

up:
	@echo "Setting up Application Infrastructure... 🚀"
	-@ docker compose down
	-@ docker compose -f docker-compose-dev.yml up -d

down:
	@echo "Stopping the project 🛑"
	-@ docker compose down

clean:
	@echo "Cleaning up the project 🧹"
	-@ docker compose down
	-@ sudo rm -rf ./.data

# Run
run:
	@echo "Running the project in development mode 🚀"
	-@ python manage.py runserver


# Setup
setup_dev:
	@echo "Setting up the development environment 🚀"
	-@ uv sync

	@echo "Copying the .env file 🚀"
	-@ cp dotenv_files/.env.sample .env
