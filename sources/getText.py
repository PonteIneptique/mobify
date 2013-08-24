#!/usr/bin/env/ python
def getText(src):
	f = open(src)

	text = f.read()
	f.close()

	return text
