# Naive_Bayes_02.py
# 문장의 유사도 측정하기

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df = 1)

contents = ['메리랑 놀러가고 싶지만 바쁜데 어떻하죠?',
            '메리는 공원에서 산책하고 노는 것을 싫어해요',
            '메리는 공원에서 노는 것도 싫어해요. 이상해요.',
            '먼 곳으로 여행을 떠나고 싶은데 너무 바빠서 그러질 못하고 있어요']

X = vectorizer.fit_transform(contents)
n = vectorizer.get_feature_names()
print(n)
# ['것도', '것을', '곳으로', '공원에서', '그러질', '너무', '노는', '놀러가고',
#  '떠나고', '메리는', '메리랑', '못하고', '바빠서', '바쁜데', '산책하고',
# '싫어해요', '싶은데', '싶지만', '어떻하죠', '여행을', '이상해요', '있어요']

print(X.toarray().transpose)
# [[0 0 1 0]
#  [0 1 0 0]
#  [0 0 0 1]
#  [0 1 1 0]
#  [0 0 0 1]
#  [0 0 0 1]
#  [0 1 1 0]
#  [1 0 0 0]
#  [0 0 0 1]
#  [0 1 1 0]
#  [1 0 0 0]
#  [0 0 0 1]
#  [0 0 0 1]
#  [1 0 0 0]
#  [0 1 0 0]
#  [0 1 1 0]
#  [0 0 0 1]
#  [1 0 0 0]
#  [1 0 0 0]
#  [0 0 0 1]
#  [0 0 1 0]
#  [0 0 0 1]]

# X = vectorizer.fit_transform(contents)
# [[0 0 0 0 0 0 0 1 0 0 1 0 0 1 0 0 0 1 1 0 0 0]
#  [0 1 0 1 0 0 1 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0]
#  [1 0 0 1 0 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0]
#  [0 0 1 0 1 1 0 0 1 0 0 1 1 0 0 0 1 0 0 1 0 1]]
num_samples, num_features = X.shape
print(num_samples, num_features)  # (4,22)

new_post = ['메리랑 공원에서 산책하고 놀고 싶어요']
# new_post = ['근처 공원에 메리랑 놀러가고 싶네요.']
new_post_vec = vectorizer.transform(new_post)
print(new_post_vec.toarray())
# [[0 0 0 1 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0]]

import scipy as sp

def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())


best_doc = None
best_dist = 65535
best_i = None

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    d = dist_raw(post_vec, new_post_vec)

    print("== Post %i with dist=%.2f   : %s" % (i, d, contents[i]))

    if d < best_dist:
        best_dist = d
        best_i = i


from konlpy.tag import Twitter
t = Twitter()
contents_tokens = [t.morphs(row) for row in contents]
print(contents_tokens)
# [['메리', '랑', '놀러', '가고', '싶지만', '바쁜데', '어떻하죠', '?'],
# ['메리', '는', '공원', '에서', '산책', '하고', '노', '는', '것', '을', '싫어해요'],
# ['메리', '는', '공원', '에서', '노', '는', '것', '도', '싫어해요', '.', '이상해요', '.'],
# ['먼', '곳', '으로', '여행', '을', '떠나고', '싶은데', '너무', '바빠서', '그러질', '못', '하고', '있어요']]

contents_for_vectorize = []

for content in contents_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word

    contents_for_vectorize.append(sentence)

print(contents_for_vectorize)
# [' 메리 랑 놀러 가고 싶지만 바쁜데 어떻하죠 ?',
#  ' 메리 는 공원 에서 산책 하고 노 는 것 을 싫어해요',
#  ' 메리 는 공원 에서 노 는 것 도 싫어해요 . 이상해요 .',
#  ' 먼 곳 으로 여행 을 떠나고 싶은데 너무 바빠서 그러질 못 하고 있어요']

X = vectorizer.fit_transform(contents_for_vectorize)
n = vectorizer.get_feature_names()
print(n)
# ['가고', '공원', '그러질', '너무', '놀러', '떠나고', '메리', '바빠서',
# '바쁜데', '산책', '싫어해요', '싶은데', '싶지만', '어떻하죠', '에서',
# '여행', '으로', '이상해요', '있어요', '하고']
num_samples, num_features = X.shape
print(num_samples, num_features)  # (4,20)

print(X.toarray().transpose())
# [[1 0 0 0]
#  [0 1 1 0]
#  [0 0 0 1]
#  [0 0 0 1]
#  [1 0 0 0]
#  [0 0 0 1]
#  [1 1 1 0]
#  [0 0 0 1]
#  [1 0 0 0]
#  [0 1 0 0]
#  [0 1 1 0]
#  [0 0 0 1]
#  [1 0 0 0]
#  [1 0 0 0]
#  [0 1 1 0]
#  [0 0 0 1]
#  [0 0 0 1]
#  [0 0 1 0]
#  [0 0 0 1]
#  [0 1 0 1]]

