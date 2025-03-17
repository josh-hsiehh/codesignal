def solution(matrix):
    if not matrix: 
        return 0
    rows, cols = len(matrix), len(matrix[0])
    max_length = 0

    # Possible diagonal directions: ↘, ↙, ↖, ↗
    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]

    def get_pattern_value(step):
        """ Returns expected value at a given step in the pattern. """
        return 1 if step == 0 else (2 if step % 2 == 1 else 0)

    def check_diagonal(r, c, dr, dc):
        """ Checks the longest valid diagonal sequence from (r, c) in direction (dr, dc). """
        length = 0
        x, y = r, c
        step = 0  # Tracks position in the repeating pattern

        while 0 <= x < rows and 0 <= y < cols and matrix[x][y] == get_pattern_value(step):
            length += 1
            x += dr
            y += dc
            step += 1

        # Check if the sequence terminated at the border
        if not (0 <= x < rows and 0 <= y < cols):
            return length  # Valid sequence reaching the border
        return 0  # Invalid sequence (did not reach the border)

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:  # Start only from 1
                for dr, dc in directions:
                    max_length = max(max_length, check_diagonal(r, c, dr, dc))

    return max_length
