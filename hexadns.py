import re
import socket


def extract_ipaddr(path, output_path,mode):
    with open(path, 'r') as file:
        url=file.read()

    if mode == '1':
        domains=re.findall(r'(?:https?://)?(?:www\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)',url)
        converter=socket.gethostbyname

    elif mode == '2':
        domains=re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',url)
        converter=socket.gethostbyaddr
    else:
        print("invalid")
        return

    with open(output_path, 'w') as output:
        for domain in domains:
            try:
                ip_addr=converter(domain)
                output.write(f"{domain}:{ip_addr}\n")
            except socket.gaierror:
                output.write(f"cant find ip for {domain}\n")

    print(f"ip saved to {output_path}")

if __name__ == "__main__":
    input_path=input("enter the path:")
    output_path=input("enter the path to save the results:")
    mode=input("press '1' for domain_2_ip and press '2' for ip_2_domain:")

extract_ipaddr(input_path, output_path, mode)

