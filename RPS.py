# RPS.py
import random

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default move if no history yet
    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    # Look at the opponent’s last 3 moves
    last_three = opponent_history[-3:]
    prediction = max(["R", "P", "S"], key=last_three.count)

    # Play the counter move
    if prediction == "R":
        return "P"
    elif prediction == "P":
        return "S"
    else:
        return "R"
