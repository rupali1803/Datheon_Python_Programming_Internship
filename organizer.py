
import shutil
from pathlib import Path

folder = Path(input("Enter folder path: ").strip())

if not folder.is_dir():
    print("Invalid folder path!")
    raise SystemExit

types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".rar"],
    "Code": [".py", ".java", ".c", ".cpp"]
}

moved = 0

for file in folder.iterdir():
    if not file.is_file():
        continue

    category = next(
        (name for name, exts in types.items()
         if file.suffix.lower() in exts),
        "Others"
    )

    dest_folder = folder / category
    dest_folder.mkdir(exist_ok=True)
    destination = dest_folder / file.name

    if destination.exists():
        print("Skipped:", file.name)
        continue

    try:
        shutil.move(str(file), str(destination))
        print(f"Moved: {file.name} -> {category}")
        moved += 1
    except OSError as e:
        print(f"Error: {file.name} - {e}")

print("\nTotal files moved:", moved)
print("File organization completed!")

