SETUP_FILE = setup.py
RUN_FILE = run.py

install:
	pip install -r requirements.txt
	python $(SETUP_FILE)

run:
	python $(RUN_FILE)