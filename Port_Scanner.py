# Provides access to low-level networking interface
import socket 


# Target IP address 
user=input("Please enter an IP adress : ") 


def PortScanner(ip,port):
    # Create a TCP socket
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #socket.AF_INET(IPv4) et socket.SOCK_STREAM(TCP)
    # Set timeout to avoid waiting too long for response
    sock.settimeout(0.5)

    # Try to connect to the target IP and port
    result=sock.connect_ex((ip,port))

    #result
    if result==0:
        print(f"Port {port} : Open") # Port is open (connection successful)
    else:
        print(f"Port {port} Closed") # Port is closed or unreachable


    # Close the socket after each attempt
    sock.close()

#main
if __name__ == '__main__':
    print("+++ welcome to Redissi's Port Scanner +++")
    for ports in[21,22,80,443,3306]: # List of common ports to scan ( 21->FTP / 22->SSH / 80->HTTP / 443->HTTPS / 3306->MySQL )
        PortScanner(user,ports)

