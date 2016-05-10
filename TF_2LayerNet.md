**Environments:**  
>Macbook Pro 15" Mid 2012  
>OSX 10.11.3  
>TensorFlow r0.8 (OSX, CPU only)  
>Google Chrome ver. 50.0.2661.86 (64-bit)  
  
open terminal  
change directory to where TF_2LayerNet.py is stored  
run TF_2LayerNet.py  
```
cd <TF_2LayerNet directory>  
python TF_2LayerNet.py  
```
the output should look like  

<img src="https://github.com/kyeokabe/notes/blob/master/pics/TF_2LayerNet_Output.png" width="500">  

To *activate* TensorBoard, enter the following in terminal:  
```
tensorboard --logdir=/tmp/fc_logs    
```
The output should look like:  
<img src="https://github.com/kyeokabe/notes/blob/master/pics/TB.png" width="500">  
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
