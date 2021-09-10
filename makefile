pypi=test

.PHONY: test
test:
	@echo "===== Running pytest ====="
	pytest -vv

	@echo

.PHONY: black
black:
	@echo "===== Blacking ====="
	black . --skip-string-normalization

	@echo

.PHONY: build
build:
	@echo "===== Cleaning dist directory ====="
	rm -rf dist

	@echo

	@echo "===== Building python source archive and built distribution ====="
	python -m build

.PHONY: upload
upload:
	@echo "===== Uploading package to $(pypi) PyPI ====="
ifeq ($(strip $(pypi)), test)
	python -m twine upload --repository testpypi dist/*

	@echo

else ifeq ($(strip $(pypi)), real)
	python -m twine upload dist/*

	@echo

else
	@echo "Unknown Index"
	exit 1

endif
