def main():
    rock_bonus = 1
    paper_bonus = 2
    scisors_bonus = 3
    loss_amount = 0
    draw_amount = 3
    win_amount = 6

    filename = "input.txt"
    total_score: int = 0
    with open(filename, 'r+') as file:
        for line in file.readlines():
            line = line.replace('\n', '')
            opponent_choice = line.split(' ')[0]
            outcome_type = line.split(' ')[1]

            if opponent_choice == "A":
                if outcome_type == "X":
                    total_score += scisors_bonus
                    total_score += loss_amount
                elif outcome_type == "Y":
                    total_score += rock_bonus
                    total_score += draw_amount
                elif outcome_type == "Z":
                    total_score += paper_bonus
                    total_score += win_amount
            elif opponent_choice == "B":
                if outcome_type == "X":
                    total_score += rock_bonus
                    total_score += loss_amount
                elif outcome_type == "Y":
                    total_score += paper_bonus
                    total_score += draw_amount
                elif outcome_type == "Z":
                    total_score += scisors_bonus
                    total_score += win_amount
            elif opponent_choice == "C":
                if outcome_type == "X":
                    total_score += paper_bonus
                    total_score += loss_amount
                elif outcome_type == "Y":
                    total_score += scisors_bonus
                    total_score += draw_amount
                elif outcome_type == "Z":
                    total_score += rock_bonus
                    total_score += win_amount
            
    print(f"Total score for the rock-paper-scissors competition is {total_score}")

main()