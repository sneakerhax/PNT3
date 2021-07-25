import argparse
import sys
import smtplib


def main(args):
    print("[+] Checking Credentials")
    print(smtp_auth(args.server, args.port, args.username, args.password))


def banner():
    print("#################################")
    print("#       smtp_authcheck.py       #")
    print("#        by: sneakerhax         #")
    print("#################################")


def usage():
    print("Usage: python smtp_authcheck.py --server <mail server> --port <SMTP port> --username <username> --password <password>")


def smtp_auth(server, port, username, password):
    s = smtplib.SMTP(server, port)
    s.starttls()

    try:
        s.login(username, password)
        return "Authentication successful"

    except smtplib.SMTPAuthenticationError:
        return "Wrong username or password"

    finally:
        s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", action="store", dest='server', help="server address")
    parser.add_argument("--port", action="store", dest='port', help="server port", type=int)
    parser.add_argument("--username", action="store", dest='username', help="username")
    parser.add_argument("--password", action="store", dest='password', help="password")

    args = parser.parse_args()
    banner()
    main(args)
