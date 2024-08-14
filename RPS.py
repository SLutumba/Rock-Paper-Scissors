import random


def main():
    #List of possible moves in game
    moves = ["Rock", "Paper", "Scissors"]
    will_play_again = True
    # prompt user for input
    print("This is a Rock, Paper, Scissors game.\n"
          "You'll be faced off against the CPU, good luck!\n")

    while will_play_again:
        print("Please make your move, type only 'Rock', 'Paper', or 'Scissors'")
        player_move = input().capitalize()

        #ensure user enters a valid move only
        while not is_correct_input(player_move):
            print("Incorrect input. please type only 'Rock', 'Paper', or 'Scissors'")
            player_move = input().capitalize()

        #randomly generate a move for the computer
        cpu_move = moves[random.randint(0, 2)]

        #display the results
        result = return_string_result(player_move, cpu_move)
        print(f"CPU move: {cpu_move}\n"
              f"Your move: {player_move}\n"
              f"{result}")
        print_comments(result)
        print("Do you wish to play again? Type 'y' for yes and any other character to exit:")
        play_again = input().lower()
        will_play_again = restart_game(play_again)


#verifies input and returns value based on validity
def is_correct_input(move) -> bool:
    if move != "Rock" and move != "Paper" and move != "Scissors":
        return False
    return True


#determines then returns a string indicating result
def return_string_result(player_move, cpu_move) -> str:
    cpu_wins = (cpu_move == "Paper" and player_move == "Rock") or (
                cpu_move == "Rock" and player_move == "Scissors") or (cpu_move == "Scissors" and player_move == "Paper")
    if player_move == cpu_move:
        return "Draw"
    elif cpu_wins:
        return "CPU wins"
    else:
        return "Player wins"


#prints comments for the end of each game
def print_comments(result):
    win_comments = [
        "Well played! That was a close one.",
        "Nice move! You really outsmarted your opponent.",
        "That was a perfect strategy, well done!",
        "You got them this time! Great job.",
        "Impressive! You really know how to play.",
        "That was a clever choice! You’re on fire.",
        "Victory! You dominated that round.",
        "Excellent choice! Your strategy paid off.",
        "You outmaneuvered them completely, awesome!",
        "Bravo! You’re on a winning streak."
    ]
    loss_comments = [
        "Ouch, tough luck! Better luck next time.",
        "Oh no, they got you! Try again.",
        "So close, but not quite! Keep practicing.",
        "You were almost there! Don’t give up.",
        "That was a tough one! You’ll get them next time.",
        "Unlucky this time! Stay focused and try again.",
        "It’s all part of the game! Learn and come back stronger.",
        "Don’t worry, every loss is a step towards improvement.",
        "They got the better of you this time, but you’re improving!",
        "Keep your head up! The next round is yours."
    ]
    draw_comments = [
        "It’s a draw! You’re evenly matched.",
        "Great minds think alike! It’s a tie.",
        "No winner this time, it’s a draw!",
        "Both of you played well! It’s a tie.",
        "Stalemate! You’re both in sync.",
        "Even match! Let’s see who wins the next round.",
        "It’s a tie! You both held your ground.",
        "Neither wins, neither loses. It’s a draw!",
        "A draw! You’re on the same wavelength.",
        "Perfectly balanced! It’s a tie."
    ]

    if result == "CPU wins":
        print(f"{loss_comments[random.randint(0, 9)]}")
    elif result == "Draw":
        print(f"{draw_comments[random.randint(0, 9)]}")
    else:
        print(f"{win_comments[random.randint(0, 9)]}")


def restart_game(play_again) -> bool:
    if play_again == 'y':
        return True
    return False


if __name__ == "__main__":
    main()
