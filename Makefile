.PHONY: install, run, lint
SHELL := /bin/bash

RUN_FILE = run.py

install:
	pip install -r requirements.txt
	pip install .

run:
	python $(RUN_FILE)

lint:
	mypy rr_light tests