.PHONY : test
.PHONY : coverage
.PHONY : packages
.PHONY : pypi
.PHONY : rpm
.PHONY : deb
.PHONY : clean

test:
	find pyagent/test -name '*[^_].py' -print0 | xargs -0 nosetests

coverage:
	find pyagent/test -name '*[^_].py' -print0 | xargs -0 nosetests --with-coverage --cover-package="pyagent"

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
