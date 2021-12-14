RUN_FILE = run.py

install:
	pip install -r requirements.txt
	pip install .

run:
	python $(RUN_FILE)