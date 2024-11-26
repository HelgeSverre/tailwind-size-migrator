# Tailwind Size Migrator 🎨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line tool that automatically migrates legacy Tailwind CSS height/width utility combinations to the new
`size-{n}` utility class where applicable.

## What it does

This tool scans your project for HTML and Blade files, finding instances where you've used `h-{n}` and `w-{n}` together
with the same value (where n is 1-12) and replaces them with the equivalent `size-{n}` utility class.

For example:

```html
<!-- Before -->
<div class="w-6 h-6 text-gray-500">...</div>

<!-- After -->
<div class="size-6 text-gray-500">...</div>
```

## Features

- 🔍 Recursively scans directories for `.html` and `.blade.php` (or whatever) files
- 🚫 Automatically skips `node_modules` and `vendor` directories
- ✨ Only updates files that need changes
- 📝 Provides detailed console output of processed files
- 🔒 Safe processing with error handling
- 💡 Maintains all other classes and file formatting

## Installation

```bash
git clone https://github.com/helgesverre/tailwind-size-migrator.git
cd tailwind-size-migrator
```

## Usage

1. Navigate to your project directory where your HTML/Blade files are located
2. Run the script:

```bash
python tailwind_size_migrator.py
```

The script will:

1. Search for all `.html` and `.blade.php` files
2. Process each file and replace applicable class combinations
3. Show progress and results in the console
4. Provide a summary of processed and updated files

## Example Output

```
Starting Tailwind class replacement...
Searching for .html and .blade.php files...

✓ Updated: ./resources/views/components/icon.blade.php
- Skipped: ./resources/views/layouts/app.blade.php (no changes needed)
✓ Updated: ./resources/views/dashboard.blade.php

Summary:
Files scanned: 3
Files updated: 2
```

## Formatting

```shell
pipx run black main.py
```

## Requirements

- Python 3.6 or higher

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
