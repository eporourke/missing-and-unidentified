from pathlib import Path
import shutil
import re

source_dir = Path(r"C:\Users\Erin\Documents\Data\github\missing-and-unidentified\data\scraped\dekalb_unidentified")
target_dir = source_dir   # Same folder, just organizing it

case_pattern = re.compile(r"(\d{2}-\d{4})")

for file in source_dir.iterdir():

    # Skip folders
    if not file.is_file():
        continue

    # Find the case number anywhere in the filename
    match = case_pattern.search(file.name)

    if not match:
        print(f"Skipping {file.name}")
        continue

    case_number = match.group(1)

    case_folder = target_dir / case_number
    case_folder.mkdir(exist_ok=True)

    destination = case_folder / file.name

    print(f"Moving {file.name} → {case_folder}")

    shutil.move(file, destination)