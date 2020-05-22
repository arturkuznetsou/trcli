import getopt, sys, other
import translate as tr
gen_aud_file = True

try:
    opts, args = getopt.getopt(sys.argv[1:], 'hto:')
except Exception as error:
    sys.exit("An error occured. " + str(error))

if len(args) < 3:
    sys.exit('Too few positional arguments. trscli <format> <input language>-<output language> <file>.')

filein = args[-1]
fileout = filein + '.out.mp3'
langin = args[-2].split('-')[0]
langout = args[-2].split('-')[1]

for arg, value in opts:
    if arg == '-t':
        gen_aud_file = False
    elif arg == '-o':
        fileout = value




pattern = other.gen_format(args[-3])
try:
    trans = tr.gen_text(args[-1], langin, langout)
except Exception as error:
    sys.exit(error)

try:
    tr.gen_audio_file(trans, langin, langout, pattern, fileout)
except Exception as error:
    sys.exit(error)
