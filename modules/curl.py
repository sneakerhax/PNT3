import urllib.request


def urllib_curl(host_list):
    for host in host_list:
        try:
            response = urllib.request.urlopen(host)
            print(host)
            print(response.read())
            print("\n")
        except:
            print("Unable to curl")
