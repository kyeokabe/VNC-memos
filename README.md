#Connect Mac to [corn](https://web.stanford.edu/group/farmshare/) via VNC


##### Executive Summary of [FarmVNC](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/FarmVNC)

###overview
..1. open a terminal on Mac  
  **2.open a new terminal on Mac**  
  **3.open a new**  

**open a terminal on Mac** 
```
ssh <SUID>@corn.stanford.edu
<enter SUID PW>
<double authentication>
vncpasswd
module load farmvnc
farmvnc
farmvnc 1440x900
```
This should output the following screen:  
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/farmVNC.png" width="350">

**open a new terminal on Mac**

```
ssh -L 5901:localhost:XYZW<SUID>@cornPQ.stanford.edu
yes
<enter SUID PW>
<double authentication>
```
**open [Screen Sharing](https://osxdaily.com/2013/04/05/vnc-client-mac-os-x-screen-sharing/)**  
Enter Host:
```
localhost:5901
```
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/ScreenSharing1.png" width="350">  
Enter VNC PW:
```
<enter VNC PW>
```
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/ScreenSharing2.png" width="350">

**The corn VNC should launch on your screen**
