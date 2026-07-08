class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = 0
        hset = defaultdict(set)
        vset = defaultdict(set) 
        box = defaultdict(set)
        while h<9:
            v = 0
            while v<9:
                if board[h][v].isdigit():
                    if board[h][v] not in hset[h]:
                        hset[h].add(board[h][v])
                    else :
                        print(1)
                        return False

                    if board[h][v] not in vset[v]:
                        vset[v].add(board[h][v])
                    else :
                        print(2) 
                        return False

                    if board[h][v] not in box[(h//3,v//3)]:
                        box[(h//3,v//3)].add(board[h][v])
                    else:
                        print(3) 
                        return False
                v += 1
            h += 1
        return True
        

