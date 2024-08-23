from q4 import SnakesAndLadders

def run_test_case(test_case_name, n, snakes, ladders, expected_output):
	game = SnakesAndLadders(n, snakes, ladders)
	print("Test case:", test_case_name)
	print("Game:", game)
	print("Expected output:", expected_output)
	print("Actual output:", game.path_exists())
	print("Result:", "Pass" if game.path_exists() == expected_output else "Fail")
	print()

# Test case 1: No snakes or ladders, path exists from 1 to n^2
n = 10
snakes = []
ladders = []
expected_output = True
run_test_case("Test case 1", n, snakes, ladders, expected_output)

# Test case 2: No snakes or ladders, no path exists from 1 to n^2
n = 10
snakes = []
ladders = []
expected_output = False
run_test_case("Test case 2", n, snakes, ladders, expected_output)

# Test case 3: Snakes and ladders share start or end positions
n = 10
snakes = [(10, 7), (9, 5), (3, 8)]
ladders = [(7, 10), (3, 8)]
expected_output = True
run_test_case("Test case 3", n, snakes, ladders, expected_output)

# Test case 4: No snakes or ladders, no loops exist
n = 10
snakes = []
ladders = []
expected_output = False
run_test_case("Test case 4", n, snakes, ladders, expected_output)

# Test case 5: Snakes and ladders create loops
n = 10
snakes = [(10, 7), (7, 10)]
ladders = [(3, 8), (8, 3)]
expected_output = True
run_test_case("Test case 5", n, snakes, ladders, expected_output)

# Test case 6: Ladder directly from 1 to n^2
n = 10
snakes = [(10, 7), (9, 5)]
ladders = [(1, n**2)]
expected_output = True
run_test_case("Test case 6", n, snakes, ladders, expected_output)

# Test case 7: No ladder directly from 1 to n^2
n = 10
snakes = [(10, 7), (9, 5)]
ladders = [(3, 8)]
expected_output = False
run_test_case("Test case 7", n, snakes, ladders, expected_output)
