from pathlib import Path

from tqdm import tqdm
import re

def is_csv_file(file: Path) -> bool:
    supported_extensions = [".csv"]
    return file.suffix.lower() in supported_extensions

def main():

    KANA_PATTERN = re.compile("[ァ-ヴー　]+")
    komoji_list = ["ァ","ィ","ゥ","ェ","ォ","ャ","ュ","ョ", "ヮ"]
    
    LA_PATTERN = re.compile("[ウフツシジヴツ]ァ")
    LI_PATTERN  = re.compile("[ウフヴテデツ]ィ")
    LU_PATTERN  = re.compile("[トド]ゥ")
    LE_PATTERN  = re.compile("[ウシジチフヴツ]ェ")
    LO_PATTERN = re.compile("[ウフヴツ]ォ")
    KWA_PATTERN = re.compile("[クグ]ヮ")
    LYA_PATTERN = re.compile("[キギシジチヂニヒビピミリ]ャ")
    LYU_PATTERN = re.compile("[キギシジチヂテデニヒビピフブプミリ]ュ")
    LYO_PATTERN = re.compile("[キギシジチヂニヒビピミリ]ョ")

    input_dir_path = Path("./build")
    csv_files = [file for file in input_dir_path.rglob("*") if is_csv_file(file)]

    for file in csv_files:
        data_list = []
        text_list = file.read_text(encoding="utf-8").split("\n")

        

        for line in tqdm(text_list):
            split_line = line.split(",")

            pron = split_line[12]
            mora = pron
            
            for i in komoji_list:
                if i in mora:
                    mora = LA_PATTERN.sub("_", mora)
                    mora = LI_PATTERN.sub("_", mora)
                    mora = LU_PATTERN.sub("_", mora)
                    mora = LE_PATTERN.sub("_", mora)
                    mora = LO_PATTERN.sub("_", mora)
                    mora = LYA_PATTERN.sub("_", mora)
                    mora = LYU_PATTERN.sub("_", mora)
                    mora = LYO_PATTERN.sub("_", mora)
                    mora = KWA_PATTERN.sub("_", mora)

            mora = len(mora)
            mora_acc = split_line[13]
            mora_acc_split = mora_acc.split("/")
            if len( mora_acc_split ) == 2 and mora_acc != "*/*":
                mora_acc = f"{mora_acc_split[0]}/{mora}" 

                split_line = split_line[:13] + [mora_acc, split_line[14] ]
                line = ",".join(split_line)

            if "　" in pron and KANA_PATTERN.fullmatch(pron):
                
                pron = pron.replace("　", "")
                if pron == "":
                    pron = "　"

                print(pron)
                new_split_line = split_line[:12] + [pron] + split_line[13:]
                line = ",".join(new_split_line)


            if split_line[3] == "":
                split_line = split_line[:3] + ["8000"] + split_line[4:]

                line = ",".join(split_line)

                print(split_line[0])


            if len(split_line) == 15:
                data_list.append(line)

            elif len(split_line) < 15:
                continue

            else:
                line = ",".join( split_line[:15] )
                data_list.append(line)
        
        file.write_text( "\n".join(data_list), encoding = "utf-8" )

if __name__ == "__main__":
    main()