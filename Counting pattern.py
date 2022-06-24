filename = input("Enter the file name: ")
handle = open(filename, "r+")
counts = dict()
#line = input("Enter a line of text")
for line in handle:
    words = line.split()
    for  word in words:
        counts[word] = counts.get(word, 0) + 1

print("counts: ", counts)
bigcount = None
bigword = None
wordcount = open("word_count.txt", "w")
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
handle.write('\n' + str(counts) + '\n' + str(bigword) + ": " + str(bigcount))
#wordcount.write('\n', counts, '\n', bigword, bigcount)
print(bigword, bigcount)
