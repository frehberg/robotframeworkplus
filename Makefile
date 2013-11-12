
chartdemo:
	PYTHONPATH=lib/  pybot --include chart demo/

clean:
	rm -f demo/*~ *.html *.xml *.svg lib/*~ ./*~ 
	rm -rf build dist

register:
	python setup.py register

upload:
	PYTHONPATH=~/lib/python python setup.py sdist upload

