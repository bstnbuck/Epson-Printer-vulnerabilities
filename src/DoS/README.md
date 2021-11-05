# Denial of Service (DoS)

## WebUI DoS
### Details
An attacker can use it to make the printer unavailable for some time.

### Proof-of-Concept

1. In `https://<ip>/PRESENTATION/ADVANCED/PASSWORD/SET` the user can type in username and password.
2. Make a POST-request with very large usernames to the URL. Use  `dos_webui.py` Python3 script. Like `python3 dos_webui.py`.

3. With this the printer was unavailable for more than 10 minutes.

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**

---

## Firmware update DoS
### Details
An attacker can use it to make the printer completely unavailable.

### Proof-of-Concept

1. With `https://<ip>/DOWN/FIRMWAREUPDATE/ROM1` the printer firmware can be updated.
2. Make a GET-request to the URL. Use `dos_firmware.py` Python3 script. Like `python3 dos_firmware.py`.

3. With this the printer is fully unavailable. The printer has to be hard rebooted.

### Affected Firmware Version
> **16.57.CU24JA**

Patch released by manufacturer: **YES** (version: **16.58.CU10KB**)
</br></br>

---

## DoS via FTP
### Details
If an Attacker finds a non parsed file format, the printer prints it in binary format. 
Due to this behaviour, the printer prints a very large number of sheets and 
is not to be used until then.
### Proof-of-Concept

1. Print some file, that is not correctly parsed to the printer via FTP

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**
</br></br>


> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)