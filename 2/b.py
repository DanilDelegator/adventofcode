import enum

"""
X -> Need to lose
Y -> Need to draw
Z -> Need to win
"""

ROUND_OUTCOME_SCORE = {
    'Z': 6,
    'Y': 3,
    'X': 0
}

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

MY_MOVE = {
    'X': { # lose
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    },
    'Y': { # draw
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    },
    'Z': { # win
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
}

rounds = open("./b.input", "r").readlines()

total_score = 0

for round in rounds:
    round = round.strip()
    their_move, outcome = round.split(" ")
    my_move = MY_MOVE[outcome][their_move]

    print(round, ROUND_OUTCOME_SCORE[outcome], SHAPE_SCORE[my_move])

    total_score += ROUND_OUTCOME_SCORE[outcome]
    total_score += SHAPE_SCORE[my_move]

print(total_score)