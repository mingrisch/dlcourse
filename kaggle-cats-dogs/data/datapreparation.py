import os
ff = os.listdir('ttrain')

cats = [el for el in ff if el.startswith('cat')
]
dogs = [ el for el in ff if el.startswith('dog')]

import random
random.shuffle(cats)
random.shuffle(dogs
)

valcats = cats[25:2500]
valdogs = dogs[25:2500]
traincats = cats[2500:]
traindogs = dogs[2500]
traindogs = dogs[2500:]
sampledogs = dogs[:25]
samplecats = cats[:25]

os.mkdir('train')
os.mkdir('valid')
os.mkdir('sample')
os.mkdir('train/cat')
os.mkdir('train/dog')
os.mkdir('valid/dog')
os.mkdir('valid/cat')
os.mkdir('sample/dog')
os.mkdir('sample/cat')

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

ll = sampledogs
target = 'sample/dog'
for el in ll:
    shutil.move(opj('ttrain', el), target)

ll = samplecats
target = 'sample/cat'
for el in ll:
    shutil.move(opj('ttrain', el), target)
