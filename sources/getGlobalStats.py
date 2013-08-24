#!/usr/bin/env/ python3
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

def getGlobalStats(dico):
	#we get every chapter
	stats = {}
	for chapter in dico:
		#Create new key
		

		#Get every lemma

		for lemma in dico[chapter]["lemma"]:

			#Create a key shortcut
			lem = dico[chapter]["lemma"][lemma]

			if lem[1] in stats:
				stats[lem[1]] += 1
			else:
				stats[lem[1]] = 1

		#End Lemma Loop
	#End chapter loop	
	return stats