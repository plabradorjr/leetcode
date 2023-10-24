class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = []
        formattedList = []
        
        wordList = s.split(" ")
        for y in wordList:
            if y.strip() == "":
                continue
            formattedList.append(y.strip())
        formattedList.reverse()
     
        return " ".join(formattedList)
