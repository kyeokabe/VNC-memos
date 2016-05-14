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
