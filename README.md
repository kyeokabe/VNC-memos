# VNC memos

##Connect Mac to corn@stanford via VNC


##### Executive Summary of [FarmVNC](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/FarmVNC)

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

<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/farmVNC.png" width="350">

**open a new terminal on Mac**

```
ssh -L 5901:localhost:XYZW<SUID>@cornPQ.stanford.edu
yes
<enter SUID PW>
<double authentication>
```
**open screen sharing**
```
localhost:5901
```
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/ScreenSharing1" width="350">
```
<enter VNC PW>
```
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/ScreenSharing2" width="350">
