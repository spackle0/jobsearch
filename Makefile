PROJECT_NAME=jobsearch
APP_NAME=intertraq
VERSION=0.1.0
# For build process, minimum test coverage required to pass testing
MIN_COVERAGE=0

$(info ========================================)
$(info App Name=${APP_NAME})
$(info Version=${VERSION})
$(info Min Test Coverage=${MIN_COVERAGE})
$(info ========================================)

.PHONY: run
run:
	poetry run python manage.py runserver

# Update semver per .bumpversion.cfg
.PHONY: bump_major
bump_major:
	poetry run bumpversion --list major

.PHONY: bump_minor
bump_minor:
	poetry run bumpversion --list minor

.PHONY: bump_patch
bump_patch:
	poetry run bumpversion --list patch

.PHONY: lint
lint:
	@echo "Flake8 running"
	-poetry run flake8 ${APP_NAME}
	@echo "Pylint running"
	-poetry run pylint ${APP_NAME}

.PHONY: dbmigrate
dbmigrate:
	# Generate a new .py file in versions folder with changes
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

.PHONY: format
format:
	poetry run isort --skip migrations ${APP_NAME}
	poetry run black --exclude="migrations/" ${APP_NAME}

.PHONY: sec
sec:
	poetry run bandit ./intertraq
	poetry run pyt -a D ./intertraq
