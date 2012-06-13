.PHONY : test
.PHONY : coverage

test:
	find test -name '*[^_].py' -print0 | xargs -0 nosetests

coverage:
	find test -name '*[^_].py' -print0 | xargs -0 nosetests --with-coverage --cover-package=agent,data_provider,settings
