test:
	poetry run pytest --capture=no --cov=lssr --cov-report=term-missing --cov-report=html

switch:
	git switch --create develop

after-develop-merged:
	git switch main
	git pull --prune
	git branch --delete develop
	make switch

update:
	python -m pip install --upgrade pip setuptools wheel

clean:
	rm -r .venv/
	rm -r .pytest_cache/
	rm -r .tox/
	rm -r htmlcov/
	rm .coverage

init:
	python3.7 -m venv .venv/
	poetry install
	direnv allow
