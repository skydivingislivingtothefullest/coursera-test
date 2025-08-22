# coursera-test

As the name says :-)

## Visualizing duplicate images

This repository includes a small utility, `show_duplicates.py`, which scans a
directory for duplicate images using the
[imagededup](https://github.com/idealo/imagededup) library and displays the
results.

### Installation

The utility depends on the optional extras for `imagededup` to handle image
decoding. Install them with:

```bash
pip install "imagededup[full]"
```

### Usage

Provide the path to the directory containing images:

```bash
python show_duplicates.py --dir /path/to/images
```