new_post = ['메리랑 공원에서 산책하고 놀고 싶어요']
# new_post = ['근처 공원에 메리랑 놀러가고 싶네요.']
new_post_tokens = [t.morphs(row) for row in new_post]

new_post_for_vectorize = []

for content in new_post_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word

    new_post_for_vectorize.append(sentence)

print(new_post_for_vectorize)
# [' 메리 랑 공원 에서 산책 하고 놀고 싶어요']

new_post_vec = vectorizer.transform(new_post_for_vectorize)
print(new_post_vec.toarray())
#   공원       메리   산책       에서      하고
# [[0 1 0 0 0 0 1 0 0 1 0 0 0 0 1 0 0 0 0 1]]

best_doc = None
best_dist = 65535
best_i = None

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    d = dist_raw(post_vec, new_post_vec)

    print("== Post %i with dist=%.2f   : %s" % (i, d, contents[i]))

    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i, dist = %.2f" % (best_i, best_dist))
print('-->', new_post)
print('---->', contents[best_i])


##############################################

# tf : term frequency , 자주 등장하면 중요도가 증가
# idf : inverse document frequency, 비교하는 모든 문서에 같은 단어가 있다면
#                                   비교에서는 중요한 단어가 아니다

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')

contents_tokens = [t.morphs(row) for row in contents]

contents_for_vectorize = []

for content in contents_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word

    contents_for_vectorize.append(sentence)

X = vectorizer.fit_transform(contents_for_vectorize)
num_samples, num_features = X.shape
print(num_samples, num_features)  # (4,20)

print(X.toarray())
# [[0.43003652 0.         0.         0.         0.43003652 0.
#   0.27448674 0.         0.43003652 0.         0.         0.
#   0.43003652 0.43003652 0.         0.         0.         0.
#   0.         0.        ]
#  [0.         0.39954636 0.         0.         0.         0.
#   0.32346721 0.         0.         0.5067739  0.39954636 0.
#   0.         0.         0.39954636 0.         0.         0.
#   0.         0.39954636]
#  [0.         0.43584673 0.         0.         0.         0.
#   0.35285549 0.         0.         0.         0.43584673 0.
#   0.         0.         0.43584673 0.         0.         0.55281632
#   0.         0.        ]
#  [0.         0.         0.34056989 0.34056989 0.         0.34056989
#   0.         0.34056989 0.         0.         0.         0.34056989
#   0.         0.         0.         0.34056989 0.34056989 0.
#   0.34056989 0.26850921]]
n = vectorizer.get_feature_names()
print(n)
# ['가고', '공원', '그러질', '너무', '놀러', '떠나고', '메리', '바빠서',
#  '바쁜데', '산책', '싫어해요', '싶은데', '싶지만', '어떻하죠', '에서',
#  '여행', '으로', '이상해요', '있어요', '하고']

new_post = ['근처 공원에 메리랑 놀러가고 싶네요.']
# new_post = ['메리랑 공원에서 산책하고 놀고 싶어요']
new_post_tokens = [t.morphs(row) for row in new_post]

new_post_for_vectorize = []

for content in new_post_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word

    new_post_for_vectorize.append(sentence)

print(new_post_for_vectorize)
# [' 근처 공원 에 메리 랑 놀러 가고 싶네요 .']

new_post_vec = vectorizer.transform(new_post_for_vectorize)
print(new_post_vec.toarray())
# [[0.57457953 0.4530051  0.         0.         0.57457953 0.
#   0.36674667 0.         0.         0.         0.         0.
#   0.         0.         0.         0.         0.         0.
#   0.         0.        ]]

def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())

    delta = v1_normalized - v2_normalized

    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = 65535
best_i = None

for i in range(0, num_samples):
    post_vec = X.getrow(i)
    d = dist_norm(post_vec, new_post_vec)

    print("== Post %i with dist=%.2f   : %s" % (i, d, contents[i]))

    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i, dist = %.2f" % (best_i, best_dist))
print('-->', new_post)
print('---->', contents[best_i])

# == Post 0 with dist=0.90   : 메리랑 놀러가고 싶지만 바쁜데 어떻하죠?
# == Post 1 with dist=1.18   : 메리는 공원에서 산책하고 노는 것을 싫어해요
# == Post 2 with dist=1.16   : 메리는 공원에서 노는 것도 싫어해요. 이상해요.
# == Post 3 with dist=1.41   : 먼 곳으로 여행을 떠나고 싶은데 너무 바빠서 그러질 못하고 있어요
# Best post is 0, dist = 0.90
# --> ['근처 공원에 메리랑 놀러가고 싶네요.']
# ----> 메리랑 놀러가고 싶지만 바쁜데 어떻하죠?
