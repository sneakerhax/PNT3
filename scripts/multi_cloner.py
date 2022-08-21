import sys
import subprocess


def banner():
    print("")
    print("#######################")
    print("#    Multi Cloner     #")
    print("#######################")
    print("")


def clone(git_url, repo_list):
    with open(repo_list, 'r') as clone_list:
        for repo in clone_list:
            print("[+] Cloning repo " + str(git_url) + str(repo))
            remote_origin = str(git_url + repo).strip()
            subprocess.Popen(["git", "clone", remote_origin], stdout=subprocess.PIPE).communicate()[0]
            print("\n")


def main():
    if len(sys.argv) == 3:
        banner()
        git_url = sys.argv[1]
        repo_list = sys.argv[2]
        clone(git_url, repo_list)
    else:
        print("[*] Usage: python3 multi_cloner.py <repo_url> <repo_list>")


if __name__ == "__main__":
    main()
