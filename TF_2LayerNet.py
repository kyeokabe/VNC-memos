#This example was taken from Stanford CS231n Winter2016 Lecture 12 slide 131
#http://cs231n.stanford.edu/slides/winter1516_lecture12.pdf

import tensorflow as tf
import numpy as np

N, D, H, C = 64, 1000, 100, 10

x=tf.placeholder(tf.float32, shape=[None, D], name='x')
y=tf.placeholder(tf.float32, shape=[None, C], name='y')

w1=tf.Variable(1e-3*np.random.rand(D,H).astype(np.float32), name='w1')
w2=tf.Variable(1e-3*np.random.rand(H,C).astype(np.float32), name='w2')

with tf.name_scope('scores') as scope:
  a=tf.matmul(x,w1)
  a_relu=tf.nn.relu(a)
  scores=tf.matmul(a_relu,w2)

with tf.name_scope('loss') as scope:
  probs=tf.nn.softmax(scores)
  loss=-tf.reduce_sum(y*tf.log(probs))

loss_summary=tf.scalar_summary('loss',loss)
w1_hist=tf.histogram_summary('w1',w1)
w2_hist=tf.histogram_summary('w2',w2)

learning_rate=1e-2
train_step=tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

xx=np.random.randn(N,D).astype(np.float32)
yy=np.zeros((N,C)).astype(np.float32)
yy[np.arange(N), np.random.randint(C, size=N)]=1

with tf.Session() as sess:
  merged=tf.merge_all_summaries()
  writer=tf.train.SummaryWriter('/tmp/fc_logs', sess.graph_def)
  sess.run(tf.initialize_all_variables())

  for t in xrange(100):
      summary_str,_,loss_value=sess.run([merged, train_step, loss], feed_dict={x: xx, y: yy})
      writer.add_summary(summary_str, t)
      print loss_value
