.PHONY : test
.PHONY : coverage
.PHONY : packages

.PHONY : pypi
.PHONY : pypi_build_pkg
.PHONY : pypi_info
.PHONY : pypi_clean

.PHONY : fedora
.PHONY : fedora_build_pkg
.PHONY : fedora_info
.PHONY : fedora_clean

.PHONY : clean

# The hash of the HEAD commit
PYAGENT_GIT_COMMIT=$(shell git rev-parse HEAD)

###================================================================================================
# UNIT TESTS
###================================================================================================

test:
	find pyagent/test -name '*[^_].py' -print0 | xargs -0 nosetests

coverage:
	find pyagent/test -name '*[^_].py' -print0 | xargs -0 nosetests --with-coverage --cover-package="pyagent"

###================================================================================================
# PACKAGES
###================================================================================================

# Package the code
packages: pypi_build_pkg fedora_build_pkg pypi_info fedora_info

###================================================================================================
# PYTHON PACKAGE INDEX
###================================================================================================

# Package the code in the Python Package Index format
pypi: pypi_build_pkg pypi_info

pypi_build_pkg:
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

pypi_info:
	@echo "=================================================="
	@echo "Packages successfully created in ./packages/pypi"
	@echo "=================================================="

# Remove all files produced when packaging in the Python Package Index format
pypi_clean:
	rm -rf ./packages/pypi

###================================================================================================
# FEDORA
###================================================================================================

# Package the code in the Fedora native format
# First the Python code is tar-gzipped by pypi target and this archive will be used to build rpm
# Then the actual work is done
# At last, the changes done by pypi are reverted with clean_pypi
fedora: fedora_build_pkg fedora_info

# Build an RPM package for Fedora
fedora_build_pkg:
	git archive $(PYAGENT_GIT_COMMIT) -o ./packages/fedora/rpmbuild/SOURCES/pyagent-$(PYAGENT_GIT_COMMIT).tar
	cd ./packages/fedora/rpmbuild/SPECS;\
		rpmbuild\
			--define "pyagent_git_commit $(PYAGENT_GIT_COMMIT)"\
			--define "_topdir $(PWD)/packages/fedora/rpmbuild"\
			-ba pyagent.spec

fedora_info:
	@echo "=================================================="
	@echo "Packages successfully created in ./packages/fedora"
	@echo "=================================================="

# Remove all files produces when packaging in the Fedora native format
fedora_clean:
	rm -rf ./packages/fedora/rpmbuild/SOURCES/*

###================================================================================================
# CLEAN
###================================================================================================

# Remove the files created during packaging
clean: pypi_clean fedora_clean
