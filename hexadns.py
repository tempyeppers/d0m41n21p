import re
import socket

def banner():
    banner_text = """
  __ \    \  |   ___|    _ \                      |                    
  |   |    \ | \___ \   |   |   _ \   __|   _ \   | \ \   /  _ \   __| 
  |   |  |\  |       |  __ <    __/ \__ \  (   |  |  \ \ /   __/  |    
 ____/  _| \_| _____/  _| \_\ \___| ____/ \___/  _|   \_/  \___| _|    
                                                                                                                                                                                                              
"""
    print(banner_text)

banner()

def extract_ipaddr(path, output_path, mode):
    with open(path, 'r') as file:
        url = file.read()

    if mode == '1':
        domains = re.findall(r'(?:https?://)?(?:www\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)', url)
        converter = socket.gethostbyname

    elif mode == '2':
        ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', url)
        converter = socket.gethostbyaddr
    else:
        print("invalid mode")
        return

    with open(output_path, 'w') as output:
        if mode == '1':
            for domain in domains:
                try:
                    ip_addr = converter(domain)
                    output.write(f"{domain}:{ip_addr}\n")
                except socket.gaierror:
                    output.write(f"cant find ip for {domain}\n")
        elif mode == '2':
            for ip in ips:
                try:
                    domain_name = converter(ip)[0]
                    output.write(f"{ip}:{domain_name}\n")
                except socket.herror:
                    output.write(f"cant find domain for ip {ip}\n")

    print(f"Thanks for using the DNS Resolver tool. The results have been saved in the file: {output_path}")


if __name__ == "__main__":
    input_path = input("enter the filename containing the domains/ips:")
    output_path = input("enter the filename to save the results:")
    mode = input("choose the operation: Press '1' for Domain to IP, '2' for IP to Domain:")

    extract_ipaddr(input_path, output_path, mode)
