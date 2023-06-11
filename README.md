# cs179iMPTCPvsMPQUIC

All comamnds performed assume you are in a linux environment. 

Here are the listed instructions followed to run the MPTCP:
1. sudo apt update
2. sudo apt install mptcpize
3. 
    <br>a. mptcpize enable server.py
    <br>b. mptcpize enable client.py
4. In a mininet xterm for your desired server host, run the following command:
    <br>mptcpize run -d python3 ./server.py
5. In a mininet xterm for your desired client host, run the following command:
    <br>mptcpize run -d python3 ./client.py

The mptcpize command forces the any TCP socket program to run MPTCP on top of the process.
