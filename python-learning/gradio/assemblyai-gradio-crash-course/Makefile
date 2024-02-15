# src: https://stackoverflow.com/a/59335943
all: install run

install: venv
	# Activate venv and install smthing inside
	. .venv/bin/activate && pip install -r requirements.txt

venv:
	: # Create venv if it doesn't exist
	test -d .venv || python3 -m venv .venv && pip install --upgrade pip setuptools

run:
	: # Or see @wizurd's answer to exec multiple commands
	. .venv/bin/activate && (\
		python3 -m pytest -v\
	)

version:
	: # Run your app here, e.g
	: # determine if we are in venv,
	: # see https://stackoverflow.com/q/1871549
	. .venv/bin/activate && pip -V

clean:
	rm -rf .venv

format:
	. .venv/bin/activate && black . && isort .
