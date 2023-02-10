import numpy as np


default_reber_grammar = [
    [("B", 1)],
    [("T", 2), ("P", 3)],
    [("S", 2), ("X", 4)],
    [("T", 3), ("V", 5)],
    [("X", 3), ("S", 6)],
    [("P", 4), ("V", 6)],
    [("E", None)]]


def generate_string() -> str:
    state = 0
    output = []

    while state is not None:
        index = np.random.randint(len(default_reber_grammar[state]))
        char, state = default_reber_grammar[state][index]
        output.append(char)

    return ''.join(output)


def generate() -> set[str]:
    lines = []

    while len(set(lines)) < 2000:
        lines.append(generate_string())

    return set(lines)


if __name__ == '__main__':
    lines = generate()

    with open('proper_reber.txt', 'w') as f:
        for line in lines:
            f.write(f'{line}\n')
