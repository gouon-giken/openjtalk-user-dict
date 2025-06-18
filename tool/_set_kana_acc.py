import re
from pathlib import Path


"""
nhk日本語アクセント辞書　カタカナのアクセント推定より抜粋
"""
ONLY_KATAKANA_PATTERN = re.compile("^[ァ-ワヰヱヲンヴー]+$")
youon_list = ["ァ", "ィ", "ゥ", "ェ", "ォ", "ャ", "ュ", "ョ"]


def is_csv_file(file: Path) -> bool:
    supported_extensions = [".csv"]
    return file.suffix.lower() in supported_extensions

def main():
    input_dir_path = Path("pyopenjtalk/user_dict_src")
    csv_files = [file for file in input_dir_path.rglob("*") if is_csv_file(file)]

    for file in csv_files:
        if "katakana" in str(file.name):
            data = file.read_text(encoding="utf-8").split("\n")
            out = []
            for line in data:
                i = line.split(",")
                surface = i[0]
                pron = surface
                mora = pron

                for youon in youon_list:
                    mora = mora.replace(youon, "")

                mora = len(mora)

                # 4モーラ以上の時後ろから数えて三番目までを高くする
                if mora >= 4:
                    accent = mora - 2

                else:
                    accent = 1

                if ONLY_KATAKANA_PATTERN.fullmatch(surface):
                    line = f"{surface},{i[1]},{i[2]},-3000,{i[4]},{i[5]},{i[6]},{i[7]},{i[8]},{i[9]},{surface},{pron},{pron},{accent}/{mora},*,{i[15]}"
                    out.append(line)

            out = "\n".join(out)
            file.write_text(out, encoding="utf-8")

if __name__ == "__main__":
    main()