import random
import os

from reber_grammars.base_grammars.grammar_degenerator import degenerate


lines = degenerate(os.path.join('..', 'base_grammars', 'proper_reber.txt'))

for idx in range(len(lines)):
    beginning = [*random.choice(['BT', 'BP'])]
    ending = [*random.choice(['TE', 'PE'])]

    random.shuffle(beginning)
    random.shuffle(ending)

    line = f'{"".join(beginning)}{lines[idx]}{"".join(ending)}'
    lines[idx] = line

if __name__ == '__main__':
    with open('improper_embedded_reber.txt', 'w') as f:
        for line in lines:
            f.write(f'{line}\n')
