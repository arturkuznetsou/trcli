def empty_and_comments(x):
	return x and not x.lstrip().startswith('#')

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
        newformt.append(1/float(tpm[1]))
        newformt.append(float(tpm[2]))
        newret.append(newformt)
    return newret
