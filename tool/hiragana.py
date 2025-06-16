import re
from pathlib import Path

ONLY_HIRAGANA_PATTERN = re.compile("[ぁ-わゐゑをんー]+")

data = Path("csv/JMnedict_without_eigo.csv").read_text(encoding = "utf-8")
data = data.split("\n")

out_4gram = []
out = []

for line in data:
    split_line = line.split(",", 1)
    surface = split_line[0]
    if ONLY_HIRAGANA_PATTERN.fullmatch(surface):
        out_4gram.append(line)
    else:
        out.append(line)

out = "\n".join(out)
out_4gram = "\n".join(out_4gram)

Path("JMnedict_01_hiragana.csv").write_text(out_4gram, encoding = "utf-8")
Path("JMnedict_01_without_hiragana.csv").write_text(out, encoding = "utf-8")
