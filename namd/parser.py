def readfile(path):
    ''' retrieve the x, y, z coordinates of every atoms in the molecule '''
    with open(path, 'r') as ifile:
        raw = ifile.readlines()
    
    for data in raw:
        data = data.split()
        atype = data[0]
        if atype == 'ATOM':
            atom = data[2]
            x = float(data[6])
            y = float(data[7])
            z = float(data[8])
            print(f'{atom}\t{x}\t{y}\t{z}')
        elif atype == 'HETATM':
            atom = data[2]
            x = float(data[5])
            y = float(data[6])
            z = float(data[7])
            print(f'{atom}\t{x}\t{y}\t{z}')


if __name__ == "__main__":
    readfile('./receptor5_Pemirolast.pdb')