
chartdemo:
	PYTHONPATH=lib/ pybot --include chart demo/

clean:
	rm -f demo/*~ *.html *.xml lib/*~ ./*~
