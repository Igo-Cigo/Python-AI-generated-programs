# prompt used: Port Scanner - Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open. this script should be written in python

import socket

# Enter the IP address and port range to scan
IP_ADDRESS = "xxx.xxx.xxx.xxx"
START_PORT =    1
END_PORT = 100

# Create a socket and try to connect to each port in the range
for port in range(START_PORT, END_PORT+1):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  result = s.connect_ex((IP_ADDRESS, port))
  
  # If the connection is successful, the port is open
  if result == 0:
    print(f"Port {port} is open")
    
  # Close the socket
  s.close()
