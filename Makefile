clean:
	rm *.pyc

testall:
	ls *.py | perl -pe 's/(.*)\.py/\1/' | xargs -n 1 python -m unittest -v
