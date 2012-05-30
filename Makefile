.PHONY : test
test:
	find test -name '*[^_].py' -exec nosetests {\} \;
