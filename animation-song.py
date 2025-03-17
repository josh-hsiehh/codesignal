def solution(songs, animations):
    result = []  # List to store the final matched animations for each song

    # Create a dictionary to store animation lengths for quick lookup
    # Format: {animation_name: animation_length}
    animation_map = {}
    for animation in animations:
        name, length = animation.split(":")  # Split animation into name and length
        animation_map[name] = int(length)  # Convert length to an integer

    # Process each song in the input list
    for song in songs:
        song_name, song_length = song.split(":")  # Split song into name and length
        song_length = int(song_length)  # Convert length to an integer

        best_animation = None  # Variable to store the best animation for the current song
        min_index = float("inf")  # Track the lowest index of a valid animation

        # Iterate over the animations to find the best match
        for i, animation in enumerate(animations):
            anim_name, anim_length = animation.split(":")  # Split animation into name and length
            anim_length = int(anim_length)  # Convert length to an integer

            # Check if the animation length is a valid divisor of the song length
            if song_length % anim_length == 0:
                times_to_play = song_length // anim_length  # Calculate how many times the animation needs to play

                # Choose the first (lowest index) valid animation
                if i < min_index:
                    best_animation = f"{anim_name}:{times_to_play}"  # Store the animation name and repeat count
                    min_index = i  # Update the lowest index found

        # Append the best found animation to the result list
        result.append(best_animation)

    return result  # Return the list of best animations for each song
