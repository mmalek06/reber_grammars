import random
import string


def degenerate(proper_reber_path):
    with open(proper_reber_path, 'r') as f:
        lines = [line.rstrip() for line in f]

    initial_length = len(lines)
    five_percent_count = int(.05 * len(lines))

    with open('../actual_words.txt', 'r') as f:
        random_words = list(set([line.rstrip() for line in f]))

    def get_diffed_list(diff: list[str]) -> list[str]:
        return list(set(lines) - set(diff))

    def choose(count=five_percent_count) -> list[str]:
        return random.sample(lines, k=count)

    grammar_letters = set(''.join(lines))
    alphabet = list(set(list(string.ascii_uppercase)) - grammar_letters)

    def switch_end_char() -> tuple[list[str], list[str]]:
        switch_end_char_list = choose()
        diffed_list = get_diffed_list(switch_end_char_list)

        for idx in range(len(switch_end_char_list)):
            switch_end_char_list[idx] = f'{switch_end_char_list[idx][:-1]}{random.choice(alphabet)}'

        return diffed_list, switch_end_char_list

    def switch_start_char() -> tuple[list[str], list[str]]:
        switch_start_char_list = choose()
        diffed_list = get_diffed_list(switch_start_char_list)

        for idx in range(len(switch_start_char_list)):
            switch_start_char_list[idx] = f'{random.choice(alphabet)}{switch_start_char_list[idx][1:]}'

        return diffed_list, switch_start_char_list

    def switch_both_chars() -> tuple[list[str], list[str]]:
        switch_both_chars_list = choose()
        diffed_list = get_diffed_list(switch_both_chars_list)

        for idx in range(len(switch_both_chars_list)):
            switch_both_chars_list[idx] = f'{random.choice(alphabet)}{"".join(switch_both_chars_list[idx][1:-1])}{random.choice(alphabet)}'

        return diffed_list, switch_both_chars_list

    def revert() -> tuple[list[str], list[str]]:
        revert_list = choose()
        diffed_list = get_diffed_list(revert_list)

        for idx in range(len(revert_list)):
            revert_list[idx] = revert_list[idx][::-1]

        return diffed_list, revert_list

    def cut_in_half() -> tuple[list[str], list[str]]:
        cut_in_half_list = choose()
        diffed_list = get_diffed_list(cut_in_half_list)

        for idx in range(len(cut_in_half_list)):
            cut_in_half_list[idx] = ''.join(cut_in_half_list[idx][:int(len(cut_in_half_list[idx]) / 2)])

        return diffed_list, cut_in_half_list

    def break_in_half_and_revert_end() -> tuple[list[str], list[str]]:
        break_in_half_and_revert_end_list = choose()
        diffed_list = get_diffed_list(break_in_half_and_revert_end_list)

        for idx in range(len(break_in_half_and_revert_end_list)):
            break_in_half_and_revert_end_list[idx] = \
                break_in_half_and_revert_end_list[idx][:int(len(break_in_half_and_revert_end_list[idx]) / 2)] + \
                break_in_half_and_revert_end_list[idx][int(len(break_in_half_and_revert_end_list[idx]) / 2):][::-1]

        return diffed_list, break_in_half_and_revert_end_list

    def break_in_half_and_revert_start() -> tuple[list[str], list[str]]:
        break_in_half_and_revert_start_list = choose()
        diffed_list = get_diffed_list(break_in_half_and_revert_start_list)

        for idx in range(len(break_in_half_and_revert_start_list)):
            break_in_half_and_revert_start_list[idx] = \
                break_in_half_and_revert_start_list[idx][:int(len(break_in_half_and_revert_start_list[idx]) / 2)][::-1] + \
                break_in_half_and_revert_start_list[idx][int(len(break_in_half_and_revert_start_list[idx]) / 2):]

        return diffed_list, break_in_half_and_revert_start_list

    def revert_middle() -> tuple[list[str], list[str]]:
        revert_middle_list = choose()
        diffed_list = get_diffed_list(revert_middle_list)

        for idx in range(len(revert_middle_list)):
            revert_middle_list[idx] = \
                revert_middle_list[idx][0] + \
                revert_middle_list[idx][1:-1][::-1] + \
                revert_middle_list[idx][-1]

        return diffed_list, revert_middle_list

    def replace_with_oov_words() -> tuple[list[str], list[str]]:
        count = int(.2 * initial_length)
        oov_words = choose(count)
        diffed_list = get_diffed_list(oov_words)
        words = random.sample(random_words, count)

        return diffed_list, words

    def replace_with_structurally_identical_words() -> tuple[list[str], list[str]]:
        '''
        :return:
            diffed_words: the original list minus the chosen lines
            replaced_words: because the shuffling happens only once, every string will have the same "schema"
                            which means the same shape: KDQQNMQDDDNNZ, KDQQDDDNMQNNZ - two possible examples.
                            The method could be improved further to randomize the return values even more.
        '''
        replace_words = choose(int(.2 * initial_length))
        diffed_words = get_diffed_list(replace_words)
        alphabet_shuffled = alphabet[:]

        random.shuffle(alphabet_shuffled)

        alphabet_iterator = iter(alphabet_shuffled)
        mapped_letters = {key: next(alphabet_iterator) for key in grammar_letters}
        replaced_words = []

        for idx in range(len(replace_words)):
            new_word = []

            for inner_idx in range(len(replace_words[idx])):
                new_word.append(mapped_letters[replace_words[idx][inner_idx]])

            replaced_words.append(''.join(new_word))

        return diffed_words, replaced_words

    def randomly_replace_letters() -> tuple[None, list[str]]:
        replacers = []

        for word in lines:
            num_letters_to_replace = random.choice(list(range(len(word)))) + 1
            indexes_to_replace = random.sample(list(range(len(word))), k=num_letters_to_replace)
            next_word = word

            for idx in indexes_to_replace:
                replacement = random.choice(alphabet)
                next_word = f'{next_word[:idx]}{replacement}{next_word[(idx + 1):]}'

            replacers.append(next_word)

        return None, replacers

    lines, with_switched_ends = switch_end_char()
    lines, with_switched_starts = switch_start_char()
    lines, with_switched_both = switch_both_chars()
    lines, reverted = revert()
    lines, cut_in_halves = cut_in_half()
    lines, broken_and_end_reverted = break_in_half_and_revert_end()
    lines, broken_and_start_reverted = break_in_half_and_revert_start()
    lines, middle_reverted = revert_middle()
    lines, oov_words = replace_with_oov_words()
    lines, structurally_ident_words = replace_with_structurally_identical_words()
    lines, with_randomly_replaced_letters = randomly_replace_letters()
    new_lines = \
        with_switched_ends + \
        with_switched_starts + \
        with_switched_both + \
        reverted + \
        cut_in_halves + \
        broken_and_end_reverted + \
        broken_and_start_reverted + \
        middle_reverted + \
        oov_words + \
        structurally_ident_words + \
        with_randomly_replaced_letters

    return new_lines


if __name__ == '__main__':
    new_lines = degenerate('proper_reber.txt')

    with open('improper_reber.txt', 'w') as f:
        for line in set(new_lines):
            f.write(f'{line}\n')
