#!/usr/bin/env/ python
from getText import getText
from getChapter import getChapter
from getSentence import getSentence
from getLemma import getLemma
from getStats import getStats
from getGlobalStats import getGlobalStats
from getSentiments import getSentiments
from getGlobalSentiments import getGlobalSentiments
from getOccurencies import getOccurencies
from getSortedStats import getSortedStats
from useSynos import useSynos

text = getText("mobydick.txt")

Dictionnary = getChapter(text)

lis = ["whale"]

Dictionnary, synos = getOccurencies(Dictionnary,lis)

Dictionnary, synos = useSynos(Dictionnary,synos)

Dictionnary = getSentence(Dictionnary)

Dictionnary = getLemma(Dictionnary)

Dictionnary = getStats(Dictionnary)


Dictionnary = getSentiments(Dictionnary)

globalStats = getGlobalStats(Dictionnary)

#PRINTS
Polarity, Subjectivity = getGlobalSentiments(Dictionnary)

#print Dictionnary

print getSortedStats(globalStats)

print "Global polarity is : " + str(Polarity) + " \nGlobal Subjectivity is : " + str(Subjectivity) 