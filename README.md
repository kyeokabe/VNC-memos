# VNC memos

## making a VNC connection from a Mac to corn@stanford (Ubuntu)


##### Executive Summary of [FarmVNC](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/FarmVNC)

open terminal  
ssh SUID@corn.stanford.edu 
*enter SUID PW*  
*double authentication*  

`ssh <SUID>@corn.stanford.edu <br /> 
enter SUID PW>  <br />
<double authentication>  <br />
corn11:~> vncpasswd # set VNC password if necessary'  
corn11:~> module load farmvnc # this loads but does not launch the program  
corn11:~> farmvnc # this will show you the resolution options  
corn11:~> farmvnc 1440x900`  

corn11:~>   
