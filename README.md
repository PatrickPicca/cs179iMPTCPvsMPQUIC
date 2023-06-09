# cs179iMPTCPvsMPQUIC
MPTCP Vs. MPQUIC

Requirment: 
1. python3.8
2. mininet
3. wireshark
4. curl 

Setting up MPTCP:

Step 1:
           Update packages
- sudo apt update

Step 2: 
          check python version and if MPTCP is already installed.
- python3.8 --versio  
- sudo dmesg| grep mptcp

follow step 3 if you do not have python3 installed for ubuntu. 
skip to step4 if you already have python3

step 3:
            install python3.8
- sudo apt update
- sudo apt install software-properties-common
            Add the deadsnakes PPA to your system’s sources list:
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt install python3.8
    check if python3.8 was installed successfully. 
python3.8 --version

step 4:
Download the .deb files 

wget https://github.com/multipath-tcp/mptcp/releases/download/v0.96/linux-mptcp_v0.96_20230203134326-1_all.deb
 
wget https://github.com/multipath-tcp/mptcp/releases/download/v0.96/linux-libc-dev_20230203134326-1_amd64.deb
 
wget https://github.com/multipath-tcp/mptcp/releases/download/v0.96/linux-image-5.4.230.mptcp_20230203134326-1_amd64.deb
 
wget https://github.com/multipath-tcp/mptcp/releases/download/v0.96/linux-image-5.4.230.mptcp-dbg_20230203134326-1_amd64.deb
  
wget https://github.com/multipath-tcp/mptcp/releases/download/v0.96/linux-headers-5.4.230.mptcp_20230203134326-1_amd64.deb

step 5:
              Install the packages
              
sudo dpkg -i linux-headers-5.4.230.mptcp_20230203134326-1_amd64.deb
 
sudo dpkg -i linux-image-5.4.230.mptcp-dbg_20230203134326-1_amd64.deb 
 
sudo dpkg -i linux-image-5.4.230.mptcp_20230203134326-1_amd64.deb 
 
sudo dpkg -i linux-libc-dev_20230203134326-1_amd64.deb 
 
sudo dpkg -i linux-mptcp_v0.96_20230203134326-1_all.deb 

step 6:
        Reboot your machine 
 sude reboot 
 
 step 7: 
         Test if you have isntalled MPTCP succfully 
         
  - sudo dmesg|grep MPTCP
  -you should get output o
  "[    0.690338] MPTCP: Stable release v0.96"

or 
-  curl http://www.multipath-tcp.org/
- output:
-"Nay, Nay, Nay, your have an old computer that does not speak MPTCP. Shame on you!" if you do not have MPTCP installed correctly 
or 
"Yay, you are MPTCP-capable! You can now rest in peace." if you have MPTCP running on your machine 

step 8(optional):
          first let's install sysctl by running
sudp apt install sysctl
          enable or disable MPTCP as needed
 - Turn is on run:
 sudo sysctl -w net.mptcp.mptcp_enabled=1
 - Turn it off run:
 sudo sysctl -w net.mptcp.mptcp_enabled=2
 or 
 sudo sysctl -w net.mptcp.mptcp_enabled=0 






