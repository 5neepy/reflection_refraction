.PHONY: install, run, lint
SHELL := /bin/bash

RUN_FILE = run.py

install:
	pip install -r requirements.txt
	pip install .

run:
	python $(RUN_FILE)

lint:
	flake8 rr_light tests
	mypy rr_light tests

format:
	isort rr_light tests
	black rr_light tests

unit-test:
	pytest -v --runxfail