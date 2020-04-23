def atomicCoor(path):
    ''' retrieve the x, y, z coordinates of every atoms in the molecule '''
    with open(path, 'r') as ifile:
        raw = ifile.readlines()
    
    acoor = hcoor = []

    for data in raw:
        data = data.split()
        record = data[0]
        if record == 'ATOM':
            acoor.append([data[2], data[6], data[7], data[8]])
        elif record == 'HETATM':
            hcoor.append([data[2], data[5], data[6], data[7]])

    return acoor, hcoor

def atomicMass(path):
    ''' retrieve the atomic mass of every atoms '''
    with open(path, 'r') as ifile:
        raw = ifile.readlines()
    
    atomicMasses = {}

    for row in raw:
        data = row.split()
        try:
            if data[0] == 'MASS':
                atomicMasses[data[2]] = float(data[3])
        except:
            pass
        
    return atomicMasses

def readTOPs(topodir):
    ''' read topology files in the given directory and return a dictionary of atomic masses '''
    massDict = {}
    massList = [atomicMass(topodir + topofile) for topofile in os.listdir(topodir)]
    for i in range(len(massList)):
        massDict = {**massDict, **massList[i]}
    return massDict

def showMolecule(display = False):
    missing = 0
    for atom in molecule:
        try:
            atom.append(massDict[atom[0]])  # atom[0] => atom name
        except:
            atom.append(0)  # 0 => no mass information
            missing += 1
        if display:
            print(f'{atom[0]}\t{atom[-1]}\t{atom[1:4]}')
    print(f'\npath: {topodir + topofile}')
    print(f'total: {len(molecule)} atoms')
    print(f'missing: {missing} atoms\n')

if __name__ == "__main__":
    import os
    topodir = './topology/'
    pdbpath = './pdb/receptor5_Pemirolast.pdb'
    
    
    molecule = atomicCoor(pdbpath)[0]  # list

    for topofile in os.listdir(topodir):
        massDict = atomicMass(topodir + topofile)
        showMolecule(0)

    # massDict = readTOPs(topodir)
    # showMolecule(1)
    
    # for atom in molecule:
    #     print(atom)
    
    # for atom in massDict.keys():
    #     print(f'{atom}: {massDict[atom]}')
