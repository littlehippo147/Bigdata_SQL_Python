# hello_rnn
# 'hihello' --> 'ihello'

import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

idx2char = ['h','i','e','l','o'] # 문자를 인덱스로 접근 가능

x_data =[[0,1,0,2,3,3]] # 'hihell', (1,6)

x_one_hot = [[[1,0,0,0,0], # 0: h
              [0,1,0,0,0], # 1: i
              [1,0,0,0,0], # 0: h
              [0,0,1,0,0], # 2: e
              [0,0,0,1,0], # 3: l
              [0,0,0,1,0], # 3: l
              ]]         #   (1,6,5)
y_data = [[1,0,2,3,3,4]] # 'ihello'  (1,6)

nb_classes = 5  # 5개의 문자
input_dim = 5   # input data(x_data) 의 one_hot size
hidden_size = 5 # output from the LSTM, one_hot size
batch_size = 1  # input data(x_data) 의 sentence 갯수
sequence_length = 6 # 'ihello' : 6

learning_rate = 0.1

#  입력변수 : X,Y
X = tf.placeholder(tf.float32,shape=[None,sequence_length,input_dim])
Y = tf.placeholder(tf.int32,shape=[None,sequence_length])

# LSTM cell, RNN
cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size,state_is_tuple=True)
initial_state = cell.zero_state(batch_size,tf.float32)
outputs,_states = tf.nn.dynamic_rnn(cell,X,initial_state=initial_state,\
                                    dtype=tf.float32)
# print(outputs) # (1,6,5)

# FC layer
X_for_fc = tf.reshape(outputs,[-1,hidden_size])
# print(X_for_fc) # (6,5) * (5,5) = (6,5)
outputs = tf.contrib.layers.fully_connected(inputs=X_for_fc,num_outputs= \
                                            nb_classes,activation_fn=None)
# print(outputs) # (6,5)

# sequence_loss
outputs = tf.reshape(outputs,[batch_size,sequence_length,nb_classes]) # (1,6,5)
weights = tf.ones([batch_size,sequence_length]) # (1,6)
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs,targets=Y,\
                                                 weights=weights )
loss = tf.reduce_mean(sequence_loss)

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction =tf.argmax(outputs,axis=2) # (1,6)

# start training
with tf.Session() as sess:  # sess = tf.Session()--> sess.close()
    sess.run(tf.global_variables_initializer())
    for i in range(50):
        l,_ = sess.run([loss,train],feed_dict={X:x_one_hot,Y:y_data})
        result =sess.run(prediction,feed_dict={X:x_one_hot})
        print(i,"loss:",l,"prediction: ",result,"true Y:",y_data)

        # print char using dic
        # np.squeeze() : 차원을 축소하는 함수, [[1 0 2 3 3 4]] --> [1 0 2 3 3 4]
        # expand_dims() : 차원을 늘리는 함수
        result_str = [idx2char[c] for c in np.squeeze(result)] #['i', 'h', 'e', 'l', 'l', 'o']
        print("\tPrediction str:","".join(result_str))         # ihello

#############################################################################
# '안녕하세요'--> '녕하세요'

tf.set_random_seed(777)
x_data = [[0,1,0,2,3,3]] # 'hihell' , (1,6)

x_one_hot = [[[1,0,0,0,0], # 0: h
              [0,1,0,0,0], # 1: i
              [1,0,0,0,0], # 0: h
              [0,0,1,0,0], # 2: e
              [0,0,0,1,0], # 3: l
              [0,0,0,1,0], # 3: l
              ]]         #   (1,6,5)
y_data = [[1,0,2,3,3,4]] # 'ihello'  (1,6)

nb_classes = 5  # 5개의 문자
input_dim = 5   # input data(x_data) 의 one_hot size
hidden_size = 5 # output from the LSTM, one_hot size
batch_size = 1  # input data(x_data) 의 sentence 갯수
sequence_length = 6 # 'ihello' : 6
""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Lab-02 : 안녕하세요
# '안녕하세'--> '녕하세요'
idx2char = ['안','녕','하','세','요'] # 문자를 인덱스로 접근 가능
x_data = [[0,1,2,3]] # '안녕하세'' , (1,4)

