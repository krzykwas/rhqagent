.PHONY : test
.PHONY : coverage

test:
	find test -name '*[^_].py' -exec nosetests {\} \;

coverage:
	find test -name '*[^_].py' -exec nosetests --with-coverage {\} \;

