# Unencrypted Services by default
## Details
An attacker can intercept the traffic between the client and the printer.
Multiple services are affected by this vulnerability (HTTP, FTP).

## Proof-of-Concept

1. The Tool "Wireshark" can record the whole traffic. 
2. By inspecting the packets unencrypted HTTP and FTP packets can be found.

## Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **NO**
</br></br>


> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)