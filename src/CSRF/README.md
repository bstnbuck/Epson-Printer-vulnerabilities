# CSRF (Cross-Site Request Forgery)

## Details
Some forms of the web-interface aren't protected against CSRF.
An attacker can trick an authenticated user into (unknowingly) sending requests to the server.
This can be any request that doesn't require confirmation of the password.
The attack can be disguised so that the user will not notice it.


## Proof-of-Concept

1. Catch a request for the desired action with a tool such as "Burp Suite" to examine the required parameters and path for the desired action. The only authentification is a session cookie.

2. Trick the user into sending a request with those required parameters to the right path on the server (ex. html form in email / malicious website). (see csrf.html for an example)

## Affected Firmware Version
> **16.57.CU24JA, 16.58.CU10KB**

Patch released by manufacturer: **YES** (version: **CU22LA**)
</br></br>



> Credits: HS-AlbSig Pentesting-Project Team 2020/2021

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)

