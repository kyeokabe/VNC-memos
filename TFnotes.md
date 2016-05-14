
tensorflow/tensorflow/python/ops/gradients.py
**[back prop](https://github.com/tensorflow/tensorflow/blob/7b4d733593842361d066d7e33a03a07da5dca465/tensorflow/python/ops/gradients.py)**  

tensorflow/tensorflow/python/ops/nn_grad.py
**[ReLU back prop](https://github.com/tensorflow/tensorflow/blob/7b4d733593842361d066d7e33a03a07da5dca465/tensorflow/python/ops/nn_grad.py)**  

line 166:
@ops.RegisterGradient("Relu")
def _ReluGrad(op, grad):
  return gen_nn_ops._relu_grad(grad, op.outputs[0])

**classes**  



tf.image
tf.python_io  

tf.nn  

tf.Session (not superclass)  

tf.errors  

tf.train  
tf.test  

tf.contrib.layers  
tf.contrib.util  



tf.placeholder(dtype, shape=None, name=None)
Inserts a placeholder for a tensor that will be always fed.

Important: This tensor will produce an error if evaluated. Its value must be fed using the feed_dict optional argument to Session.run(), Tensor.eval(), or Operation.run().
