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

packages: pypi rpm

pypi:
	# Re-create destination directory
	rm -rf ./packages/pypi
	mkdir -p ./packages/pypi
	# Create a manifest on-the-fly
	echo "include COPYING" > MANIFEST.in
	echo "include run-pyagent.sh" >> MANIFEST.in
	# Run setup.py
	python setup.py build
	python setup.py sdist
	# Delete manifest and a left-over directory
	rm -rf MANIFEST.in
	rm -rf ./pyagent.egg-info
	# Move build and dist to the destination directory
	mv build dist packages/pypi/

rpm:
	# Re-create destination directory
	rm -rf ./packages/rpm
	mkdir -p ./packages/rpm

clean:
	rm -rf ./packages
