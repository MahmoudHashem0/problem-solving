class Solution:
    def findWords(self, board, words):
        self.board = board
        self.d = 1 # direction of searcing in row
        
        word = words[0]
        words_found = []
        i, j = 0, 0
        while i < len(board):
            if word[0] == board[i][j]:
                if self.findWord_right(word, i, j): words_found.append(word)
                elif self.findWord_left(word, i, j): words_found.append(word)
                elif self.findWord_down(word, i, j): words_found.append(word)
                elif self.findWord_up(word, i, j): words_found.append(word)
            j +=self.d
            if j == len(board[0]) or j == -1:
                self.d = -1 * self.d
                j +=self.d
                i+=1


    def findWord_right(self, word, i, j):
        while word[0] == self.board[i][j]:
            word = word[1:]
            if not word:
                break
            j+=1
            w = word[0]; c = self.board[i][j]
        else:
            return False

        return True

    def findWord_left(self, word, i, j):
        while word[0] == self.board[i][j]:
            word = word[1:]
            if not word:
                break
            j-=1
            w = word[0]; c = self.board[i][j]
        else:
            return False

        return True

    def findWord_down(self, word, i, j):
        while word[0] == self.board[i][j]:
            word = word[1:]
            if not word:
                break
            i+=1
            w = word[0]; c = self.board[i][j]
        else:
            return False

        return True

    def findWord_up(self, word, i, j):
        while word[0] == self.board[i][j]:
            word = word[1:]
            if not word:
                break
            i-=1
            w = word[0]; c = self.board[i][j]
        else:
            return False

        return True



words = ["oath","pea","eat","rain"]
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]

op = Solution()
op.findWords(board, words)
