# RPS_game.py
import random

def play(player1, player2, num_games, verbose=False):
    p1 = ""
    p2 = ""
    p1_score = 0
    p2_score = 0
    tie_score = 0

    for _ in range(num_games):
        move1 = player1(p2)
        move2 = player2(p1)

        if move1 == move2:
            tie_score += 1
        elif (move1 == 'R' and move2 == 'S') or \
             (move1 == 'P' and move2 == 'R') or \
             (move1 == 'S' and move2 == 'P'):
            p1_score += 1
        else:
            p2_score += 1

        if verbose:
            print(f"Player 1: {move1}  Player 2: {move2}")

        p1 = move1
        p2 = move2

    print(f"Final results after {num_games} games:")
    print(f"Player 1 wins: {p1_score}")
    print(f"Player 2 wins: {p2_score}")
    print(f"Ties: {tie_score}")


def quincy(prev_play, counter=[0]):
    moves = ['R', 'R', 'P', 'P', 'S', 'S']
    response = moves[counter[0] % len(moves)]
    counter[0] += 1
    return response


def mrugesh(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    last_ten = opponent_history[-10:]

    most_common = max(
        ['R', 'P', 'S'],
        key=lambda x: last_ten.count(x)
    )

    if most_common == 'R':
        return 'P'
    if most_common == 'P':
        return 'S'
    return 'R'


def abbey(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    if len(opponent_history) < 5:
        guess = random.choice(['R', 'P', 'S'])
    else:
        guess = opponent_history[-5]
    return guess


def kris(prev_play, opponent_history=[]):
    if prev_play == "":
        return random.choice(['R', 'P', 'S'])
    else:
        if prev_play == 'R':
            return 'P'
        if prev_play == 'P':
            return 'S'
        if prev_play == 'S':
            return 'R'
