from pathlib import Path
from tqdm import tqdm

def is_csv_file(file: Path) -> bool:
    supported_extensions = [".csv"]
    return file.suffix.lower() in supported_extensions

def main ():
    input_dir_path = Path("src/csv_4_5gram")
    csv_files = [file for file in input_dir_path.rglob("*") if is_csv_file(file)]

    surface_list = []
    out = []

    file_num = 1
    for file in csv_files:
        print(f"current file num:{file_num}/{len(csv_files)} filename:{str(file.name)}")
        data = file.read_text(encoding="utf-8").split("\n")

        for line in tqdm(data):
            surface = line.split(",", 1)[0]
            kana = line.split(",")[11]
            
            if not surface in surface_list:
                surface_list.append((surface, kana))
                out.append(line)
        file_num += 1
        
    Path("build/kanji_4_5gram.csv").write_text("\n".join(out), encoding="utf-8")
    

if __name__ == "__main__":
    main()