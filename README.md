# Redissi-s-Port-Scanner
A simple Python tool that scans a list of ports on a target IP address and identifies whether they are open or closed.

## Features
- Scans multiple ports on a target host
- Detects open and closed ports
- Uses TCP sockets for network communication
- Fast scanning with timeout control

## Technologies Used
- Python
- socket

## How it works
The program attempts to connect to each port on the target IP address.  
If the connection is successful, the port is considered open. Otherwise, it is closed.

## Ports scanned
- 21 (FTP)
- 22 (SSH)
- 80 (HTTP)
- 443 (HTTPS)
- 3306 (MySQL)

## Usage
1. Replace the target IP address in the code:
```python
user = "YOUR_TARGET_IP"
