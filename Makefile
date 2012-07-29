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
	echo "include COPYING" > MANIFEST.in
	echo "include run-pyagent.sh" >> MANIFEST.in
	python setup.py build
	python setup.py sdist
	rm -rf MANIFEST.in
	rm -rf ./pyagent.egg-info

rpm:

deb:

clean:
	python setup.py clean --all
	rm -rf ./dist
