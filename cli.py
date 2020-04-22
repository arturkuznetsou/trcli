#!/usr/bin/env python3
import getopt, sys, other
import translate as tr
gen_aud_file = True

try:
    opts, args = getopt.getopt(sys.argv[1:], 'to:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

filein = args[-1]
fileout = filein + '.out.mp3'
langin = args[-2].split('-')[0]
langout = args[-2].split('-')[1]

for arg, value in opts:
    if arg == '-t':
        gen_aud_file = False
    elif arg == '-o':
        fileout = value

if len(args) < 2 and not gen_aud_file or len(args) == 0:
    sys.exit('Too few positional arguments.')


trans = tr.gen_text(args[-1], langin, langout)
pattern = other.gen_format(args[-3])
tr.gen_audio_file(trans, langin, langout, pattern, fileout)
