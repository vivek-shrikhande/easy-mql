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