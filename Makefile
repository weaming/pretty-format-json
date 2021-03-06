.PHONY: test build install publish

# the library name
name = pretty-format-json
# may change to pip3 or python3 -m pip, etc.

# it's not easy writting csv/yaml in unicode in python2
pip = pip3

test:
	cat test.json | python pretty/format.py

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

install: clean build
	$(pip) install --force-reinstall ./dist/*.whl

publish: clean build
	twine upload dist/* && git push --follow-tags

uninstall:
	pip uninstall $(name) -y
	pip3 uninstall $(name) -y

clean:
	rm -fr build dist *.egg-info
