from googletrans import Translator
from google_speech import Speech
import os, sys, shutil, logging, sox, time, getopt, other, re

def gen_text(filein, langin, langout):
    # get input lines
    fl = open(filein, 'r').read()
    fl = re.sub('[\n\t ]+', '\n', fl)
    fl = fl.split('\n')
    del fl[-1]
    # translate lines
    t = Translator()

    tr = []
    for line in fl:
        tr.append(t.translate(line, langin, langout))

    return tr


#Takes a google Translated object as input
def gen_audio_file(trs, langin, langout, pattern, fileout):

    temp = '/tmp'
    # settle tmp
    temp += '/mvoad-' + str(time.time())
    os.mkdir(temp)

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
            inter = tmpdest
            tmpdest = tmpold
            tmpold = inter
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
    shutil.move(tmpold, fileout)
    shutil.rmtree(temp)
