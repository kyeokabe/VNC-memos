# VNC memos

##Connect Mac to corn@stanford via VNC


##### Executive Summary of [FarmVNC](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/FarmVNC)

open terminal  
```
ssh <SUID>@corn.stanford.edu  
<enter SUID PW>
<double authentication>  

corn11:~> vncpasswd <i># set VNC password if _necessary_* </i> 
corn11:~> module load farmvnc *# this loads but does not launch the program*  
corn11:~> farmvnc *# this will show you the resolution options*  
corn11:~> farmvnc 1440x900 *launch farmvnc with selected resolution*
```
corn11:~>   
