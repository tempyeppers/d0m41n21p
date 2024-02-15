import re
import socket


def extract_ipaddr(path, output_path):
    with open(path, 'r') as file:
        url=file.read()
    
    domains=re.findall(r'(?:https?://)?(?:www\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)', url)

    with open(output_path, 'w') as output:
        for domain in domains:
            try:
                ip_addr=socket.gethostbyname(domain)
                output.write(f"{domain}:{ip_addr}\n")
            except socket.gaierror:
                output.write(f"cant find ip for {domain}\n")

    print(f"ip saved to {output_path}")

extract_ipaddr("domain.txt", "ip.txt")

