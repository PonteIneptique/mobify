#!/usr/bin/env/ python

def getSortedStats(globalStats):
	i = 0
	for sort in sorted(globalStats, key = globalStats.get, reverse=True):
		print str(sort) + " - " + str(globalStats[sort])
		i += 1
		if i == 40:
			break