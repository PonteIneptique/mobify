#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pattern.en import parse, pprint, tag, singularize, pluralize, sentiment, wordnet
import string, re

def getOccurencies(dico, lis):
	synlist = {}
	
	#Loop on chapters, j is the key, dico[j] is the dictionnary of this chapter with a child "fulltext"
	for j in dico:
		c = dico[j]["fulltext"]
		wordpos = {}
		exclude = set (string.punctuation)
		#c = ''.join(ch for ch in c if ch not in exclude)
		#print c

		#Loop on words in list
		c = c.lower()
		for i in range(len(c)):
			for word in lis:
				if c[i:len(word)+i] == word:
					wordpos[i] = word

		"""
		for l in lis:
			wlen = 0
			for pos, words in enumerate(c.split()):
				#print words
				#wlen += len(words)
				#print words
				#for en, char in enumerate(c):
				if l == words and l not in wordpos:
					#if not l in wordpos:
					wordpos[pos] = l
					#break
					#wordpos[l] = pos
			"""
		#End of word loop

		#Get synonyms
		for l in lis:
			syns = wordnet.synsets(l)
			for k in syns:
				if not l in synlist:
					synlist[l] = []
				synlist[l].extend(k.synonyms)
		#End of synonyms loop

		#We update dico
		dico[j]["occurencies"] = wordpos

	#End of loop on chapters
	setsyn = set()
	lis1 = []
	for word in synlist:
		synlist[word] = list(set(synlist[word]))
	#print(synlist)
	return dico, synlist

