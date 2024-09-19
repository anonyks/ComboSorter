# ComboSorter #Only4ThoseWhoKnows

`ComboSorter` is a Python utility designed to efficiently sort and organize email-password combinations, commonly referred to as "combos". This tool reads from a list of combos in the format `email:password` and sorts them into separate files based on their email domain. It handles encoding errors gracefully and appends to existing files to avoid data loss.

## Features

- **Domain Sorting**: Sorts email-password combos by their email domains.
- **Encoding Robustness**: Skips lines with encoding errors to ensure smooth processing.

## Getting Started

### Prerequisites

Before running ComboSorter, ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/). This script also requires the `colorama` package for colored output in the terminal.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/anonyks/ComboSorter.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd ComboSorter
   ```
3. Install the required packages:
   ```bash
   pip install colorama
   ```

### Usage

To run the script, execute the following command in the terminal:

```bash
python combo_sorter.py
```

Follow the on-screen prompts to select your combo list file, and the tool will handle the rest, sorting the combos into appropriately named files within the `sorted` directory.

## Contributing

Contributions are welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

## Contact
[@AnonyKs_xD](https://t.me/@AnonyKs_xD)
