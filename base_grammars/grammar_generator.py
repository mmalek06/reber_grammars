import random


class Rule:
    def applies(self, string_so_far: str) -> bool:
        pass


class BRule(Rule):
    LETTER = 'b'

    def applies(self, string_so_far: str) -> bool:
        return string_so_far is None or len(string_so_far) == 0


class TRule(Rule):
    LETTER = 't'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [letter] if letter == BRule.LETTER:
                return True
            case [*_, BRule.LETTER, PRule.LETTER] | \
                 [*_, PRule.LETTER, TRule.LETTER] | \
                 [*_, TRule.LETTER, TRule.LETTER] | \
                 [*_, XRule.LETTER, XRule.LETTER] | \
                 [*_, XRule.LETTER, TRule.LETTER] | \
                 [*_, PRule.LETTER, XRule.LETTER]:
                return True
            case _:
                return False


class PRule(Rule):
    LETTER = 'p'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [BRule.LETTER] | \
                 [*_, TRule.LETTER, VRule.LETTER] | \
                 [*_, XRule.LETTER, VRule.LETTER] | \
                 [*_, PRule.LETTER, VRule.LETTER]:
                return True
            case _:
                return False


class VRule(Rule):
    LETTER = 'v'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [BRule.LETTER, PRule.LETTER] | \
                 [*_, PRule.LETTER, TRule.LETTER] | \
                 [*_, TRule.LETTER, TRule.LETTER] | \
                 [*_, XRule.LETTER, TRule.LETTER] | \
                 [*_, XRule.LETTER, XRule.LETTER] | \
                 [*_, PRule.LETTER, VRule.LETTER] | \
                 [*_, TRule.LETTER, VRule.LETTER] | \
                 [*_, XRule.LETTER, VRule.LETTER] | \
                 [*_, PRule.LETTER, XRule.LETTER]:
                return True
            case _:
                return False


class XRule(Rule):
    LETTER = 'x'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [BRule.LETTER, TRule.LETTER] | \
                 [*_, TRule.LETTER, SRule.LETTER] | \
                 [*_, SRule.LETTER, SRule.LETTER] | \
                 [*_, TRule.LETTER, XRule.LETTER] | \
                 [*_, SRule.LETTER, XRule.LETTER] | \
                 [*_, VRule.LETTER, PRule.LETTER]:
                return True
            case _:
                return False


class SRule(Rule):
    LETTER = 's'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [BRule.LETTER, TRule.LETTER] | \
                 [*_, TRule.LETTER, SRule.LETTER] | \
                 [*_, SRule.LETTER, SRule.LETTER] | \
                 [*_, TRule.LETTER, XRule.LETTER] | \
                 [*_, SRule.LETTER, XRule.LETTER] | \
                 [*_, VRule.LETTER, PRule.LETTER]:
                return True
            case _:
                return False


class ERule(Rule):
    LETTER = 'e'

    def applies(self, string_so_far: str) -> bool:
        match string_so_far:
            case [*_, XRule.LETTER, SRule.LETTER] | \
                 [*_, PRule.LETTER, SRule.LETTER] | \
                 [*_, VRule.LETTER, VRule.LETTER]:
                return True
            case _:
                return False


rules = [BRule(), TRule(), PRule(), VRule(), XRule(), SRule(), ERule()]


def generate(rules: list[Rule]) -> set[str]:
    lines = []
    counter = 0
    MAX = 500

    while len(set(lines)) < 2000:
        letters = []

        while True:
            counter += 1
            applicable_rules = list(filter(lambda rule: rule.applies(letters), rules))
            chosen_rule = random.choice(applicable_rules)
            next_letter = chosen_rule.LETTER

            letters.append(next_letter)

            if next_letter == ERule.LETTER:
                break
            if len(letters) >= MAX:
                letters = []

                break

        if len(letters) > 0:
            line = list(map(lambda char: char.upper(), letters))

            lines.append(''.join(line))

    return set(lines)


lines = generate(rules)

with open('proper_reber.txt', 'w') as f:
    for line in lines:
        f.write(f'{line}\n')
