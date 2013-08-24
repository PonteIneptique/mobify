#!/usr/bin/env/ python
"""
	WHAT I HAVE
	Dictionnary = {
		ChapterName = {
			"fulltext" = fulltext,
			"occurencies" = {
				charPos = wordFound
			},
			"sentences" = {
				charPos = sentenceWithWordFound
			},
			lemma = {
				"UID UID2 WORD" = (
					WordType,
					Lemma
					)
			}

		}
	}
"""

def getStats(dico):
	#we get every chapter
	for chapter in dico:
		#Create new key
		dico[chapter]["stats"] = {}

		#Get every lemma

		for lemma in dico[chapter]["lemma"]:

			#Create a key shortcut
			lem = dico[chapter]["lemma"][lemma]

			if lem[1] in dico[chapter]["stats"]:
				dico[chapter]["stats"][lem[1]] += 1
			else:
				dico[chapter]["stats"][lem[1]] = 1

		#End Lemma Loop
	#End chapter loop	
	return dico