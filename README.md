# PyAnalyzer
A Python-based text parsing tool used to analyze the NAMD and HPCC results.

## Prerequites
This repository needs `Python 3.6+`.  
No other external packge is required.

## Usage
### NAMD cmass
If you want to calculate the center of mass of a molecule, navigate to the `PyAnalyzer/namd/` folder.  

Execute the `cmmi.py` with a given pdb file and a directory of topology files.  
```shell
python cmmi.py <PDB_FILE> [TOPOLOGY_DIR]
```

Some example pdb file and topology files are provided in `PyAnalyzer/namd/pdb/` and `PyAnalyzer/namd/topology/`.

Execute the `cmmi.py` with no paramter.  
```shell
python cmmi.py
```