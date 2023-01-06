import sys
import subprocess

usage = "[*] Usage: python3 multi_cloner.py <repo_list>"


def banner():
    print("###############################")
    print("#       multi_cloner.py       #")
    print("#        by: sneakerhax       #")
    print("###############################")
    print("")


def clone(repo_list):
    with open(repo_list, 'r') as clone_list:
        for repo in clone_list:
            print("[+] Cloning repo " + str(repo.strip()))
            remote_origin = str(repo).strip()
            subprocess.Popen(["git", "clone", remote_origin], stdout=subprocess.PIPE).communicate()[0]
            print("\n")


def main():
    if len(sys.argv) == 2:
        repo_list = sys.argv[1]
        banner()
        clone(repo_list)
    else:
        print(usage)


if __name__ == "__main__":
    main()
