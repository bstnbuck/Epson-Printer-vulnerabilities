
## Information Disclosure (USB -> Samba (Pass-through))
### Details
An attacker can use it to read data from a connected USB device. 
Thus, the severity depends on the data on the affected devices. 
In addition, the victim would not notice that data was copied, 
since the printer does not provide any information about the access.

### Proof-of-Concept

1. Connect a USB stick to the printer
2. Log in on to the printer via Samba and (program-automated) checking for new data. (example use: `python3 samba_lookup.py`)
3. Download new data if necessary. No log messages are left.

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**

---

## Information Disclosure (USB -> USB (Pass-through))
### Details
An attacker can use it to read data from a connected USB device. 
Thus, the severity depends on the data on the affected devices. 
In addition, the victim would not notice that data was copied, 
since the printer does not provide any information about the access.

### Proof-of-Concept

1. Connecting a USB stick to the printer
2. Plugging in a (for example Raspberry-Pi) which checks for new data and downloads if necessary

#### example flow
file: cp.sh (Bash)
```bash
#!/bin/sh
cp -r $1 /path/to/save/directory
```

Start Script
```bash
while true; do
	ls -d $printerdirectory | entr -d ./cp.sh $printerdirectory
done
```

### Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**
</br></br>


> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)