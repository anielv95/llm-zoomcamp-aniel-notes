install:
	pip install -U pip &&\
		pip install -r 1-Introduction/requirements.txt

format:
	black */*/*.ipynb &&\
		black */*.ipynb