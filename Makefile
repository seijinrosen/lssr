test:
	poetry run pytest --capture=no --cov=lssr --cov-report=term-missing --cov-report=html

update:
	python -m pip install --upgrade pip setuptools wheel

init:
	python3.7 -m venv .venv/
	poetry install
	direnv allow
