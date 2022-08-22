class Solution:
    def groupAnagrams(self, strs: list) -> list:
        self.strs_sorted = []
        strs_dic = {}
        anagrams = []
        for s in strs:
            sorted_s_ls = sorted(s)
            sorted_s = "".join(sorted_s_ls)
            
            if sorted_s in strs_dic.keys():
                idx = strs_dic[sorted_s]
                anagrams[idx].append(s)
            else:
                anagrams.append([])
                anagrams[-1].append(s)
                strs_dic[sorted_s] = len(anagrams)-1
        
        return anagrams
