from pathlib import Path

from tqdm import tqdm
import re

def is_csv_file(file: Path) -> bool:
    supported_extensions = [".csv"]
    return file.suffix.lower() in supported_extensions

def main():

    KANA_PATTERN = re.compile("[ァ-ロワヲンヴー]+")
    komoji_list = ["ァ","ィ","ゥ","ェ","ォ","ャ","ュ","ョ", "ヮ"]
    
    VU_PATTERN = re.compile("ヴ[ョュャォェィァ]")
    RI_PATTERN = re.compile("リ[ョュャェ]")
    MI_PATTERN = re.compile("ミ[ョュャェ]")
    HU_PATTERN = re.compile("フ[ォェィァ]")
    HI_PATTERN = re.compile("ヒ[ョュャェ]")
    PI_PATTERN = re.compile("ビ[ョュャェ]")
    BI_PATTERN = re.compile("ピ[ョュャェ]")
    NI_PATTERN = re.compile("ニ[ョュャェ]")
    TU_PATTERN = re.compile("[トド]ゥ")
    DE_PATTERN = re.compile("デ[ョュャィ]")
    TE_PATTERN = re.compile("テ[ョュャィ]")
    TSU_PATTERN = re.compile("ツ[ォェィァ]")
    CHI_PATTERN = re.compile("チ[ョュャェ]")
    ZU_PATTERN = re.compile("[スズ]ィ")
    JI_PATTERN = re.compile("ジ[ョュャェ]")
    SI_PATTERN = re.compile("シ[ョュャェ]")
    GI_PATTERN = re.compile("ギ[ョュャェ]")
    KI_PATTERN = re.compile("キ[ョュャェ]")
    U_PATTERN = re.compile("ウ[ォェィ]")
    I_PATTERN = re.compile("イェ")

    NUM_PATTERN = re.compile("[1234567890]+")

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
                    mora = VU_PATTERN.sub("_", mora)
                    mora = RI_PATTERN.sub("_", mora)
                    mora = MI_PATTERN.sub("_", mora)
                    mora = HU_PATTERN.sub("_", mora)
                    mora = HI_PATTERN.sub("_", mora)
                    mora = PI_PATTERN.sub("_", mora)
                    mora = BI_PATTERN.sub("_", mora)
                    mora = NI_PATTERN.sub("_", mora)
                    mora = TU_PATTERN.sub("_", mora)
                    mora = DE_PATTERN.sub("_", mora)
                    mora = TE_PATTERN.sub("_", mora)
                    mora = TSU_PATTERN.sub("_", mora)
                    mora = CHI_PATTERN.sub("_", mora)
                    mora = ZU_PATTERN.sub("_", mora)
                    mora = JI_PATTERN.sub("_", mora)
                    mora = SI_PATTERN.sub("_", mora)
                    mora = GI_PATTERN.sub("_", mora)
                    mora = KI_PATTERN.sub("_", mora)
                    mora = U_PATTERN.sub("_", mora)
                    mora = I_PATTERN.sub("_", mora)

            mora = len(mora)
            mora_acc = split_line[13]
            mora_acc_split = mora_acc.split("/")
            if len( mora_acc_split ) == 2 and mora_acc != "*/*":

                mora_acc = f"{mora_acc_split[0]}/{mora}" 

                split_line = split_line[:13] + [mora_acc, split_line[14] ]
                line = ",".join(split_line)

            if "　" in pron:
                pron = pron.replace("　", "")
                new_split_line = split_line[:12] + [pron] + split_line[13:]
                line = ",".join(new_split_line)
        
            if KANA_PATTERN.fullmatch(pron) or file.name == "symbols.csv":

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
            else:
                print(pron)

        file.write_text( "\n".join(data_list), encoding = "utf-8" )

if __name__ == "__main__":
    main()