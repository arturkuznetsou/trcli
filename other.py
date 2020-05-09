import sys
defaultformat = [[False, 1, 1], [True, 1.5, 1]]
def gen_format (formatstring):
    newret = []
    formats = formatstring.split('/')
    for formt in formats:
        newformt = []
        tpm = formt.split(',')
        if len(tpm) != 3:
            sys.exit('Output format specified incorrectly')
        if tpm[0] == 't':
            newformt.append(True)
        else:
            newformt.append(False)
        try:
            newformt.append(1/float(tpm[1]))
            newformt.append(float(tpm[2]))
            newret.append(newformt)
        except:
            print('Format specified incorrectly. Using default format.')
            return defaultformat
    return newret
