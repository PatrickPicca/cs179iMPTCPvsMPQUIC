# cs179iMPTCPvsMPQUIC

All comamnds performed assume you are in a linux environment. 

Before you start:
<br> Verify in your /etc/resolv.conf

Here are the listed instructions followed to run the MPTCP:
1. sudo apt update
2. sudo apt install mptcpize
3. In a mininet xterm for your desired server host, run the following command:
    <br>mptcpize run -d python3 ./server.py
4. In a mininet xterm for your desired client host, run the following command:
    <br>mptcpize run -d python3 ./client.py

The mptcpize command forces the any TCP socket program to run MPTCP on top of the process.


Here are the listed instructions followed to run the MPQUIC:
1. In an directory adjacent to this one run: 
       <br> git clone --recursive https://github.com/cloudflare/quiche
2. sudo apt install cmake
       <br> Default installation
       <br> Rust version 1.70.0
3. sudo apt install cargo
4. source $HOME/.cargo/env
5. cd quiche
6. In the apps/src/bin folder of quiche, please transfer any files you wish for your MPQUIC server to provide.
7. cargo test
    <br> This will build a number of supported packages for quiche
8. 
