from q4 import SnakesAndLadders

# Test case 1: No snakes or ladders, path exists from 1 to n^2
n = 10
snakes = []
ladders = []
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Path exists:", game.path_exists())  # Output: True

# Test case 2: No snakes or ladders, no path exists from 1 to n^2
n = 10
snakes = []
ladders = []
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Path exists:", game.path_exists())  # Output: False

# Test case 3: Snakes and ladders share start or end positions
n = 10
snakes = [(99, 78), (97, 56), (9, 31)]
ladders = [(78, 99), (9, 31)]
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Snakes and ladders share start or end positions:", game.snakes_ladders_share_start_end())  # Output: True

# Test case 4: No snakes or ladders, no loops exist
n = 10
snakes = []
ladders = []
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Loops exist:", game.loops_exist())  # Output: False

# Test case 5: Snakes and ladders create loops
n = 10
snakes = [(99, 78), (78, 99)]
ladders = [(9, 31), (31, 9)]
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Loops exist:", game.loops_exist())  # Output: True

# Test case 6: Ladder directly from 1 to n^2
n = 10
snakes = [(99, 78), (97, 56)]
ladders = [(1, n**2)]
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Ladder from start to end:", game.ladder_from_start_to_end())  # Output: True

# Test case 7: No ladder directly from 1 to n^2
n = 10
snakes = [(99, 78), (97, 56)]
ladders = [(9, 31)]
game = SnakesAndLadders(n, snakes, ladders)
print("Game:", game)
print("Ladder from start to end:", game.ladder_from_start_to_end())  # Output: False
