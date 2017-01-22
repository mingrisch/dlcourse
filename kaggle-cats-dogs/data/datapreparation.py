import os
ff = os.listdir('ttrain')

cats = [el for el in ff if el.startswith('cat')
]
dogs = [ el for el in ff if el.startswith('dog')]

import random
random.shuffle(cats)
random.shuffle(dogs
)

valcats = cats[50:2500]
valdogs = dogs[50:2500]
traincats = cats[2500:]
traindogs = dogs[2500]
traindogs = dogs[2500:]
samplevaldogs = dogs[25:50]
samplevalcats = cats[25:50]

sampletraindogs = dogs[:25]
sampletraincats = cats[:25]

os.mkdir('train')
os.mkdir('valid')
os.mkdir('sample')
os.mkdir('sample/train')
os.mkdir('sample/valid')

os.mkdir('train/cat')
os.mkdir('train/dog')
os.mkdir('valid/dog')
os.mkdir('valid/cat')
os.mkdir('sample/valid/dog')
os.mkdir('sample/valid/cat')
os.mkdir('sample/train/dog')
os.mkdir('sample/train/cat')

from os.path import join as opj
import shutil


ll = valdogs
target = 'valid/dog'
for el in ll:
    shutil.move(opj('ttrain', el), target)

target = 'valid/cat'
ll = valcats
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = traindogs
target = 'train/dog'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = traincats
target = 'train/cat'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = samplevaldogs
target = 'sample/valid/dog'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = samplevalcats
target = 'sample/valid/cat'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = sampletraindogs
target = 'sample/train/dog'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = sampletraincats
target = 'sample/train/cat'
for el in ll:
    shutil.move(opj('ttrain', el), target)
