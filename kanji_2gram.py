import re
from pathlib import Path

KANJI_PATTERN = re.compile(r"^[\u4E00-\u9FFF\u3400-\u4DBF\u3005]+")

data = Path("bccwj_05_without_3gram.csv").read_text(encoding = "utf-8")
data = data.split("\n")

out_2gram = []
out = []

for line in data:
    split_line = line.split(",", 1)
    surface = split_line[0]
    if len(surface) == 2 and KANJI_PATTERN.fullmatch(surface):
        out_2gram.append(line)
    else:
        out.append(line)

out = "\n".join(out)
out_2gram = "\n".join(out_2gram)

Path("bccwj_05_2gram.csv").write_text(out_2gram, encoding = "utf-8")
Path("bccwj_05_without_2gram.csv").write_text(out, encoding = "utf-8")
