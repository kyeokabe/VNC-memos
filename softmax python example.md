**i)**  on paper, write the mathematical equation governing the relation between inputs  
        and outputs
    
**ii)**   on paper, write the corresponding computational graph. clearly identify every  
      branching or operations being performed on tensors (arrays)
     
**iii)**  assign a name to every edges (lines), and write the corresponding tensor dimensions  
    
**FORWARD PROP:**  
**iv)**  starting from the input(s), write step by step the corresponding FORWARD PROP  
      operations. it is good practice to denote step numbers in the comments for every step.
      to avoid broadcasting errors, it is recommended to stay consistent with tensor shapes
      specifically, tensors with shape (m,) should be reshaped to a shape of (m,1).
      be careful especially when doing summations. use keepdims=True option for np.sum()
     
**unintentional broadcasting examples:**
```python
a.shape=(m,1)
b.shape=(m,)
c.shape=(m,1)

bad=a/b                #a treated as a column vector, b treated as a row vector
>>bad.shape=(m,m)     #unintentional broadcasting
fail=a/b.T             #(m,) shapes cannot be transposed
>>fail.shape=(m,m)    #unintentional broadcasting
ok=(a.T/b).T
>>ok.shape=(m,1)      #correct, but complicated
better=a/c
>>better.shape=(m,1)  #correct, simple & easy to follow
```


  **v)**  for modularized code, if necessary, store variables in cache using a tuple or dictionary.
      If the function returns just a forward prop, return the loss (and depending on situations,
     the cache as well). If a separate function is called for back prop, unpack the cache at the
     beginning of the function
         
**BACK PROP:**  
**vi)**  
         starting from the output, write step by step the corresponding BACK PROP operations.
         comment step numbers and dimensions of tensors for legibility. Note that if tensor Z has
         shape (m,n), dL/dZ (commonly abbreviated as dZ) will and should also have shape (m,n).
         when all steps are covered, you should have calculated output gradients with respect to 
         all inputs. finally, return necessary data


```python
#notes: let X: input with shape (N,D), W: weights with shape=(D,C)

#Defining frequently used constants
N=X.shape[0]
D,C=W.shape
```
    
    

###FORWARD PROP ###

  
```python
#branch 1    W1.shape=W2.shape=(D,C)
W1=W2=W

#operation 1    W3.shape=(D,C)
W3=W2**2

#operation 2    W4.shape=()
W4=np.sum(W3)

#operation 3    R.shape=()
R=0.5*reg*W4

#operation 4    a.shape=(N,C)
a=X.dot(W1)

#branch 2    c.shape=b.shape=(N,C)
c=b=a

#operation 5    d.shape=()
d=np.max(c)

#operation 6    f.shape=(N,C)
f=b-d

#branch 3    g.shape=k.shape=(N,C)
g=k=f

#operation 7    m.shape=(N,1)
#without reshape will result in m.shape=(N,)
#this will cause broadcast to mess up in step 11
m=np.reshape(k[np.arange(0,N),y],(N,-1))              #this step is difficult!

#operation 8    h.shape=(N,C)
h=np.exp(g)

#operation 9    i.shape=(N,1)  
i=np.sum(h, axis=1, keepdims=True)

#operation 10    j.shape=(N,1)
j=np.log(i)

#operation 11    gamma.shape=(N,1)
gamma=j-m

#operation 12    beta.shape=()
beta=np.sum(gamma, axis=0)

#operation 13    alpha.shape=()
alpha=beta/float(N)

#operation 14    loss.shape=()
loss=R+alpha
  ```  
  
###BACK PROP 
```python

#operation 14    dalpha.shape=(), dR.shape=()
dalpha=1.0 #branch 1
dR=1.0      #branch 2

#operation 13    dbeta.shape=()
dbeta=dalpha/float(N)
    
#operation 12    dgamma.shape=(N,1)
#dgamma=np.array([dbeta,]*N)  #alternative fancy method
dgamma=dbeta*np.ones((N,1))
    
#operation 11    dm.shape=(N,1), dj.shape=(N,1)
dm=-dgamma
dj=dgamma
        
#operation 10    di.shape=(N,1)
di=dj/i
        
#operation 9    dh.shape=(N,C)
dh=di*np.ones((N,C))
    
#operation 8    dg.shape=(N,C)
dg=dh*np.exp(g)
    
#operation 7    dk.shape=(N,C)    
temp=np.zeros((N,C))
temp[np.arange(N),y]=1.0
dk=dm*temp                                            #this step is difficult!
    
#branch 3    df.shape=(N,C)
df=dg+dk
    
#operation 6    db.shape=(N,C), dd.shape=()
db=df
dd=-np.ones((1,N)).dot(df).dot(np.ones((C,1))) #two dimensional broadcasting!
    
#operation 5    dc.shape=(N,C)
temp2=np.zeros(N*C)
temp2[np.argmax(c)]=1.0
temp2=temp2.reshape((N-1)) #temp2 is a (N,C) zeros matrix with max_index of c = 1.0
dc=dd*temp2
    
#branch 2    da.shape=(N,C)
da=db+dc #note that you can omit adding dc to da. check red notebook p.12 for proof
    
#operation 4    dX.shape=(N,D), dW1.shape=(D,C)
dX=da.dot(W.T)    #branch 1
dW1=X.T.dot(da)    #branch 2
    
#operation 3    dR.shape=()
dW4=dR*0.5*reg
    
#operation 2    dW3.shape=(D,C)
dW3=dW4*np.ones((D,C))
    
#operation 1    dW2.shape=(D,C)
dW2=dW3*2*W2
    
#branch 1
dW=dW1+dW2

```
