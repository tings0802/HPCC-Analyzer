###### tags: `HPCAI`  
# PyAnalyzer MiniE  
> version: 1.0  

A Python-based LAMMPS log file parser and visualizer used to show the energy minimizing process of a molecular simulation  

## Requirement  
- Python 3.6+  
- Pandas 1.0+  
- Matplotlib 3.3+  

```bash
pip3 install -r requirements.txt
```

## Feature  
- Extract data from the log file and reorganize it as a csv file  
- Use configuration file to decide what data should be taken
- Plot a "E-t graphs" (energy versus timestep) from a csv input and save as a png  

## Usage  
```bash
minie.py [-h] [-v] [--cfg <file>] [--csv <file>] [--png <file>] input  
```

#### Positional arguments
`input`: specify the input file

#### Optional arguments  
`-h`, `--help`: show the help message and leave  
`-v`, `--verbose`: print data as tablular format verbosely  
`--cfg`: specify the configuration file, default: config.txt  
`--csv`: specify the csv file path, default: `EM[timestamp].csv`  
`--png`: specify the png file path, default: `EM[timestamp]-[type].png`  