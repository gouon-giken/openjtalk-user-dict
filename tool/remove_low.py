from pathlib import Path

from tqdm import tqdm


def is_csv_file(file: Path) -> bool:
    supported_extensions = [".csv"]
    return file.suffix.lower() in supported_extensions

def main():
    input_dir_path = Path("./build")
    csv_files = [file for file in input_dir_path.rglob("*") if is_csv_file(file)]

    for file in csv_files:
        data_list = []
        text_list = file.read_text(encoding="utf-8").split("\n")

        for line in tqdm(text_list):
            split_line = line.split(",")

            if split_line[3] == "":
                new_split_line = split_line[:3] + ["8000"] + split_line[4:]
                split_line = new_split_line

                line = ",".join(split_line)
                
                print(split_line[0])


            if len(split_line) == 15:
                data_list.append(line)

            elif len(split_line) < 15:
                continue

            else:
                cur_line = ",".join( split_line[:15] )
                data_list.append(cur_line)

        file.write_text( "\n".join(data_list), encoding = "utf-8" )

if __name__ == "__main__":
    main()