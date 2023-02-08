import random

from reber_grammars.base_grammars.grammar_degenerator import degenerate


lines = degenerate()

for idx in range(len(lines)):
    beginning = [*random.choice(['BT', 'BP'])]
    ending = [*random.choice(['TE', 'PE'])]

    random.shuffle(beginning)
    random.shuffle(ending)

    line = f'{"".join(beginning)}{lines[idx]}{"".join(ending)}'
    lines[idx] = line

with open('improper_embedded_reber.txt', 'w') as f:
    for line in lines:
        f.write(f'{line}\n')
