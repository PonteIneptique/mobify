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

def getGlobalSentiments(dico):
	#we get every chapter
	pol = []
	sub = []
	for chapter in dico:

		#Get every lemma

		for key in dico[chapter]["sentiments"]:

			#Create a key shortcut
			lem = dico[chapter]["sentiments"][key]

			pol.append(lem[0])
			sub.append(lem[1])

		#End Lemma Loop
	#End chapter loop	

	Polarity = sum(pol) / len(pol)
	Subjectivity = sum(sub) / len(sub)

	return Polarity, Subjectivity
	return stats