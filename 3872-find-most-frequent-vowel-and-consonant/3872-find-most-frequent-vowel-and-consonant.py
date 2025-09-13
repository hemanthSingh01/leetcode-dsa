class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        dici={}
        dicii={}
        for i in s:
            if i in vowels:
                if i not in dici:
                    dici[i]=1
                else:
                    dici[i]+=1
            else:
                if i not in dicii:
                    dicii[i]=1
                else:
                    dicii[i]+=1
        if dici!={} and dicii!={}:
            return max(dici.values())+max(dicii.values())
        if dicii!={} and dici=={}:
            return max(dicii.values())
        if dici!={} and dicii=={}: 
            return max(dici.values())
        
                
            