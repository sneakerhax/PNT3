import urllib.request


def urllib_curl(host_list):
    for host in host_list:
        try:
            response = urllib.request.urlopen(host)
            print("[+] " + host + " " + "Response code: " + str(response.getcode()))
        except urllib.error.URLError as error:
            print("[-] Unable to curl " + str(host) + ": " + str(error.reason))
        except urllib.error.HTTPError as error:
            print("[-] Unable to curl " + str(host) + ": " + str(error.reason))
        except ValueError as error:
            print("[-] Unable to curl " + str(host) + ": " + str(error))
