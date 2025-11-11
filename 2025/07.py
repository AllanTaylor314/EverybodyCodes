def rule_to_pairs(rule):
    i,o_str = rule.split(' > ')
    os = o_str.split(',')
    return frozenset(i+o for o in os)

def rules_to_allowed_follow_ups(rules):
    res = {}
    for rule in rules:
        i,o_str = rule.split(' > ')
        os = o_str.split(',')
        res[i] = os
    return res

def filter_prefixes(prefixes):
    new = []
    for p in sorted(prefixes,key=len):
        if not any(p.startswith(n) for n in new):
            new.append(p)
    return new

def load_file(part):
    with open(f"everybody_codes_e2025_q07_p{part}.txt") as f:
        header,_,*rules = f.read().splitlines()
    return header.split(','),rules

def meets_pairs(name,pairs):
    for i in range(len(name)-1):
        p = name[i:i+2]
        if p not in pairs:
            return False
    return True

def count_options(prefix,mapping):
    if len(prefix) > 11:
        return 0
    total = 0 if len(prefix) < 7 else 1
    next_chars = mapping.get(prefix[-1],())
    for char in next_chars:
        total += count_options(prefix+char,mapping)
    return total

names,rules = load_file(1)
pairs = {p for rule in rules for p in rule_to_pairs(rule)}

for name in names:
    if meets_pairs(name,pairs):
        print(name)
        break

names,rules = load_file(2)
pairs = {p for rule in rules for p in rule_to_pairs(rule)}

total = 0
for i,name in enumerate(names,1):
    if meets_pairs(name,pairs):
        total += i
print(total)

prefixes,rules = load_file(3)
prefixes = filter_prefixes(prefixes)
mapping = rules_to_allowed_follow_ups(rules)
pairs = {p for rule in rules for p in rule_to_pairs(rule)}
total = 0
for prefix in prefixes:
    if meets_pairs(prefix,pairs):
        total += count_options(prefix,mapping)
print(total)