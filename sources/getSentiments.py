#!/usr/bin/env/ python

from pattern.en import sentiment

def getSentiments(dico):
	for chapter in dico:
		#Create new key
		dico[chapter]["sentiments"] = {}

		#Get every sentence
		for sentence in dico[chapter]["sentences"]:
			stce = dico[chapter]["sentences"][sentence]
			dico[chapter]["sentiments"][sentence] = sentiment(stce)
		#End sentence loop



	#End chapter sentence
	return dico