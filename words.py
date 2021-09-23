def countWord(str, word):
    wordList = str.split()
    
    ans = 0
    for xWord in wordList:
        if xWord == word:
            ans+=1
    return ans

pp = "Hola cómo andas, yo muy bien bro. Mi mamá tmb está bien"

print(countWord(pp, "bien"))


