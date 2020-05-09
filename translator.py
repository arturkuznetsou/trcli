#!/usr/bin/env python3


from googletrans import Translator
from google_speech import Speech
import os, sys, shutil, logging, sox, time






def empty_and_comments(x):
	return x and not x.lstrip().startswith('#')

def gen_file(filein, langin, langout, pattern, , fileout, temp = '/tmp', ):

    fileout = filein + '.out.mp3'
    # get input lines
    if filein:
            lines = list(filter(empty_and_comments, open(filein, 'r').readlines()));


    # settle tmp
    temp += '/mvoad-' + str(time.time())
    os.mkdir(temp)


    # translate lines
    t = Translator()
    trs = list(map(lambda x: t.translate(x[0:len(x)-1], src=langin, dest=langout), lines))

    tmpfn = temp + '/mvoad.tmp.wav'
    tmpold = temp + '/mvoad.tmp.dest1.mp3'
    tmpdest = temp + '/mvoad.tmp.dest.mp3'

    for tr in trs:
        untrsname = temp + '/mvoad.src.word.mp3'
        trsname = temp + '/mvoad.dest.word.mp3'
        Speech(tr.origin, langin).save(untrsname)
        Speech(tr.text, langout).save(trsname)

        for item in pattern:
            # sox
            (inter, tmpdest, tmpold) = (tmpdest, tmpold, inter)
            if(item[0]):
                filename = trsname
            else:
                filename = untrsname
            t = sox.Transformer()
            t.tempo(item[1], 's')
            t.pad(0, item[2])
            if pattern.index(item) != 0 or trs.index(tr) != 0:
                t.build(filename, tmpfn)
                cbn = sox.Combiner()
                cbn.build([tmpdest, tmpfn], tmpold, 'concatenate')
            else:
                t.build(filename, tmpold)

    dest = fileout
    os.system('mv ' + tmpold + ' ' +  dest)
gen_file(sys.argv[1], 'nl', 'en', [[True, 0.50, 2], [False, 1.50, 2], [False, 1.50, 2]])
