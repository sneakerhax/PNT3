import argparse
import sys
import smtplib


def banner():
    print("#################################")
    print("#       smtp_authcheck.py       #")
    print("#        by: sneakerhax         #")
    print("#################################")


def smtp_auth(args):
    print("[+] Attempting to connect to server")
    s = smtplib.SMTP(args.server, args.port)
    # Attempt to start TLS connection s.starttls()
    if args.starttls:
        print("[+] Attempting to use STARTTLS")
        s.starttls()

    print("[+] Attempting to say ehlo")
    s.ehlo()

    try:
        s.login(args.username, args.password)
        return "Authentication successful"

    except Exception as e:
        sys.exit("Wrong username or password")

    finally:
        s.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", required=True, action="store", dest='server', help="server address")
    parser.add_argument("-p", "--port", required=True, action="store", dest='port', help="server port", type=int)
    parser.add_argument("-u", "--username", required=True, action="store", dest='username', help="username")
    parser.add_argument("-c", "--password", required=True, action="store", dest='password', help="password")
    parser.add_argument("-stls", '--start-tls', action='store_true', dest='starttls', help='run using STARTTLS')
    args = parser.parse_args()
    banner()
    print("[+] Checking Credentials")
    print(smtp_auth(args))


if __name__ == '__main__':
    main()
