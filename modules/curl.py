import urllib.request


def urllib_curl(host_list):
    for host in host_list:
        try:
            response = urllib.request.urlopen(host)
            print(host)
            print(response.read())
            print("\n")
        except urllib.error.URLError as error:
            print("[-] Unable to curl: " + str(error.reason))
        except urllib.error.HTTPError as error:
            print("[-] Unable to curl: " + str(error.reason))
        except ValueError as error:
            print("[-] Unable to curl: " + str(error))
