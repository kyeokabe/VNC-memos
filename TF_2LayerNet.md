[**[ArXiv Paper](http://arxiv.org/abs/1603.04467)**]
[**[TF Notes](https://github.com/samjabrahams/tensorflow-white-paper-notes)**]
[**[TF Examples](https://github.com/pkmital/tensorflow_tutorials)**]
[**[TF Examples2](https://github.com/nlintz/TensorFlow-Tutorials)**]
[**[TF API](https://www.tensorflow.org/versions/r0.8/api_docs/python/index.html)**]
###overview of steps
**1. Download and run TF_2LayerNet.py**  
**2. *Activate* TensorBoard**  
**3. *View* TensorBoard**  

**Environments:**  
>Macbook Pro 15" Mid 2012  
>OSX 10.11.3  
>Anaconda ver. 2.5.0 (x86_64)  
>Python ver. 2.7.11  
>Numpy ver. 1.11.0  
>TensorFlow r0.8 (OSX, CPU only)  
>Google Chrome ver. 50.0.2661.86 (64-bit)  

**1.**  
Download [TF_2LayerNet.py](https://github.com/kyeokabe/notes/blob/master/TF_2LayerNet.py) and place it in an appropriate directory
  
Open terminal  
Change directory to where TF_2LayerNet.py is stored  
run TF_2LayerNet.py  
```
cd <TF_2LayerNet directory>  
python TF_2LayerNet.py  
```
the output should look like  

<img src="https://github.com/kyeokabe/notes/blob/master/pics/TF_2LayerNet_Output.png" width="500">  

**2.**  
To *activate* TensorBoard, enter the following in terminal:  
(change */tmp/fc_logs* accordingly if you change the source code )
```
tensorboard --logdir=/tmp/fc_logs    
```
The output should look like:  
<img src="https://github.com/kyeokabe/notes/blob/master/pics/TB.png" width="500">  
  
**3.**  
To *view* TensorBoard, open a Chrome browser and enter the following in the address bar:  

```
http://0.0.0.0:6006  
```
<img src="https://github.com/kyeokabe/notes/blob/master/pics/address_bar.png" width="850">  

You should now be able to navigate through the Graph, Events and Histograms  
  
**Graph**  
<img src="https://github.com/kyeokabe/notes/blob/master/pics/TF_2LayerNet_Graphs.png" width="850">  
  
**Events**  
<img src="https://github.com/kyeokabe/notes/blob/master/pics/TF_2LayerNet_Events.png" width="850">  
  
**Histrograms**  
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/TF_2LayerNet_Histrograms.png" width="850">  
