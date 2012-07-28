packages: pypi rpm deb

pypi:
	python setup.py build
	python setup.py sdist

rpm:

deb:

clean:
	rm -rf ./build ./dist ./pyagent.egg-info
