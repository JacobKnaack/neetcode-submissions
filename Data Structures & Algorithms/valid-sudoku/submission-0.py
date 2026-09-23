class Solution:
    @staticmethod
    def getGrid(n: int, board: List[List[str]]) -> List[str]:
        values = ["."] * 9
        value_index = 0
        x_border = [0,2]
        y_border = [0,2]
        # calculate index border
        if n == 1 or n == 4 or n == 7:
            x_border = [3,5]
        if n == 2 or n == 5 or n == 8:
            x_border = [6,8]
        if n > 2:
            y_border = [3,5]
        if n > 5:
            y_border = [6,8]
    
        # read all values within the x and y border
        for i in range(y_border[0], y_border[1] + 1):
            column = board[i];
            for j in range(x_border[0], x_border[1] + 1):
                row = column[j]
                values[value_index] = row
                value_index += 1
        return values

    @staticmethod
    def getColumn(n: int, board: List[List[str]]) -> List[str]:
        values = []
        if n > 8:
            return values
        for row in board:
            values.append(row[n])
        return values

    @staticmethod
    def getRow(n: int, board: List[List[str]]) -> List[str]:
        if n > 8:
            return []
        values = board[n]
        return values

    @staticmethod
    def areValuesValid(values: List[str]) -> bool:
        found = [] 
        for value in values:
            if value == '.':
                continue
            else:
                num = int(value)
            if num in found:
                return False
            else:
                found.append(num)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 10):
            row = Solution.getRow(i, board)
            column = Solution.getColumn(i, board)
            grid = Solution.getGrid(i, board)
            if Solution.areValuesValid(row) == False or Solution.areValuesValid(column) == False or Solution.areValuesValid(grid) == False:
                return False
            print("i: ", i)
        return True
