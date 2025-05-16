import re
from pathlib import Path

ONLY_KATAKANA_PATTERN = re.compile("[ａ-ｚＡ-Ｚ]+")

data = Path("csv/bccwj_05_without_kanji_n_gram.csv").read_text(encoding = "utf-8")
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

Path("bccwj_05_eigo.csv").write_text(out_4gram, encoding = "utf-8")
Path("bccwj_05_without_eigo.csv").write_text(out, encoding = "utf-8")
