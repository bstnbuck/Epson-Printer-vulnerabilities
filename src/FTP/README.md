# Anonymous FTP by default

## Details
An attacker can use it to make the printer unavailable for some time.
The printer prints excessively to the end of colour or paper.

## Proof-of-Concept

1. Connect to the printer with FTP by using:
	`ftp <ip-address>`
2. Upload some file with (in our test a simple PNG picture):
	`put <filename>`
3. The printer prints it without login as binary trash.

## Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**
</br></br>



> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)