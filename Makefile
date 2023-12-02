download:
	@echo "downloading data..."
	@echo curl https://data.cityofnewyork.us/api/views/4p5c-cbgn/rows.csv?accessType=DOWNLOAD --output data/data.csv

install | i:
	@echo "installing dependencies..."
	@poetry install

lint:
	@echo "lint checking..."
	@flake8

test:
	@echo "running test cases..."
	@nose2 --config=nose2.cfg -v -F