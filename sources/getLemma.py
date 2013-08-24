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
			}

		}
	}
"""

from pattern.en import parse

def getLemma(dico):

	#we get every chapte
	for chapter in dico:
		#We create the new part in it
		dico[chapter]["lemma"] = {}

		#Then we get every sentence
		for sentence in dico[chapter]["sentences"]:

			#We parse it
			temp = parse(dico[chapter]["sentences"][sentence], tokenize = True, tags = True, chunks = False, relations = False, lemmata = True, default = 'NN', light = True)

			#We split it
			temp = temp.split()
			for weird in temp:
				for temp2 in temp:
					for triple in temp2:
						key = sentence + " " + triple[0]
						dico[chapter]["lemma"][key] = (triple[1],triple[2])

				#print(each)

			#print(temp)
		#End of sentence loop

	#End of chapter loop

	#We return our data
	return dico
