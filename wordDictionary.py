class WordDictionary:

    def __init__(self):
        self.size = 3676
        self.storage = [0]*self.size
        

    def addWord(self, word: str) -> None:
        h = 0
        for i, c in enumerate(word):
            h = h+ ord(c) +i
        if self.storage[h] == 0:
            self.storage[h] = set()
        self.storage[h].add(word)

    def search(self, word: str) -> bool:
        h = 0
        like = 0
        for i, c in enumerate(word):
            if c == '.':
                h+=i
                like+=1
            else:
                h= h + ord(c) + i
        try:
            if not like and word in self.storage[h]: return True
        except TypeError: return False

        if not like: return False
        else:
            likeswords = set()
            start = h+like*ord('a')
            end = h+like*ord('z')+1
            likestorage = self.storage[start :  end: ]
            for ele in likestorage:
                if ele:
                    likeswords|=ele
        
        found = False
        for w in likeswords:
            if len(w) == len(word):
                pos =0
                splits = word.split('.')
                found = True
                for splt in splits:
                #     print(f"splt: {splt}, pos: {pos},  len(splt)+pos: {len(splt)+pos}")
                    if splt != w[pos:len(splt)+pos]:
                        found = False
                    pos = pos + len(splt)+1
                if found:
                    return True
        return found

        
        # return False





        #     pass
            


        # start = h+like*ord('a')
        # end = h+like*ord('z')+1
        # found = sum(self.storage[start :  end: ])
        # return found !=0



obj = WordDictionary()
addwords = [["bad"],["dad"],["mad"]]
for word in addwords:
    obj.addWord(word[0])
serchwords = [["pad"],["bad"],[".ad"],[".b."]]
for word in serchwords:
    result = obj.search(word[0])
    print(result)