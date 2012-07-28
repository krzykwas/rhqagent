packages: pypi rpm deb

pypi:
	python setup.py build
	python setup.py sdist

rpm:

deb:

clean:
	python setup.py clean --all
	rm -rf ./pyagent.egg-info
	rm -rf ./dist
