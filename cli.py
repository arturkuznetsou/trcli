#!/usr/bin/env python3
import getopt, sys, other
import translate as tr
gen_aud_file = True
lang_in = 'nl'
lang_out = 'en'

args, opts = getopt.getopt(sys.argv[1:], 'ti:d:')
for arg, value in args:
    if arg == '-i':
        if value == '':
            sys.exit(-1)
        lang_in = value
    elif arg == '-d':
        if value == '':
            sys.exit(-1)
        lang_out = value
    elif arg == '-t':
        gen_aud_file = False

if len(opts) < 2 and not gen_aud_file or len(opts) == 0:
    sys.exit('Too few positional arguments.')

trans = tr.gen_text(lang_in, lang_out, opts[1])
frmt = other.gen_format(opts[0])
tr.gen_audio_file(trans, frmt, lang_in, lang_out)
