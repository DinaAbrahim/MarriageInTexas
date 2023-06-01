#makefile

#files to make 
all: lastNames.txt femaleNames.txt compare.txt average.txt plot.pdf

#files to remove
clean:
	rm lastNames.txt femaleNames.txt compare.txt average.txt plot.pdf

#make lastNames.txt by reading Names_2010Census.csv and running lastNames.py
lastNames.txt: Names_2010Census.csv lastNames.py
	python3 lastNames.py >lastNames.txt

#make femaleNames.txt by reading AllMarriages.gz and running femaleNames.py
femaleNames.txt: AllMarriages.gz femaleNames.py
	python3 femaleNames.py >femaleNames.txt

#make compare.txt by reading lastNames.txt and femaleNames.txt and running compare.py
compare.txt: lastNames.txt femaleNames.txt compare.py
	python3 compare.py >compare.txt

#make average.txt by reading compare.txt and running average.py
average.txt: compare.txt average.py
	python3 average.py >average.txt

#make plot.pdf by running plot.py
plot.pdf: plot.py
	python3 plot.py 
