#!/usr/bin/env/ python3

from pattern.en import sentiment

def getMood(dico):
	for chapter in dico:
		#Create new key
		dico[chapter]["sentiments"] = {}

		#Get every sentence
		for sentence in dico[chapter]["sentences"]:
			stce = dico[chapter]["sentences"][stce]
			dico[chapter]["sentiments"][sentence] = sentiment(stce)
		#End sentence loop



	#End chapter sentence