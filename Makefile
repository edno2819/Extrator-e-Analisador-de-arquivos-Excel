setup:
	pyenv

install:
	@poetry install

format:
	blue .
	prospector --with-tool pep257

test:
	pytest -v
