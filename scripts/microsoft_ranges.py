import re
import requests
import urllib.request
import xml.etree.ElementTree as ET


# Download link for Microsoft public ip space
mspublic_ip_download = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=53602"

# Download link for Azure public ip space
azure_ip_download = "https://www.microsoft.com/en-us/download/confirmation.aspx?id=41653"

# Header used for the downloads page
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
          'Accept-Encoding': 'none',
          'Accept-Language': 'en-US,en;q=0.8',
          'Connection': 'keep-alive'}


# Request and decode download
def urllib_curl(website, header):
    request = urllib.request.Request(website, headers=header)
    body = urllib.request.urlopen(request)
    return body.read().decode()


# Regex that finds the download link for the Azure public ips on the download page
def regex_azure_download_link(string):
    pattern = r'https://download.microsoft.com/download/\d/\d/\d/\w+-\w+-\w+-\w+-\w+\/\w+.xml'
    match = re.search(pattern, string)
    return match.group()


# Regex that finds the download link for the Microsoft public ips on the download page
def regex_mspub_download_link(string):
    pattern = r'https://download.microsoft.com/download/\w/\w/\w/\w+-\w+-\w+-\w+-\w+/msft-public-ips.csv'
    match = re.search(pattern, string)
    return match.group()


# Parses the Azure public ip xml and prints the subnets
def parse_azure_xml(download_link):
    azure_xml = requests.get(download_link).content
    tree = ET.fromstring(azure_xml)
    for child in tree:
        for address in child:
            print(address.attrib['Subnet'])


# Parses the Microsoft public ip csv and prints the subnets
def parse_ms_public_csv(download_link):
    ms_csv = requests.get(download_link).content.decode()
    new_file = ms_csv.split("\n")
    for line in new_file[1:]:
        print(line)


def main():
    print("[+] Printing Azure ip ranges:")
    azure_download_page = urllib_curl(azure_ip_download, header)
    azure_download_link = regex_azure_download_link(azure_download_page)
    parse_azure_xml(azure_download_link)
    print("[+] Printing MS public ip ranges:")
    ms_public_download_page = urllib_curl(mspublic_ip_download, header)
    ms_download_link = regex_mspub_download_link(ms_public_download_page)
    parse_ms_public_csv(ms_download_link)


if __name__ == "__main__":
    main()
