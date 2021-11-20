import socket
import sys

usage = "usage: port scanner <target> <ports>"


def port_scanner(target, ports):
    for port in ports:
        try:
            print("[+] Connecting to: " + target + " port:" + str(port))
            s = socket.socket()
            s.connect((target, int(port)))
            s.send('sneakerhax \n')
            banner = s.recv(1024)
            if banner:
                print("[+] Port " + str(port) + " open [+] \n" + banner)
                s.close()
        except Exception as e:
            pass


def main():
    if len(sys.argv) == 3:
        target = sys.argv[1]
        ports = sys.argv[2].split(",")
        port_scanner(target, ports)
    else:
        print(usage)


if __name__ == "__main__":
    main()
