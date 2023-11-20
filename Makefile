install | i:
	@echo "installing dependencies..."
	@poetry install

lint:
	@echo "lint checking..."
	@flake8

test:
	@echo "running test cases..."
	@nose2 --config=nose2.cfg -v -F

run-py:
	@echo "main.py is running..."
	@python3 ./src/main.py

run-ipynb:
	@echo "main.ipynb is running..."
	@jupyter-notebook ./src/main.ipynb