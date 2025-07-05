class Solution(object):
    def groupAnagrams(self, strs):
        dici={}
        for i in strs:
            s_w="".join(sorted(i))
            if s_w not in dici:
                dici[s_w]=[]
            dici[s_w].append(i)
        g_a=list(dici.values())
        return g_a