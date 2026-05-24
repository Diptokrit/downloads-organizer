import shutil
from pathlib import Path

dir = Path.home() / "Downloads"

cat = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Code": [".py", ".js", ".java", ".cpp", ".c", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Audio": [".mp3", ".wav", ".aac"]
}


def get_unique_filename(destination, filename):
    new_file = destination / filename

    if not new_file.exists():
        return new_file

    stem = new_file.stem
    suffix = new_file.suffix
    counter = 1

    while True:
        candidate = destination / f"{stem}_{counter}{suffix}"

        if not candidate.exists():
            return candidate

        counter += 1


def Organize_files(folder: Path):
    for file in folder.iterdir():
        if file.is_file():
            moved = False

            for category, extensions in cat.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder / category
                    target_dir.mkdir(exist_ok=True)

                    destination = get_unique_filename(target_dir, file.name)
                    shutil.move(str(file), destination)

                    moved = True
                    break

            if not moved:
                other_dir = folder / "Other"
                other_dir.mkdir(exist_ok=True)

                destination = get_unique_filename(other_dir, file.name)
                shutil.move(str(file), destination)


if __name__ == "__main__":
    Organize_files(dir)
    print("Files Organised Successfully")