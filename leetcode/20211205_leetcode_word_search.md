# Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

Constraints:

* m == board.length
* n = board[i].length
* 1 <= m, n <= 6
* 1 <= word.length <= 15
* board and word consists of only lowercase and uppercase English letters.

## DFS Solution
Excerpted from LC created by OldCodingFarmer
```python
def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res
```

## Recursive Solution
This doesn't account for every direction at a given point. For instance, it only follows left, right, up, down sequence in that if right and up is found to be the match, then only the sequential possibilities invoked by visiting right will be observed.

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        linear search to find a seed then search through its adjacent item
        1. linear search first or last letter of the key
        2. search adj item (top, bottom, left, right)
            a. no boundary
            b. no visited cell
        3. make sure when 1st letter found move fwd and bwd if last found
        TC:O(M*N)
        '''        
        def searching(board, inner_cnt, visited, match):
            while match:
                moved = False
                
                #left (inner_n - 1 >= 0)
                inner_m, inner_n = inner_cnt // n, inner_cnt % n
                if inner_n - 1 >= 0 and inner_cnt - 1 not in visited and match:
                    if board[inner_m][inner_n-1] == match[0]:
                        inner_cnt -= 1
                        visited.append(inner_cnt)
                        match = match[1:] 
                        moved = True

                inner_m, inner_n = inner_cnt // n, inner_cnt % n
                #right (inner_n + 1 <= n)
                if inner_n + 1 < n and inner_cnt + 1 not in visited and match:
                    if board[inner_m][inner_n+1] == match[0]:
                        inner_cnt += 1
                        visited.append(inner_cnt)
                        match = match[1:]                                
                        moved = True
                        
                #up (inner_m - 1 >= 0)
                inner_m, inner_n = inner_cnt // n, inner_cnt % n
                if inner_m - 1 >= 0 and inner_cnt - n not in visited and match:
                    print(visited, match)
                    if board[inner_m-1][inner_n] == match[0]:
                        inner_cnt -= n
                        visited.append(inner_cnt)
                        match = match[1:]
                        moved = True

                #down (inner_m + 1 <= m)
                inner_m, inner_n = inner_cnt // n, inner_cnt % n
                if inner_m + 1 < m and inner_cnt + n not in visited and match:
                    if board[inner_m+1][inner_n] == match[0]:
                        inner_cnt += n
                        visited.append(inner_cnt)
                        match = match[1:]                         
                        moved = True
                
                if moved:
                    return searching(board, inner_cnt, visited, match)
                else: #if conditions not met, exit loop
                    break
                                
            if match == []:
                return True
            else:
                return False
                
        visited = []
        fwd = word
        bwd = word[::-1]
        cnt = -1 #counter to replace coordindate
        m, n = len(board), len(board[0])

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                cnt += 1

                if c == fwd[0] or c == bwd[0]:                    
                    inner_cnt = cnt
                    visited = [cnt]
                    match = list(fwd[1:]) if c == fwd[0] else list(bwd[1:])
                    
                    result = searching(board, inner_cnt, visited, match)

                    if result:
                        return True
        
        #if not found, return False
        return False
```
