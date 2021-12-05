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

## Recursive Solution

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
