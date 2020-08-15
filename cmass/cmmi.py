def readPDB(pfile):
    ''' read a pdb file and return coordinates of atoms (2D list) '''
    atomicCoor = []     # [[name, x, y, z]]

    with open(pfile, 'r') as ifile:
        rawData = ifile.readlines()
    
    for row in rawData:
        data = row.split()
        if data[0] == 'ATOM':
            atomicCoor.append([data[-1], float(data[6]), float(data[7]), float(data[8])])
    
    return atomicCoor

def readTOP(tfile):
    ''' read a topology file and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}
 
    with open(tfile, 'r') as ifile:
        rawData = ifile.readlines()

    for row in rawData:
        data = row.split()
        try:
            if data[0] == 'MASS':
                atomicMass[data[4]] = float(data[3])
        except:
            pass
        
    return atomicMass

def readTOPs(tdir='./topology'):
    ''' read topology files in tdir and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}

    if tdir[-1] != '/' or '\\':
        tdir += '/'
    
    import os
    for tfile in os.listdir(tdir):
        atomicMass = {**atomicMass, **readTOP(tdir + tfile)}
        
    return atomicMass

#############################################

def createMole(atomicCoor, atomicMass):
    ''' merge atomic mass into coordinates list '''
    molecule = atomicCoor   # [[name, x, y, z, mass]]
    missing = []            # [[name, x, y, z, index]]

    for i in range(len(molecule)):
        atom = molecule[i]
        try:
            atom.append(atomicMass[atom[0]])
        except:
            missing.append([*atom, i])
            atom.append(0)

    return molecule, missing

def calulateCM(molecule):   # [[name, x, y, z, mass]]
    ''' calculate the molecule's center of mass and molecular mass'''
    cenMass = [0, 0, 0]     # [x, y, z]
    totMass = 0

    for atom in molecule:
        totMass += atom[4]
        for i in range(len(cenMass)):
            cenMass[i] += atom[i + 1] * atom[4]
    
    for i in range(len(cenMass)):
        cenMass[i] /= totMass
    
    return cenMass, totMass

def calculateMI(molecule, cenMass):   # [[name, x, y, z, mass]]
    angMass = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for atom in molecule:
        x = [atom[1] - cenMass[0], atom[2] - cenMass[1], atom[3] - cenMass[2]]
        for i in range(3):
            for j in range(3):
                delta = 1 if i == j else 0
                r2 = x[0] ** 2 + x[1] ** 2 + x[2] ** 2
                angMass[i][j] = atom[4] * (r2 * delta - x[i] * x[j])

    return angMass

#############################################

def printList(List):
    ''' print 2D list '''
    for line in List:
        for data in line:
            print(data, end='\t')
        print()

def printDict(Dict):
    ''' print key-value pairs line by line '''
    for key in Dict.keys():
        print(f'{key}\t{Dict[key]}')

def printMole(molecule, limit=-1):    # [[name, x, y, z, mass]]
    ''' print the atoms list of a molecule by the given format '''
    print(f'name\tmass\t\tcoordinates')
    for atom in molecule:
        print(f'{atom[0]}\t{atom[4]}\t\t{atom[1:4]}')
        limit -= 1
        if not limit: break
    print(f'molecule: {len(molecule)} atoms')

def printMiss(missing, limit=-1):     # [[name, x, y, z, index]]
    ''' print the missing atoms in a molecule '''
    if missing:
        print(f'name\tindex\tcoordinates')
        for atom in missing:
            print(f'{atom[0]}\t{atom[4]}\t{atom[1:4]}')
            limit -= 1
            if not limit: break
    print(f'missing: {len(missing)} atoms')

def printCM(cenMass, totMass=0, precision=4):
    ''' print center of mass and molecular mass with given presicion '''
    form = f'.{precision}f'
    print(f'center of mass: [{cenMass[0]:{form}}, {cenMass[1]:{form}}, {cenMass[2]:{form}}]')
    if totMass: print(f'molecular mass: {totMass:{form}}')

def printMI(angMass, precision=4):
    form = f'>10.{precision}f'
    print(f'moment of inertia:')
    for row in angMass:
        for col in row:
            print(f'{col:{form}}', end='')
        print()

#############################################

def testPrint():
    printList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print()
    printDict({'A': 4, 'B': 5, 'C': 6})
    print()
    printMole([[1, 4, 5, 3, 2], [3, 5, 2, 0, 8], [7, 1, 2, 4, 9]])

def testTOP(tdir='./topology/', tfile='top_all22_prot.rtf'):
    print(f'read a single topology file: {tdir + tfile}')
    printDict(readTOP(tdir + tfile))
    print(f'\nread topology files in directory: {tdir}')
    printDict(readTOPs(tdir))

def testPDB(pdir='./pdb/', pfile='receptor5_Pemirolast.pdb'):
    printList(readPDB(pdir + pfile))

def testMole():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)

    printMole(molecule, 18)
    print()
    printMiss(missing)

def testCM():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)
    cenMass, totMass = calulateCM(molecule)
    printCM(cenMass, totMass)

def testMI():
    coor = readPDB('./pdb/receptor5_Pemirolast.pdb')
    mass = readTOPs('./topology/')
    molecule, missing = createMole(coor, mass)
    cenMass, totMass = calulateCM(molecule)
    angMass = calculateMI(molecule, cenMass)
    printMI(angMass)

#############################################

def main(pfile='./pdb/receptor5_Pemirolast.pdb', tdir='./topology/'):
    coor = readPDB(pfile)
    mass = readTOPs(tdir)
    molecule, missing = createMole(coor, mass)

    cenMass, totMass = calulateCM(molecule)
    printCM(cenMass, totMass)
    
    angMass = calculateMI(molecule, cenMass)
    printMI(angMass)

if __name__ == "__main__":
    import sys, os
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])