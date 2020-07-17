words= "Why sometimes I have beleived as many as six impossible things before breakfast".split()

lengths = []
for word in words:
    lengths.append(len(word))

lengths = [len(word) for word in words]
