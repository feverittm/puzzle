import random
#random.seed(10)

puzzle = [  0,
           1,1,
          1,1,1,
         1,1,1,1,
        1,1,1,1,1]

moves = [ (0, 3, 1),
        (0, 5, 2),
        (1, 6, 3),
        (1, 8, 4),
        (2, 9, 5),
        (2, 7, 4),
        (3, 0, 1),
        (3, 10, 6),
        (3, 12, 7),
        (4, 11, 7),
        (4, 13, 8),
        (5, 0, 2),
        (5, 12, 8),
        (5, 14, 9),
        (6, 1, 3),
        (6, 8, 7),
        (7, 2, 4),
        (7, 9, 8),
        (8, 1, 4),
        (8, 6, 7),
        (9, 2, 5),
        (9, 7, 8),
        (10, 3, 6),
        (10, 12, 11),
        (11, 4, 7),
        (11, 13, 12),
        (12, 3, 7),
        (12, 10, 11),
        (12, 5, 8),
        (12, 14, 13),
        (13, 4, 8),
        (13, 11, 12),
        (14, 5, 9),
        (14, 12, 13)
    ]

solution = []

"""
initialize the puzzle with the open spot at the top of the puzzle
"""
def init_puzzle():
    puzzle[::] = [
            0,
           1,1,
          1,1,1,
         1,1,1,1,
        1,1,1,1,1]

"""
print out the puzzle list formatted more like how the game looks.
"""
def print_puzzle():
    print("puzzle =",puzzle)
    print("     ",puzzle[0])
    print("    ", puzzle[1], puzzle[2])
    print("   ", puzzle[3], puzzle[4], puzzle[5])
    print("  ", puzzle[6], puzzle[7], puzzle[8], puzzle[9])
    print(" ", puzzle[10], puzzle[11], puzzle[12], puzzle[13], puzzle[14])

""" check if the puzzle has been solved; precisely if there are only
def solved():  if there is only one peg left.
"""
def solved():
    return sum(puzzle) == 1

"""create a list of valid moves in the form of simple tuples that define
the start and then end of the valid move.  If this list is empty then
there are no more valid moves.
"""
valid = []
def addmove(v):
    a = v[0]
    b = v[1]
    c = v[2]
    t = tuple()
    if puzzle[a] == 1 and puzzle[b] == 0 and puzzle[c] == 1:
        t = a,b,c
        valid.append(t)

def valid_moves():
    # first set should be [(3,0,1),(5,0,2)]
    del valid[::]
    for t in moves:
        addmove(t)
    return valid

"""
choose which move we want to use for this round
"""
def domove(t):
    solution.append(t)
    a = t[0]
    b = t[1]
    c = t[2]
    puzzle[a] = 0 # start node of move
    puzzle[b] = 1 # end node of move
    puzzle[c] = 0 # intermediate node
    
def choose_move():
    #print ("Moves: ", valid)
    l=len(valid)-1
    s=random.randint(0,l)
    #print ("Length: ",l,", Selector: ",s)
    move = valid[s]
    #print ("Move ",move)
    if (puzzle[move[0]] == 1 or puzzle[move[1]] == 0 or puzzle[move[2]] == 1):
        domove(move)     
        return True
    print("Bad Move Specified", move)
    print("   ", move[0], " = ", puzzle[move[0]])
    print("   ",move[1], " = ", puzzle[move[1]])
    print("   ",move[2], " = ", puzzle[move[2]])
    return False

def run_puzzle():
    init_puzzle()
    del solution[::]
    #print_puzzle()
    #print ("Solved? ", solved())
    loops = 0
    while valid_moves():
        loops = loops + 1
        #print ("Loop: ", loops)
        choose_move()
        if solved():
            print ("Puzzle solved in ",len(solution),"moves!")
            print ("Solution: ", solution)
            print_puzzle()
            break
        if loops > 20:
            print ("Solver Loops Exceeded")
            break
        #print_puzzle()

    if not solved():
        print ("Puzzle not solved in ",loops, " loops and no valid moves left.")
        print (sum(puzzle)," Pegs left on the puzzle.")
        print_puzzle()
    return sum(puzzle)

#####################################################################
#  Start solver...
#####################################################################
init_puzzle()
main_loop = 1
solution = []
while run_puzzle() > 1 and main_loop < 50:
    print ("Trial #", main_loop)
    main_loop = main_loop+1