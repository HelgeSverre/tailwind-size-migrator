import re
import argparse
from pathlib import Path
from typing import List


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
            return True
        else:
            print(f"- Skipped: {file_path} (no changes needed)")
            return False
    except Exception as e:
        print(f"✗ Error processing {file_path}: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Replace Tailwind height/width classes with size classes where applicable."
    )
    parser.add_argument(
        "-p",
        "--path",
        default=".",
        help="Directory path to search in (default: current directory)",
    )
    parser.add_argument(
        "-e",
        "--ext",
        nargs="+",
        default=[".html", ".blade.php"],
        help="File extensions to process (default: .html .blade.php)",
    )
    parser.add_argument(
        "-x",
        "--exclude-dirs",
        nargs="+",
        default=["vendor", "node_modules"],
        help="Directories to exclude (default: vendor node_modules)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be modified without making changes",
    )

    args = parser.parse_args()

    # Convert to Path object and resolve to absolute path
    base_path = Path(args.path).resolve()

    if not base_path.exists():
        print(f"Error: Path '{base_path}' does not exist")
        return 1

    print(f"Starting Tailwind class replacement...")
    print(f"Search path: {base_path}")
    print(f"File extensions: {', '.join(args.ext)}")
    print(f"Excluded directories: {', '.join(args.exclude_dirs)}")
    if args.dry_run:
        print("DRY RUN: No files will be modified")
    print("Searching for files...\n")

    file_count = 0
    updated_count = 0

    # Process each file extension
    for ext in args.ext:
        # Remove leading dot if present and ensure there is one
        ext = "." + ext.lstrip(".")
        pattern = f"**/*{ext}"

        for file_path in base_path.glob(pattern):
            # Skip excluded directories
            if any(excluded in str(file_path.parent) for excluded in args.exclude_dirs):
                continue

            file_count += 1

            if args.dry_run:
                content = file_path.read_text(encoding="utf-8")
                new_content = replace_tailwind_classes(content)
                if content != new_content:
                    print(f"Would update: {file_path}")
                    updated_count += 1
            else:
                was_updated = process_file(file_path)
                if was_updated:
                    updated_count += 1

    print(f"\nSummary:")
    print(f"Files scanned: {file_count}")
    if args.dry_run:
        print(f"Files that would be updated: {updated_count}")
    else:
        print(f"Files updated: {updated_count}")

    return 0


if __name__ == "__main__":
    exit(main())
