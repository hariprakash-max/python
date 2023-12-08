import random

def play_cricket():
    print("Welcome to the Text-based Cricket Game!")

    # Initialize scores and overs
    player_scores = [0, 0]
    total_overs = 2

    # Game loop
    for current_over in range(1, total_overs + 1):
        print("\n----- Over", current_over, "-----")

        # Batting loop
        for player in range(2):
            print("\nPlayer", player + 1, "Batting:")
            player_score = 0

            for ball in range(6):
                input("Press Enter to bowl...")

                # Simulate a random run for each ball
                runs = random.randint(0, 6)
                print("You scored", runs, "runs!")

                player_score += runs

            print("\nPlayer", player + 1, "Scored", player_score, "runs in this over.")
            player_scores[player] += player_score

        print("\n--- End of Over", current_over, "---")
        print("Player 1 Total Score:", player_scores[0])
        print("Player 2 Total Score:", player_scores[1])

    # Determine the winner
    if player_scores[0] > player_scores[1]:
        print("\nPlayer 1 wins!")
    elif player_scores[0] < player_scores[1]:
        print("\nPlayer 2 wins!")
    else:
        print("\nIt's a tie!")

if __name__ == "__main__":
    play_cricket()

