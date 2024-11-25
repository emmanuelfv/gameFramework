"""
Solver for 15 puzzle.
The game consist in 4*4 grid with numbers from 1 to 15 randombly placed in the initial state and one empty cell. 
By moving the place of the empty cell we should be able to sort the numbers. e.g.:

Initial state:
NA  1  2  3
 5  6  7  4
 9 10 11  8
13 14 15 12

Final state:
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 NA

The purpose of this agent is to generate the minimun number of movements needed to solve the puzzle.
By change the state to have a pointer to the previos step we will be able to track the hore route.

Using this approach the problem complexity is: (heigth * width)!
"""

class puzzle_15:
    def dfs_solver(self, board) -> int:
        board2 = [list(map(str, row)) for row in board]
        heigth, width = len(board), len(board[0])
        def make_str(M) -> str:
            return ";".join([ "".join(row) for row in M ])

        def make_mat(s) -> list:
            return [ list(row) for row in s.split(";") ]

        def validate(M) -> bool:
            return all( val == (x+1)%(heigth * width) for x, val in 
                       enumerate(int(val) for row in m for val in row))

        def swap(M, zero, chg) -> list:
            new = zero[0] + chg[0], zero[1] + chg[1]
            if new[0] == -1 or new[0] == heigth or new[1] == -1 or new[1] == width:
                return None
            M2 = [ [i for i in row] for row in M ]
            M2[new[0]][new[1]], M2[zero[0]][zero[1]] = M2[zero[0]][zero[1]], M2[new[0]][new[1]]
            return M2

        def find_zero(M) -> tuple:
            for i in range(heigth):
                for j in range(width):
                    if M[i][j] == "0":
                        return (i,j)                    

        def expand(M, explored, new_set) -> None:
            zero = find_zero(M)
            for chg in swap_list:
                M2 = swap(M, zero, chg)
                if not M2:
                    continue
                s2 = make_str(M2)
                if s2 not in explored and s2 not in new_set and s2 not in to_explore:
                    new_set.add(s2)

        
        swap_list = [(0,1),(0,-1),(1,0),(-1,0)]
        explored = set()
        to_explore = {make_str(board2)}

        count = 0
        while True:
            new_set = set()
            while to_explore:
                s = to_explore.pop()
                m = make_mat(s)
                if validate(m):
                    return count
                explored.add(s)            
                expand(m, explored, new_set)
            if not new_set:
                return -1
            count += 1
            to_explore = new_set


test_list = [
    [[1,2,3],[4,5,6],[7,8,0]],
    [[1,2,3],[4,5,6],[7,0,8]],
    [[1,2,3],[4,5,6],[8,7,0]],
    [[0,1,2],[4,5,3],[7,8,6]],
]

result_list = [
    0,1,-1,4
]

if __name__ == "__main__":
    solver = puzzle_15()
    for test in test_list:
        print(test)
        print("number of movements to solve it:", solver.dfs_solver(test))

