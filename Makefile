install | i:
	@echo "installing dependencies..."
	@poetry install

lint:
	@echo "lint checking..."
	@flake8

test:
	@echo "running test cases..."
	@nose2 --config=nose2.cfg -v -F
