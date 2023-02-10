import random

from reber_grammars.base_grammars.grammar_generator import generate


lines = list(generate())

for idx in range(len(lines)):
    beginning = random.choice(['BT', 'BP'])
    ending = random.choice(['TE', 'PE'])
    line = f'{beginning}{lines[idx]}{ending}'
    lines[idx] = line

if __name__ == '__main__':
    with open('proper_embedded_reber.txt', 'w') as f:
        for line in lines:
            f.write(f'{line}\n')
