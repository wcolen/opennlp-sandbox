import random
import sys

train = []
dev = []
test = []

def remove_control_chars(s):
    return control_char_re.sub('', s)

if len(sys.argv) != 2:
    print("Usage split.py corpus_file")
    sys.exit()

corpus_in = sys.argv[1]

with open(corpus_in, "r", encoding="utf-8") as f:
    for line in f:

        if len(line.strip()) == 0:
            continue

        line = "".join(c for c in line if c.isprintable() or c in "\n\t")

        rand = random.random()
        if rand < 0.8:
            train.append(line)
        elif rand < 0.9:
            dev.append(line)
        elif rand <= 1.0:
            test.append(line)

with open(corpus_in + '.train', 'w', encoding="utf-8") as f:
    for item in train:
        f.write("%s" % item)

with open(corpus_in + '.dev', 'w', encoding="utf-8") as f:
    for item in dev:
        f.write("%s" % item)

with open(corpus_in + '.test', 'w', encoding="utf-8") as f:
    for item in test:
        f.write("%s" % item)