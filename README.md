# PyAnalyzer
A Python-based text parsing tool used to analyze the energy minimization and find the center of mass of a protein molecule.

## Prerequites
This repository needs `Python 3.6+`.  

## Usage
### CMass
If you want to calculate the center of mass of a molecule, navigate to the `PyAnalyzer/namd/` folder.  

Execute the `cmmi.py` with a given pdb file and a directory of topology files.  
```shell
python3 cmmi.py <PDB_FILE> [TOPOLOGY_DIR]
```

Some example pdb file and topology files are provided in `PyAnalyzer/namd/pdb/` and `PyAnalyzer/namd/topology/`.

Execute the `cmmi.py` with no paramter.  
```shell
python3 cmmi.py
```

### MiniE
See the `minie` folder.  
