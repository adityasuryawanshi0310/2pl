def is_safe(board, row, col, n):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens_backtracking(board, row, n):
    if row == n:
        print_board(board, n)
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            if solve_n_queens_backtracking(board, row + 1, n):
                return True
            board[row] = -1
    return False

def print_board(board, n):
    for i in range(n):
        row = ['Q' if board[i] == j else '.' for j in range(n)]
        print(" ".join(row))
    print("\n")
    
def n_queens_backtracking(n):
    board = [-1] * n
    if not solve_n_queens_backtracking(board, 0, n):
        print("Solution does not exist.")


def is_safe1(board , row , col , n):
    for i in range(row):
        if board[i] == col or board[i]-i == col- row or board[i]+i == col+row:
            return False
    return True
    
def backtrack(board , row , n):
    if row == n:
        print_b(board ,n)
        return True
    for col in range(n):
        if is_safe1(board , row , col , n ):
            board[row] = col
            if backtrack(board , row+1 , n):
                return True
            board[row] = -1
    return False

def print_b(board , n):
    for i in range(n):
        row = ('Q' if board[i]==j else '.' for j in range(n))
        print(" ".join(row))
    print("\n")
def n_queen(n):
    board = [-1]*n
    if not backtrack(board , 0 , n):
        print("not possible")        

n = int(input("enter = "))

n_queen(n)

class Node:
    def __init__(self, level, board):
        self.level = level
        self.board = board

def is_safe_branch(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def bound(node, n):
    # The branch and bound function checks how many possibilities are left.
    # It ensures the node is still feasible (not pruned).
    row = node.level
    for col in range(n):
        if is_safe_branch(node.board, row, col):
            return True
    return False

def branch_and_bound_n_queens(n):
    root = Node(0, [-1] * n)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.level == n:
            print_board(node.board, n)
            return True
        
        for col in range(n):
            if is_safe_branch(node.board, node.level, col):
                new_board = node.board[:]
                new_board[node.level] = col
                new_node = Node(node.level + 1, new_board)
                
                if bound(new_node, n):
                    queue.append(new_node)
    print("Solution does not exist.")
    return False
    


