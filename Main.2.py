def match_words(words):
   ctr=0
   lst=[ ]
   for word in words:
    if len(word) > 1 and word[0] == word[-1]:
       ctr+= 1
       lst.append(word)
    print("List of words with the first and the last character\n",lst)
    return ctr

count=match_words(['abc','cfc','xyz','aba','1212'])
print("Numbers of words having first and last character same:",count)