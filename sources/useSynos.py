#!/usr/bin/env/ python
from getOccurencies import getOccurencies

def useSynos(Dictionnary,synos):
	#{'whale': ['whale', 'giant', 'heavyweight', 'hulk']}
	for word in synos:
		Dictionnary = getOccurencies(Dictionnary,synos[word])
	return Dictionnary