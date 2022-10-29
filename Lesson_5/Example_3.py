# Создайте программу для игры в ""Крестики-нолики"".

matrix = [[None, None, None], [None, None, None], [None, None, None]]
available = True
while available:
    # Крестик - латинская буква X, нолик - латинская буква O 
    # Ходы принимаются в формате [0][0] = "X" или [2][1] = "О"
    turn = input()
    exec('matrix' + turn)
    for row in matrix:
        print(row)
    
    reference_matrix = [
        matrix[0],
        matrix[1],
        matrix[2],
        [i[0] for i in matrix],
        [i[1] for i in matrix],
        [i[2] for i in matrix],
        [matrix[0][0], matrix[1][1], matrix[2][2]],
        [matrix[0][2], matrix[1][1], matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            available = False
            break