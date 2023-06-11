# cs179iMPTCPvsMPQUIC

All comamnds performed assume you are in a linux environment. 

Before you start:
<br> 1. Verify in your /etc/resolv.conf that you have the following nameserver: nameserver 8.8.8.8
<br> 2. You have installed a working version of wireshark and xterm.


Here are the listed instructions followed to run the MPTCP:
1. sudo apt update
2. sudo apt install mptcpize
3. In a mininet xterm for your desired server host, run the following command:
    <br>mptcpize run -d python3 ./server.py
4. In a mininet xterm for your desired client host, run the following command:
    <br>mptcpize run -d python3 ./client.py
    <br> Both these scripts executes the Perf stat process onto the mptcpize client and server.

The mptcpize command forces the any TCP socket program to run MPTCP on top of the process.


Here are the listed instructions followed to run the MPQUIC:
1. In an directory adjacent to this one run: 
       <br> git clone --recursive https://github.com/cloudflare/quiche
        <br> The MPQUIC related scripts to run the client and server only work if the quiche directory is adjacent to this one.
2. sudo apt install cmake
       <br> Default installation
       <br> Rust version 1.70.0
3. sudo apt install cargo
4. source $HOME/.cargo/env
5. cd quiche
6. In the apps/src/bin folder of quiche, please transfer any files you wish for your MPQUIC server to provide.
7. In the quiche/example folder, update the server.rs file by replacing the line 72 with the following mio line:
     <br> mio::net::UdpSocket::bind("10.0.4.1:4433".parse().unwrap()).unwrap();
     <br> We update the IP in use as all mininet topologies assume the sever uses that IP.
8. cargo test
    <br> This will build a number of supported packages for quiche
9. In a mininet xterm run the following command: 
<br> cargo run --bin quiche-client -- https://cloudflare-quic.com/ –config “net.git-fetch-with-cli=true”
<br> You will need to run this commance atleast once as the xterm of seperateily fetch the cargo files.
<br> After you do this, you will not need to do this again.
10. To run the server run the command in a mininet server host: ./MPQUICserverScript.sh
11. To run the client run the command in a mininet client host: ./MPQUICserverScript.sh
