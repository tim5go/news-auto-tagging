import fasttext

classifier = fasttext.load_model('model.bin')

result = classifier.test('test.txt')

print 'P@1:', result.precision
print 'R@1:', result.recall
print 'Number of examples:', result.nexamples

