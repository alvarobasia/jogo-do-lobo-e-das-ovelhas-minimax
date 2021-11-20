def print_board(sheeps_positions=[[0, 1], [0, 3], [0, 5], [0, 7]], wolf_position=[7, 4]):
    print("   0   1   2   3   4   5   6   7  ")
    print(" |===|===|===|===|===|===|===|===|")
    for i in range(0, 8):
        print(f"{i}", end="")
        for j in range(0, 8):
            print("|", end="")
            if i == wolf_position[0] and j == wolf_position[1]:
                print("🐺 ", end="")
                continue
            has_sheep = False
            for sheep in sheeps_positions:
                if i == sheep[0] and j == sheep[1]:
                    print("🐑 ", end="")
                    has_sheep = True
            has_indicator = False
            if not has_sheep:
                print("   ", end="")
        print("|")
        print(" |===|===|===|===|===|===|===|===|")
