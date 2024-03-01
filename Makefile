ROOT = $(dir $(realpath $(firstword $(MAKEFILE_LIST))))


clean:
	find . -name '__pycache__' | xargs rm -rf
	rm -rf htmlcov .coverage .pytest_cache


format:
	python3 -m black abuelitosmx
	python3 -m isort abuelitosmx


lint:
	python3 -m pylint abuelitosmx


test:
	python3 -m pytest
