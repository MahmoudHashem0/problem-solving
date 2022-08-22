class Solution:
    def find1(word: str, s: str) -> bool:
        len_w = len(word)
        dic = {}
        indexes = []
        update = True
        for i, c in enumerate(s):
            if c == word[0]:
                idx = i if update else idx
                dic[idx] = dic.get(idx, 0) + 1
                update = False
            else:
                update = True

        for idx, length in dic.items():
            n = length//len_w
            for i in range(length%len_w+1):
                start = idx
                for _ in range(n):
                    indexes.append((start+i, start+len_w-1+i))
                    start+=len_w
        return indexes

    def find2(word: str, s:str) -> bool:
        i=-1
        start = 0
        indexes = []
        while True:
            i+=1
            idx = s.find(word,start,len(s))
            if idx == -1:
                return indexes
            indexes.append((idx, idx + len(word)-1))
            start = idx + len(word)

    def find_word_boundry(word: str, s: str) -> bool:
        if word == len(word)*word[0]:
            return Solution.find1(word, s)
        else:
            return Solution.find2(word, s)
    def find_word_boundry2(word: str, s: str) -> bool:
        if not word or not s:
            return []
        len_s = len(s)
        len_word = len(word)
        j=0
        i=0
        indexes = []
        while True :
            if s[j] == word[i]:
                i+=1
                j+=1
            elif i!=0:
                i=0
            else:
                i=0
                j+=1
            if i == len_word:
                idx = j-len_word, j-1
                indexes.append(idx)

                if j + 1 <= len_s:
                    i = 0
                    j = j-len_word +1
                else:
                    return indexes
            elif j == len_s:
                return indexes
        return indexes
    

    def find_pattern(ls, ln_s):
        dic = {}
        for element in ls:
            v = dic.get(element[0],[])
            v.append(element[1])
            dic[element[0]]  = v

        s = 0
        tmp_ls = []
        known_keys = set()
        while s < ln_s:
            
            i=0
            e_ls = dic.get(s,-1)
            ln_tmp_ls = len(tmp_ls)
            if e_ls == -1 or s in known_keys:
                try:
                    tmp_ls[-1][1]+=1
                    e_ls, i = tmp_ls[-1]
                except IndexError:
                    return False
            else:
                tmp_ls.append([e_ls, 0])
            try:
                known_keys.add(s)
                s = e_ls[i] + 1
            except IndexError:
                tmp_ls.pop()
                known_keys.remove(s)


        else:
            return True

    
    def wordBreak(s, wordDict):
        len_s = len(s)
        idxes = []
        for word in wordDict:
            idx =  Solution.find_word_boundry(word, s)
            idxes.extend(idx)
        return Solution.find_pattern(idxes, len_s)


s = "catcatcatcatcatcatcatcatcatcatccc"
wordDict = ["cat","catcatcatccc"]

print(Solution.wordBreak(s, wordDict))