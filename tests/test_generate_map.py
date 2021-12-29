from run import EASY, MEDIUM, HARD, mines_dict, generate_map


def calculate_mines(map):
    return 0


def test_if_hard_map_is_correct():
    matrix = generate_map(HARD)
    assert calculate_mines(matrix) == mines_dict.get(HARD)