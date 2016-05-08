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

<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/farm_VNC.png" width="350">

**open a new terminal on Mac**

```
ssh -L 5901:localhost:XYZW<SUID>@corn26.stanford.edu
yes
<enter SUID PW>
<double authentication>
```
<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/farm_VNC.png" width="350">

**open screen sharing**

<img src="https://github.com/kyeokabe/VNC-memos/blob/master/pics/farm_VNC.png" width="350">


enter host name
