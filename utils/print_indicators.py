def print_indicators(wolf_position):
    indicators = [None, None, None, None]

    indicators[0] = [wolf_position[0] - 1, wolf_position[1] - 1]
    indicators[1] = [wolf_position[0] - 1, wolf_position[1] + 1]
    indicators[2] = [wolf_position[0] + 1, wolf_position[1] - 1]
    indicators[3] = [wolf_position[0] + 1, wolf_position[1] + 1]

    if wolf_position[0] == 0:
        indicators[0] = None
        indicators[1] = None
    if wolf_position[0] == 7:
        indicators[2] = None
        indicators[3] = None
    if wolf_position[1] == 0:
        indicators[0] = None
        indicators[3] = None
    if wolf_position[1] == 7:
        indicators[1] = None
        indicators[3] = None
    return indicators
