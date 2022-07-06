test:
	poetry run pytest --capture=no --cov=lssr --cov-report=term-missing --cov-report=html

init:
	python3.7 -m venv .venv/
	poetry install
	direnv allow
