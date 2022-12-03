import enum

class RoundOutcome(enum.Enum):
    LOSE = 0
    DRAW = 1
    WIN  = 2

ROUND_OUTCOME_SCORE = {
    RoundOutcome.LOSE: 0,
    RoundOutcome.DRAW: 3,
    RoundOutcome.WIN: 6
}

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def round_outcode(round):
    if round in ['A Z', 'B X', 'C Y']:
        print(f"lose: {round}")
        return RoundOutcome.LOSE
    elif round in ['A Y', 'B Z', 'C X']:
        print(f"win: {round}")
        return RoundOutcome.WIN
    else:
        print(f"draw: {round}")
        return RoundOutcome.DRAW

rounds = open("./a.input", "r").readlines()

total_score = 0

for round in rounds:
    round = round.strip()
    my_move = round.split(" ")[1]
    outcome = round_outcode(round)

    total_score += ROUND_OUTCOME_SCORE[outcome]
    total_score += SHAPE_SCORE[my_move]

print(total_score)