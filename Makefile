clean:
	rm -rf ./build/
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*~' -exec rm -rf {} +
	find . -name '.*~' -exec rm -rf {} +
	find . -name 'Thumbs.db' -exec rm -rf {} +
	find . -name '.DS_Store' -exec rm -rf {} +

build:
	pip install -r requirements.txt

test:
	python3 -m pytest tests/

lint:
	black . --check
	isort . --check-only

coverage:
	python3 -m pytest --cov=src --cov-report=term-missing --cov-report=html