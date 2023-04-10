def update_score(station_number, current_score):
    # Validate the input station_number
    if station_number not in [1, 2, 3]:
        print("Invalid station number. Station number must be 1, 2, or 3.")
        return

    # Read the current scores from the file
    with open("highscores.txt", "r") as f:
        scores = f.readlines()
    
    # Update the score for the specified station if the current_score is greater
    station_score = int(scores[station_number - 1].split(":")[1])
    if current_score > station_score:
        scores[station_number - 1] = f"Station {station_number}: {current_score}\n"
        
        # Write the updated scores to the file
        with open("highscores.txt", "w") as f:
            f.writelines(scores)
