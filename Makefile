all: part0.py part1.py part2.py nosel.py success.py

nosel.py:
	pyuic5 nosel.ui -o nosel.py

success.py:
	pyuic5 success.ui -o success.py

part0.py:
	pyuic5 part0.ui -o part0.py

part1.py:
	pyuic5 part1.ui -o part1.py

part2.py:
	pyuic5 part2.ui -o part2.py


