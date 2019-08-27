import glob
import re
from collections import defaultdict, OrderedDict
import operator

posts = glob.glob("_posts/*.md")
tagExpr = re.compile("tags: (.*)$")

# Get distinct tags
tags = []
for post in posts:
	with open(post) as file:
		for line in file:
			match = tagExpr.search(line)
			if match:
				tags.extend(match.group(1).split(" "))

tagsDict = defaultdict(int) # Neat dictionary that adds a member if not present
for tag in tags:
	tagsDict[tag] += 1

# Sort on values
tagsDict = OrderedDict(sorted(tagsDict.items(), key=operator.itemgetter(1), reverse=True))

for tag in tagsDict:
	print(str(tagsDict[tag]) + " - " + tag)