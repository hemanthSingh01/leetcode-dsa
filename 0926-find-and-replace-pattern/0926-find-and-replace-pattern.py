class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def isomorphic(word,patt):
            if len(word)!=len(patt):
                return False
            d1={}
            d2={}
            for w,p in zip(word,patt):
                if w in d1:
                    if d1[w]!=p:
                        return False
                else:
                    d1[w]=p
                if p in d2:
                    if d2[p]!=w:
                        return False
                else:
                    d2[p]=w
            return True
        res=[]
        for i in range(len(words)):
            if isomorphic(words[i],pattern):
                res.append(words[i])
        return res