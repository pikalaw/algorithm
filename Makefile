clean:
	rm -f *.pyc experimental/*.pyc

testall:
	ls *.py | perl -pe 's/(.*)\.py/\1/' | xargs -n 1 python -m unittest -v

tar:
	cd .. ; tar -vzcf algorithm.tar.gz --exclude '.git/*' --exclude '*.pyc' algorithm

backup: tar
	scp ../algorithm.tar.gz zebra.hot:
