import re
from pathlib import Path

ONLY_KATAKANA_PATTERN = re.compile("[ァ-ワヰヱヲンヴー]+")

data = Path("csv/JMnedict_without_kanji1-4gram.csv").read_text(encoding = "utf-8")
data = data.split("\n")

out_4gram = []
out = []

for line in data:
    split_line = line.split(",", 1)
    surface = split_line[0]
    if ONLY_KATAKANA_PATTERN.fullmatch(surface):
        out_4gram.append(line)
    else:
        out.append(line)

out = "\n".join(out)
out_4gram = "\n".join(out_4gram)

Path("JMnedict_katakana.csv").write_text(out_4gram, encoding = "utf-8")
Path("JMnedict_without_katakana.csv").write_text(out, encoding = "utf-8")
