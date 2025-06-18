from pathlib import Path
from tqdm import tqdm



def main ():

    file  = Path("build/kanji_ngram.csv")
    data = file.read_text(encoding="utf-8").split("\n")

    split_num = len(data) // 2
    Path("build/kanji_ngram_0.csv").write_text("\n".join(data[:split_num]), encoding="utf-8")
    Path("build/kanji_ngram_1.csv").write_text("\n".join(data[split_num:]), encoding="utf-8")

if __name__ == "__main__":
    main()