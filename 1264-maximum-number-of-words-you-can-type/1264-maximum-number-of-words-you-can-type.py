class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split()
        bl=set(brokenLetters)
        count=0
        for word in words:
            for j in word:
                if j in bl:
                    count+=1
                    break
        return len(words)-count
                    