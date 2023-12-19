download:
	@echo "downloading data..."
	@echo curl https://data.cityofnewyork.us/api/views/4p5c-cbgn/rows.csv?accessType=DOWNLOAD --output data/data.csv

install:
	@echo "installing dependencies..."
	@poetry install --only main

lint:
	@echo "lint checking..."
	@flake8

test:
	@echo "running test cases..."
	@nose2 --config=nose2.cfg -v -F

coverage:
	@echo "running test coverage..."
	@coverage report ./test/*_test.py