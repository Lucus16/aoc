from collections import defaultdict

with open("day22.in", "r") as f:
    initials = [int(line) for line in f]

def evolve(secret):
    secret = (secret ^ (secret << 6)) & 0xffffff
    secret = (secret ^ (secret >> 5)) & 0xffffff
    secret = (secret ^ (secret << 11)) & 0xffffff
    return secret

sequences = dict()
for initial in initials:
    sequences[initial] = [initial]
    secret = initial
    for _ in range(2000):
        secret = evolve(secret)
        sequences[initial].append(secret)

print(sum([seq[-1] for seq in sequences.values()]))

all_prices = dict()
for initial, seq in sequences.items():
    changes = [s1 % 10 - s0 % 10 for s0, s1 in zip(seq, seq[1:])]
    prices = dict()
    for price, change_seq in zip(seq[4:], zip(changes, changes[1:], changes[2:], changes[3:])):
        if change_seq not in prices:
            prices[change_seq] = price % 10
    all_prices[initial] = prices

all_change_seqs = defaultdict(int)
for prices in all_prices.values():
    for seq, price in prices.items():
        all_change_seqs[seq] += price
print(max(all_change_seqs.values()))
