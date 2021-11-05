from smb.SMBConnection import SMBConnection

userID = '<username>'
passWord = '<password>'
clientName = '<client-Name>'
printersName = '<printers-name>'
printersIP = '<printers-ip>'
printersDomain = '<domain-name>'

def samba_lookup():
    conn = SMBConnection(userID, passWord, clientName, printersName,domain=printersDomain, use_ntlm_v2=True,is_direct_tcp=True)
    conn.connect(printersIP, 445)

    shares = conn.listShares()
    print(shares)
	
    for share in shares:
        if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
            sharedFiles = conn.listPath(share.name, '/')
            for sharedFile in sharedFiles:
                print(sharedFile.filename)
				#conn.storeFile(share.name+"/", sharedFile.filename)
				#print(text)

if __name__ == '__main__':
	samba_lookup()