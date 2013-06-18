clean:
	rm *.pyc experimental/*.pyc

testall:
	ls *.py | perl -pe 's/(.*)\.py/\1/' | xargs -n 1 python -m unittest -v

tar:
	cd .. ; tar -vzcf algorithm.tar.gz --exclude '.git/*' algorithm

backup: tar
	scp ../algorithm.tar.gz zebra.hot:
