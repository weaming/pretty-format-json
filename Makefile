.PHONY: test build install publish

# the library name
name = pretty-format-json
# may change to pip3 or python3 -m pip, etc.
# python2 do not support write csv in unicode
pip = pip

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
	$(pip) uninstall $(name)

clean:
	rm -fr build dist *.egg-info
