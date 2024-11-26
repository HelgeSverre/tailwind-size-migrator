# Tailwind Size Migrator 🎨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Works on My Machine](https://img.shields.io/badge/Works-On%20My%20Machine-success.svg)](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)
[![Over Engineered](https://img.shields.io/badge/Over%20Engineered-Definitely-red.svg)](https://github.com/helgesverre)
[![Time Saved](https://img.shields.io/badge/Time%20Saved-Probably%20Negative-orange.svg)](https://xkcd.com/1205/)

<center>
<img src="/art/header.png">
</center>

A command-line tool that automatically migrates legacy Tailwind CSS height/width utility combinations to the new
`size-{n}` utility class where applicable.

## What it does

This tool scans your project files, finding instances where you've used `h-{n}` and `w-{n}` together
with the same value (where n is 1-12) and replaces them with the equivalent `size-{n}` utility class. Yes, this is
literally all it does.

For example:

```html
<!-- Before -->
<div class="w-6 h-6 text-gray-500">...</div>

<!-- After -->
<div class="size-6 text-gray-500">...</div>
```

## Features

- 🔍 Recursively scans directories for specified file extensions (like find+replace but more complicated)
- 🚫 Configurable directory exclusion (because we learned from that one time we borked node_modules)
- ✨ Only updates files that need changes (revolutionary, I know)
- 📝 Provides detailed console output of processed files (for when you need to know what you broke)
- 🔒 Safe processing with error handling (as safe as modifying files can be)
- 💡 Maintains all other classes and file formatting (we're not monsters)
- 🔄 Dry run mode to preview changes (for the paranoid among us)

## Installation

```bash
git clone https://github.com/helgesverre/tailwind-size-migrator.git
cd tailwind-size-migrator
```

## Usage

1. Navigate to your project directory
2. Back up your files (you're going to ignore this anyway)
3. Run the script with your desired options:

```bash
# Use defaults (current directory, .html and .blade.php files, vendor and node_modules folders are excluded)
python main.py

# Specify a different directory (default is current directory, which makes sense if you copy the script to your project)
python main.py -p ./src

# Specify custom extensions (for you non-Laravel folks, you know who you are)
python main.py -e .jsx .tsx .html

# Exclude specific directories (instead of the defaults vendor and node_modules)
python main.py -x build dist cache

# Specify path, extensions and exclusions (for the control freaks)
python main.py -p ./src -e .jsx .tsx -x build dist

# Do a dry run to see what would be changed without making changes
python main.py --dry-run

# Get help
python main.py --help
```

### Command Line Options

| Option                 | Description                                               |
|------------------------|-----------------------------------------------------------|
| `-p`, `--path`         | Directory path to search in (default: current directory)  |
| `-e`, `--ext`          | File extensions to process (default: .html .blade.php)    |
| `-x`, `--exclude-dirs` | Directories to exclude (default: vendor node_modules)     |
| `--dry-run`            | Show which files would be modified without making changes |

## Example Output

```
Starting Tailwind class replacement...
Search path: /path/to/your/project
File extensions: .html, .blade.php
Excluded directories: vendor, node_modules
Searching for files...

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

- Python 3.6 or higher (I actually have no clue, figure it out yourself, nobody understands python anyways)
