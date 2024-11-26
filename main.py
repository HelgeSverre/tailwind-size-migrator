import re
from pathlib import Path


def replace_tailwind_classes(content):
    """
    Replace Tailwind height/width pairs with size class where applicable.
    Only matches exact pairs where both numbers are identical.
    """
    pattern = r"(?:h-(\d{1,2})\s+w-(\d{1,2})|w-(\d{1,2})\s+h-(\d{1,2}))"

    def replace_match(match):
        if match.group(1) and match.group(2):  # h-n w-n pattern
            h_num, w_num = match.group(1), match.group(2)
        else:  # w-n h-n pattern
            h_num, w_num = match.group(4), match.group(3)

        if h_num == w_num and 1 <= int(h_num) <= 12:
            return f"size-{h_num}"
        return match.group(0)

    return re.sub(pattern, replace_match, content)


def should_skip_directory(dir_path):
    """Check if directory should be skipped."""
    skip_dirs = {"node_modules", "vendor"}
    return dir_path.name in skip_dirs


def process_file(file_path):
    """Process a single file and replace its contents."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = replace_tailwind_classes(content)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✓ Updated: {file_path}")
        else:
            print(f"- Skipped: {file_path} (no changes needed)")

    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")


def main():
    current_dir = Path(".")
    file_count = 0
    updated_count = 0

    print("Starting Tailwind class replacement...")
    print("Searching for files...\n")

    for file_pattern in ["**/*.html", "**/*.blade.php"]:
        for file_path in current_dir.glob(file_pattern):
            # Skip files in node_modules and vendor directories
            if any(
                part in str(file_path.parent) for part in ["node_modules", "vendor"]
            ):
                continue

            file_count += 1
            before_content = file_path.read_text(encoding="utf-8")
            process_file(file_path)
            after_content = file_path.read_text(encoding="utf-8")

            if before_content != after_content:
                updated_count += 1

    print(f"\nSummary:")
    print(f"Files scanned: {file_count}")
    print(f"Files updated: {updated_count}")


if __name__ == "__main__":
    main()
