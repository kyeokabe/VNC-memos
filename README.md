# VNC memos

##Connect Mac to corn@stanford via VNC


##### Executive Summary of [FarmVNC](https://web.stanford.edu/group/farmshare/cgi-bin/wiki/index.php/FarmVNC)

open terminal  
<pre>
ssh \<SUID\>@corn.stanford.edu  
\<enter SUID PW\>
\<double authentication\>  
<b>vncpasswd</b> <i>set VNC password if _necessary</i> 
<b>module load farmvnc</b> <i># this loads but does not launch the program</i> 
<b>farmvnc</b> <i># this will show you the resolution options</i>
<b>farmvnc 1440x900</b> <i>launch farmvnc with selected resolution</i>
<\pre>
corn11:~>   
