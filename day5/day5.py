

def main():
    with open("input.txt", "r") as f:
        # comical amount of code to parse the input :P
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

        total = 0
        for sequence in sequences:
            active_rules = {}
            valid = True
            for i in range(0, len(sequence)):
                if sequence[i] in sum(list(active_rules.values()), []):
                    valid = False
                    break
                if sequence[i] in rules.keys():
                    active_rules[sequence[i]] = rules[sequence[i]]
            if valid:
                total += sequence[len(sequence)//2]
        
        print(total)


if __name__ == "__main__":
    main()