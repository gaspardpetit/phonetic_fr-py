PYTHON ?= python
TEST_ARGS ?=

.PHONY: test
test:
	@$(PYTHON) -m pytest $(TEST_ARGS)

.PHONY: check
check:
	@$(PYTHON) -m pylint $(shell git ls-files '*.py')
