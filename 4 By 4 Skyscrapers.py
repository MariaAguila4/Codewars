import numpy as np
def solve_puzzle (clues):
    print("clues:",clues,"Len:", len(clues))
    board =  [0, 0, 0, 0 ,
              0, 0, 0, 0 ,
              0, 0, 0, 0 ,
              0, 0, 0, 0  ]

    clues1 = clues[0:4]
    clues2 = clues[4:8]
    clues3 = clues[8:12]
    clues4 = clues[12:16]
    print(clues1, clues2, clues3, clues4)
    
    return board

clues = (
( 2, 2, 1, 3,
  2, 2, 3, 1,
  1, 2, 2, 3,
  3, 2, 1, 3 ),
( 0, 0, 1, 2,
  0, 2, 0, 0,
  0, 3, 0, 0,
  0, 1, 0, 0 )
)

outcomes = (
( ( 1, 3, 4, 2 ),
  ( 4, 2, 1, 3 ),
  ( 3, 4, 2, 1 ),
  ( 2, 1, 3, 4 ) ),
( ( 2, 1, 4, 3 ),
  ( 3, 4, 1, 2 ),
  ( 4, 2, 3, 1 ),
  ( 1, 3, 2, 4 ) )
)

print(solve_puzzle (clues[0]))