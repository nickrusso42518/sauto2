# Default goal runs the "test" target
.DEFAULT_GOAL := all

.PHONY: all
all: clean lint unit

.PHONY: lint
lint:
	@echo "Starting  lint"
	# find . -name "*.yaml" | xargs yamllint -s
	find . -name "*.py" | xargs pylint
	find . -name "*.py" | xargs black -l 82 --check
	@echo "Completed lint"

.PHONY: unit
unit:
	@echo "Starting  unit tests"
	python m2/get_computers.py
	python m3/tg_test.py
	python m4/umb_enf_test.py
	python m4/umb_inv_test.py
	python m4/umb_rep_test.py
	@echo "Completed unit tests"

.PHONY: clean
clean:
	@echo "Starting  clean"
	# find . -name "*.pyc" | xargs -r rm
	find . -name "*.pyc" | xargs rm
	@echo "Starting  clean"
