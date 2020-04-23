#!/usr/bin/env python3
import getopt, sys, other
import translate as tr
gen_aud_file = True

opts, args = getopt.getopt(sys.argv[1:], 'to:')

if len(args) < 2:
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



trans = tr.gen_text(args[-1], langin, langout)
pattern = other.gen_format(args[-3])
tr.gen_audio_file(trans, langin, langout, pattern, fileout)
