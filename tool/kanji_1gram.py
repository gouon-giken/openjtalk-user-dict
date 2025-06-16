import re
from pathlib import Path

KANJI_PATTERN = re.compile(r"^[\u4E00-\u9FFF\u3400-\u4DBF\u3005]+")

data = Path("bccwJ_01_without_2gram.csv").read_text(encoding = "utf-8")
data = data.split("\n")

out_1gram = []
out = []

for line in data:
    split_line = line.split(",", 1)
    surface = split_line[0]
    if len(surface) == 1 and KANJI_PATTERN.fullmatch(surface):
        out_1gram.append(line)
    else:
        out.append(line)

out = "\n".join(out)
out_1gram = "\n".join(out_1gram)

Path("bccwJ_01_1gram.csv").write_text(out_1gram, encoding = "utf-8")
Path("bccwJ_01_without_1gram.csv").write_text(out, encoding = "utf-8")