x_one_hot = [[[1,0,0,0,0], # 0: 안
              [0,1,0,0,0], # 1: 녕
              [0,0,1,0,0], # 2: 하
              [0,0,0,1,0], # 3: 세
             ]]         #   (1,4,5)
y_data = [[1,2,3,4]] #   (1,4) , '녕하세요'

nb_classes = 5  # 5개의 문자
input_dim = 5   # input data(x_data) 의 one_hot size
hidden_size = 5 # output from the LSTM, one_hot size
batch_size = 1  # input data(x_data) 의 sentence 갯수
sequence_length = 4 # '녕하세요' : 4

""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Lab-03 : '메리크리스마스'
idx2char = ['메','리','크','스','마']
x_data = [[0,1,2,1,3,4]] # '메리크리스마' , (1,6)

x_one_hot = [[[1,0,0,0,0], # 0: 메
              [0,1,0,0,0], # 1: 리
              [0,0,1,0,0], # 2: 크
              [0,1,0,0,0], # 1: 리
              [0,0,0,1,0], # 3: 스
              [0,0,0,0,1], # 4: 마
              ]]         #   (1,6,5)
y_data = [[1,2,1,3,4,3]] # '리크리스마스'  (1,6)

nb_classes = 5  # 5개의 문자
input_dim = 5   # input data(x_data) 의 one_hot size
hidden_size = 5 # output from the LSTM, one_hot size
batch_size = 1  # input data(x_data) 의 sentence 갯수
sequence_length = 6 # '리크리스마스' : 6

""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Lab-04 : '손을잡을래요'
idx2char = ['손','을','잡','래','요']
x_data = [[0,1,2,1,3]] # '손을잡을래' , (1,5)

x_one_hot = [[[1,0,0,0,0], # 0: 손
              [0,1,0,0,0], # 1: 을
              [0,0,1,0,0], # 2: 잡
              [0,1,0,0,0], # 1: 을
              [0,0,0,1,0], # 3: 래
              ]]         #   (1,5,5)
y_data = [[1,2,1,3,4]] # '을잡을래요'  (1,5)

nb_classes = 5  # 5개의 문자
input_dim = 5   # input data(x_data) 의 one_hot size
hidden_size = 5 # output from the LSTM, one_hot size
batch_size = 1  # input data(x_data) 의 sentence 갯수
sequence_length = 5 # '을잡을래요' : 5

""""""""""""""""""""""""""""""""""""""""""""""""""""""
learning_rate = 0.1

#  입력변수 : X,Y
X = tf.placeholder(tf.float32,shape=[None,sequence_length,input_dim])
Y = tf.placeholder(tf.int32,shape=[None,sequence_length])

# LSTM cell, RNN
cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size,state_is_tuple=True)
initial_state = cell.zero_state(batch_size,tf.float32)
outputs,_states = tf.nn.dynamic_rnn(cell,X,initial_state=initial_state,\
                                    dtype=tf.float32)
# print(outputs) # (1,6,5)

# FC layer
X_for_fc = tf.reshape(outputs,[-1,hidden_size])
# print(X_for_fc) # (6,5) * (5,5) = (6,5)
outputs = tf.contrib.layers.fully_connected(inputs=X_for_fc,num_outputs= \
                                            nb_classes,activation_fn=None)
# print(outputs) # (6,5)

# sequence_loss
outputs = tf.reshape(outputs,[batch_size,sequence_length,nb_classes]) # (1,6,5)
weights = tf.ones([batch_size,sequence_length]) # (1,6)
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs,targets=Y,\
                                                 weights=weights )
loss = tf.reduce_mean(sequence_loss)

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction =tf.argmax(outputs,axis=2) # (1,6)

# start training
with tf.Session() as sess:  # sess = tf.Session()--> sess.close()
    sess.run(tf.global_variables_initializer())
    for i in range(50):
        l,_ = sess.run([loss,train],feed_dict={X:x_one_hot,Y:y_data})
        result =sess.run(prediction,feed_dict={X:x_one_hot})
        print(i,"loss:",l,"prediction: ",result,"true Y:",y_data)

        # print char using dic
        # np.squeeze() : 차원을 축소하는 함수, [[1 0 2 3 3 4]] --> [1 0 2 3 3 4]
        # expand_dims() : 차원을 늘리는 함수
        result_str = [idx2char[c] for c in np.squeeze(result)] #['i', 'h', 'e', 'l', 'l', 'o']
        print("\tPrediction str:","".join(result_str))         # ihello

