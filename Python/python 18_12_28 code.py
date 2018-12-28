# Naive_Bayes Classifier 통계적 이론 사용(조건부 확률, 베이즈 정리)

from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')

train = [('I like you', 'pos'),
         ('I hate you', 'neg'),
         ('you like me', 'neg'),
         ('I like her', 'pos')]


all_words = set(word.lower() for sentence in train for word in word_tokenize(sentence[0]))

print(all_words)

b = list(a for i in range(5) for a in range(3))
print(b)

t = [({word : (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

print(t)

classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()


test_sen = 'i like MeRui'
test_sen_features = {word.lower() : (word in word_tokenize(test_sen.lower())) for word in all_words}

print(test_sen_features)

predict = classifier.classify(test_sen_features)
print(predict)

