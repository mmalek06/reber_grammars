import random


with open('proper_reber.txt', 'r') as f:
    lines = [line.rstrip() for line in f]


initial_length = len(lines)
switch_end_char_size = int(.05 * initial_length)
switch_end_char_list = random.choices(lines, k=switch_end_char_size)
lines = list(set(lines) - set(switch_end_char_list))
switch_start_char_size = int(.05 * initial_length)
switch_start_char_list = random.choices(lines, k=switch_start_char_size)
lines = list(set(lines) - set(switch_start_char_list))
