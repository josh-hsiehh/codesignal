def solution(lamps, points):
    # Create an event list to track the number of lamps covering each point
    events = []
    
    # Add lamp start and end points to events
    for start, end in lamps:
        events.append((start, 1))  # Lamp starts illuminating
        events.append((end + 1, -1))  # Lamp stops illuminating after 'end'
    
    # Sort events by position, breaking ties by type (-1 should come before +1 to maintain correctness)
    events.sort()

    # Process points and determine illumination
    result = []
    active_lamps = 0
    event_index = 0
    num_events = len(events)
    
    # Sort points with original indices to maintain order
    sorted_points = sorted(enumerate(points), key=lambda x: x[1])
    
    for index, point in sorted_points:
        # Process all events that are <= current point
        while event_index < num_events and events[event_index][0] <= point:
            active_lamps += events[event_index][1]
            event_index += 1
        result.append((index, active_lamps))  # Store result with original index
    
    # Restore original order
    result.sort()
    return [count for _, count in result]
