import re
from pathlib import Path

KANJI_PATTERN = re.compile(r"^[\u4E00-\u9FFF\u3400-\u4DBF\u3005]+")

data = Path("bccwj_05_without_4gram.csv").read_text(encoding = "utf-8")
data = data.split("\n")

out_3gram = []
out = []

for line in data:
    split_line = line.split(",", 1)
    surface = split_line[0]
    if len(surface) == 3 and KANJI_PATTERN.fullmatch(surface):
        out_3gram.append(line)
    else:
        out.append(line)

out = "\n".join(out)
out_3gram = "\n".join(out_3gram)

Path("bccwj_05_3gram.csv").write_text(out_3gram, encoding = "utf-8")
Path("bccwj_05_without_3gram.csv").write_text(out, encoding = "utf-8")
