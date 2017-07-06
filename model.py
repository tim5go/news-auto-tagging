import fasttext


classifier = fasttext.supervised('train.txt', 'model')
