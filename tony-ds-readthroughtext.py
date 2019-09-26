alice_file = open("alice.txt") #import alice.txt from internet as txt file

words_count = {}

for line in alice_file:
	words = line.split()
	for word in words :
		if words_count.get(word) == None:
			words_count[word] = 1
		else:
			words_count[word] += 1

alice_tbl = Table().with_column('word',make_array(*list(words_count)))


#NOT COMPLETE - reffer slack channel posting!
