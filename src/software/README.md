## Misconfigurated Software
### Details
An attacker can reset the admin user account when the access control is deactivated.

### Proof-of-Concept

1. Go to the printers control panel (physically)
2. Navigate to the "gear"-symbol (top right)
3. Navigate to user settings
4. A non-logged-in user can change or remove the password for the admin 
	and set up an access restriction by himself

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**

---

## Information Disclosure
### Details
An attacker can use it to read print jobs via service support mode.

### Proof-of-Concept

1. Power off the printer.
2. Now press Power-button and "#"-Button at the same time until the printer 
	powers on.
3. Enter the service PIN (can be found in the service manual on page 216)
4. Plug in a USB-Stick and choose "Debug Log Write Mode"
5. When analysing the created 4 files the file with ending ".frd" is interesting.
6. By using the following Linux command usernames can be found:
	`strings <filename>.frd`

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**
</br></br>


> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)
