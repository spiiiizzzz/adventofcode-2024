from functools import cmp_to_key

def main():
    with open("input.txt", "r") as f:
        raw = f.readlines()
        empty_index = 0
        for i in range(0, len(raw)):
            if not raw[i].strip():
                empty_index = i
        rules_tmp = list(map(lambda l: tuple(map(int, l.strip().split("|"))), raw[:empty_index]))
        rules = {}
        for rule in rules_tmp:
            if not rule[1] in rules.keys():
                rules[rule[1]] = []
            rules[rule[1]].append(rule[0])
        sequences = list(map(lambda l: list(map(int, l.strip().split(","))), raw[empty_index+1:]))

        def custom_compare(a: int, b: int) -> int:
            if a in rules.keys() and b in rules[a]:
                return 1
            if b in rules.keys() and a in rules[b]:
                return -1
            return 0

        invalid_sequences = []
        for sequence in sequences:
            active_rules = {}
            for i in range(0, len(sequence)):
                if sequence[i] in sum(list(active_rules.values()), []):
                    invalid_sequences.append(sequence)
                    break
                if sequence[i] in rules.keys():
                    active_rules[sequence[i]] = rules[sequence[i]]
        
        total = 0
        for inv in invalid_sequences:
            new_sequence = sorted(inv, key=cmp_to_key(custom_compare))
            total += new_sequence[len(new_sequence)//2]

        print(total)


if __name__ == "__main__":
    main()