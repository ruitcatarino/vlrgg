# VLRgg

[![License: GPL v3](https://img.shields.io/badge/license-MIT-blue.svg)](https://spdx.org/licenses/MIT.html)

An Unofficial script to retrieve results and upcoming matches from [vlr.gg](https://www.vlr.gg/), a Valorant Esports match and news coverage site.

This script could not have been made without the use of the [Unofficial REST API for vlr.gg](https://github.com/axsddlr/vlrggapi) made by [Andre Saddler](https://github.com/axsddlr/)

Built by [Rui Catarino](https://github.com/ruitcatarino)

## Usage

```bash
usage: vlrgg.py [-h] [-t TEAM] [-l] [-u]

options:
  -h, --help            show this help message and exit
  -t TEAM, --team TEAM  Team Name
  -l, --last            Only get last game
  -u, --upcoming        Get upcoming matches
```

### Example of Usage
```bash
python3 vlrgg.py -l
```
#### Ouput
```
Playoffs-Lower Round 2 in Champions Tour 2023: Masters Tokyo
Paper Rex vs EDward Gaming
2 - 1
More info: https://www.vlr.gg/220452/paper-rex-vs-edward-gaming-champions-tour-2023-masters-tokyo-lr2
```
## Installation
```bash
git clone https://github.com/ruitcatarino/vlrgg
cd vlrgg
pip install -r requirements.txt
```
### Create alias
If you want to run the script from anywhere in your machine you can create an alias in your **$HOME/.bashrc**

Just add the following line to the end of the **$HOME/.bashrc** file

```bash
alias vlrgg=python3 {path_to_cloned_repo}/vlrgg.py
```
>Note: Replace *{path_to_cloned_repo}* with the correct path to the cloned repo

This way, all you need to do to run the script is type **vlrgg** with the desired flags

#### Example
```bash
vlrgg -l
```
##### Ouput
```
Playoffs-Lower Round 2 in Champions Tour 2023: Masters Tokyo
Paper Rex vs EDward Gaming
2 - 1
More info: https://www.vlr.gg/220452/paper-rex-vs-edward-gaming-champions-tour-2023-masters-tokyo-lr2
```

## Using Poetry
If you are using Poetry you should know what you are doing, but just in case you forget something, here is a reminder:

### Usage
```bash
poetry run python vlrgg.py
```
