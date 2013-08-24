#!/usr/bin/env/ python
"""
	WHAT I HAVE
	Dictionnary = {
		ChapterName = {
			"fulltext" = fulltext,
			"occurencies" = {
				charPos = wordFound
			},

			WHAT ID DO :
			"sentences" = {
				charPos = sentenceWithWordFound
			}

		}
	}
"""

def getSentence(dico):
	#We set our temporary dictionnary
	sentences = {}

	#Sentences end =
	ends = [".", "!", "?"]
	#Abreviations
	abrev = ["Mr", "Mrs", "Dr", "Jr"]

	#We get every chapter
	for chapter in dico:
		#We create the new dictionary if it doesnt exist
		if "sentences" not in dico[chapter]:
			dico[chapter]["sentences"] = {}

		#We go to every word we found
		for char in dico[chapter]["occurencies"]:
			#We get first character as char variable, and chapter["occurencies"]["word"]

			#We cut our text in a temp string which start at the word.
			#We are first looking for the end of the string
			temp = dico[chapter]["fulltext"][char:]


			tempEnds = -1
			tempBegin = -1

			#Check for every char in a loop
			for c in range(len(temp)):
				#print temp[c]
				#If temp[c] is an ending character
				if temp[c] in ends:
					#If temp_ends has not been declared
					if tempEnds < 0:
						#We check that c+1 exists
						if (c+1) <= (len(temp) - 1):
							temp_caps = -1

							#Until c + i is a space, we check if the character after it is a cap

							i = 1
							while temp[c+i] == " ":
								if temp[c+i+1].isupper():
									temp_caps = char + c+i
									break
									#print temp[c+i]+ " : Next one is cap" 

								i += 1

							#We have a temp caps, we just check the word before was not an abreviation
							if temp_caps >= 0:
								#Now we check fro abreviation
								is_abv = False
								for abv in abrev:
									c2 = c+2

									abv_qstion = temp[(c-len(abv)):c]

									if abv == abv_qstion:
										is_abv = True
										break

								#Then we check it is not a name abreviation like "H. G. Whale"
								if temp[c-1].isupper() and temp[c-2] == " ":
									is_abv = True



								if is_abv == False:
									tempEnds = temp_caps
									break


						#Else we set it to this char
						else:
							tempEnds = char + c +1
					#Else We break THE LOOP
					else:
						break


			#We are then looking for the start
			temp_r = dico[chapter]["fulltext"][char::-1]

			#Check for every char in a loop
			for c in range(len(temp_r)):

				#If temp[c] is an ending character
				if temp_r[c] in ends:
					if tempBegin < 0:
					#We check that c+1 exists
						if (c+1) <= (len(temp_r) - 1):
							#Until c + i is a space, we check if the character after it is a cap
							i = 1


							#If next one is lower, then start sentence
							if temp_r[c+i].islower():
								#But NOT if it is an abreviation
								is_abv = False

								for abv in abrev:
									#We set a second counter
									c2 = c+2

									#We get the same amount of character than in the abreviation, then register it into a var
									abv_qstion = temp_r[(c2-1):(c+1+len(abv))]

									#We compare the abreviation BACKWARD (because our string is) to the same amount of characters
									if abv[::-1] == abv_qstion:
										is_abv = True
										break


								if is_abv == False:
									tempBegin = char - (c-1)
									break

							#If it is a space
							elif temp_r[c+i] == " ":

								#START LOOP WHILE FOR WHITE SPACES
								while temp_r[c+i] == " ":
									
									if temp_r[c+i+1].islower():
										tempBegin = char - (c+i)
										#print temp_r[:c+i]
										break
										#print temp[c+i]+ " : Next one is cap" 

									i += 1
								#END LOOP WHILE FOR WHITE SPACES



				elif c == (len(temp_r)-1):
					tempBegin = char - c
			#End for loop looking for beginning
			

			#We push the result in sentences
			key= str(tempBegin) + " " + str(tempEnds)
			dico[chapter]["sentences"][key] =dico[chapter]["fulltext"][tempBegin:tempEnds]

		#End of Word found loop

	#End of Chapter loop

		
	return dico

