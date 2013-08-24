#!/usr/bin/env/ python
def getChapter(text):

	dictionary = {}
	Chapters = text.split('CHAPTER')

	for chapter in Chapters:
		#print(chapter)
		for i in range(len(chapter)):

			if (chapter[i: i + 1]=="\n"):

				title = chapter[:i-1]
				text_chapter = chapter[i+2:]
				dictionary[title]={"fulltext":text_chapter}
				break

	return(dictionary)