install:
	pip install -U pip &&\
		pip install -r 1-Introduction/1.2-Configuring-Your-Environment/requirements.txt

format:
	black 1-Introduction/*/*.ipynb