#################################
tf.set_random_seed(777)
        
sentence = ("if you want to build a ship, don't drum up people together to "
            "collect wood and don't assign them tasks and work, but rather "
            "teach them to long for the endless immensity of the sea.")

char_set = list(set(sentence)) # 25개 문자 사용
char_dic = {w : i for i,w in enumerate(char_set)}
print(len(char_set), char_set)
print(char_dic)

# hyper parameters
data_dim = len(char_set) # 25
hidden_size = len(char_set) # 25
num_classes = len(char_set) # 25
sequence_length = 10  # 임의로 설정

learning_rate = 0.1

# x_data, y_data, X,Y 입력변수
dataX = []
dataY = []
for i in range(len(sentence) - sequence_length):  # 180 - 10 --> 170
    x_str = sentence[i:i+sequence_length]       # "if you wan"
    y_str = sentence[i+1:i+sequence_length + 1] # "f you want"
    print(i,x_str,'->',y_str)

    x = [char_dic[c] for c in x_str]
    y = [char_dic[c] for c in y_str]
    # print('x:',x)
    # print('y:',y)

    dataX.append(x)
    dataY.append(y)

# print(dataX) # (170,10)
# print(dataY) # (170,10)

batch_size = len(dataX) # 170

X = tf.placeholder(tf.int32,[None,sequence_length]) # (?,10)
Y = tf.placeholder(tf.int32,[None,sequence_length]) # (?,10)

X_one_hot = tf.one_hot(X,num_classes)
# print(X_one_hot) # (?,10,25)

# Stacked RNN :  2 RNN layer
cell = tf.contrib.rnn.BasicLSTMCell(hidden_size,state_is_tuple =True)
multi_cells = tf.contrib.rnn.MultiRNNCell([cell]*2,state_is_tuple =True)
# initial_state = cell.zero_state(batch_size,tf.float32)
outputs,_states = tf.nn.dynamic_rnn(multi_cells,X_one_hot,dtype=tf.float32)
# print(outputs) # (?,10,25)
# print(multi_cells)

# def lstm_cell():
#     cell = tf.contrib.rnn.BasicLSTMCell(hidden_size, state_is_tuple=True)
#     return cell
#
# multi_cells = tf.contrib.rnn.MultiRNNCell([lstm_cell() for _ in range(2)],state_is_tuple =True)
# outputs,_states = tf.nn.dynamic_rnn(multi_cells,X_one_hot,dtype=tf.float32)
# print(multi_cells)

# FC layer
X_for_fc = tf.reshape(outputs,[-1,hidden_size]) # (?,25)
# print(X_for_fc) # (?,25) * (25,25) = (?,25)
outputs = tf.contrib.layers.fully_connected(inputs=X_for_fc,num_outputs= \
                                            num_classes,activation_fn=None)
print(outputs) # (?,25)

# sequence_loss
outputs = tf.reshape(outputs,[batch_size,sequence_length,num_classes]) # (170,10,25)
weights = tf.ones([batch_size,sequence_length]) # (170,10)
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs,targets=Y,\
                                                 weights=weights )
loss = tf.reduce_mean(sequence_loss)

train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction =tf.argmax(outputs,axis=2) # (170,10,25) -> (170,10)

# start training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1500):
        l,_ = sess.run([loss,train],feed_dict={X:dataX,Y:dataY})
        results = sess.run(prediction,feed_dict={X:dataX}) # (170,10)

        for j,index in enumerate(results):
            print(i,j,l,''.join([char_set[t] for t in index]))


    # all data
    results = sess.run(prediction, feed_dict={X: dataX})  # (170,10)
    for j,index in enumerate(results):
        if j == 0:
            print(''.join([char_set[t] for t in index]),end='')
        else :
            print(char_set[index[-1]],end='')

        # t you want to build a ship, don't drum up people together to
        # collect wood and don't assign them tasks and work, but rather
        # teach them to long for the endless immensity of the sea.