download:
	@echo "downloading data..."
	@echo curl https://data.cityofnewyork.us/api/views/4p5c-cbgn/rows.csv?accessType=DOWNLOAD --output data/data.csv

install:
	@echo "installing dependencies..."
	@poetry install --only main

lint:
	@echo "lint checking..."
	@flake8