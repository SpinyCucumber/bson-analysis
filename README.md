# BSON Size Analyzer

This is a fork of [mongodb/mongo-python-driver](https://github.com/mongodb/mongo-python-driver) which adds a command-line tool to analyze the structure and size of BSON files.

The specific feature is contained in the `size_analysis` branch.

## Installation

First, ensure the required build tools are up-to-date:
```
python -m pip install --upgrade pip setuptools wheel
```

Then, install from GitHub using pip:
```
pip install git+https://github.com/ehilty-hexagon/bson-analysis@size_analysis
```

## Usage

This package adds a single command, `bson-analyzer`, which accepts a BSON file and an optional output file (defaults to `stdout`).

The tool produces a "tree breakdown" of the provided BSON file. Each node's size in bytes is displayed, along with its size relative to its parent. Larger sibling nodes will appear before smaller sibling nodes.

## Sample Output

```
PS C:\Users\ehilty\Documents> bson-analyzer .\sample.bson
root: 395
  glossary: 390 (98.73%)
    GlossDiv: 347 (88.97%)
      GlossList: 319 (91.93%)
        GlossEntry: 303 (94.98%)
          GlossDef: 139 (45.87%)
            para: 83 (59.71%)
            GlossSeeAlso: 41 (29.50%)
              0: 11 (26.83%)
              1: 11 (26.83%)
          GlossTerm: 52 (17.16%)
          Abbrev: 26 (8.58%)
          GlossSee: 21 (6.93%)
          Acronym: 18 (5.94%)
          SortAs: 17 (5.61%)
          ID: 13 (4.29%)
      title: 13 (3.75%)
    title: 28 (7.18%)
```

*This BSON file was generated from [this JSON sample.](https://www.json.org/example.html)*

*Note that due to the size of headers and other metadata, the sum of childrens' sizes does not match the parent's size.*