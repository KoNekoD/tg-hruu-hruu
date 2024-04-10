python_install:
	python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt

update_requirements:
	./venv/bin/pip freeze > requirements.txt