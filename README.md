# Epson WorkForce Pro WF-C5710DWF Series vulnerabilities

## Why?
During a research project, the Epson WorkForce Pro WF-C5710DWF Series multifunction device was tested for vulnerabilities. The results can be found in the src/ folder. Several vulnerabilities were closed by the manufacturer. Many others were not. 

## Which vulnerabilities?
* Information Disclosure (3 times; Services: Samba, USB, Firmware)
* Denial of Service (3 times; Services: http, FTP)
* Malconfigured Software (3 times; Services: FTP, Firmware, http)
* CSRF (Cross-Site Request Forgery) (1 time; Service: http(s))

## Requirements (for short)
* Python 3
* pip
* some Linux OS (e.g. Kali or Parrot Linux)

--- 
</br></br>



> Credits: HS-AlbSig Pentesting-Project Team 2020/2021 </br>
Responsible and managed by: Prof. Holger Morgenstern, M.Eng. Simon Malik </br>
Responsible for content: Bastian Buck </br>
Contributors: Robert Schreiber, Dennis Bäßler, Moritz Schürmann, Andreas Luft, Jonas Cremer, Lukas Hoffmann, Lennart Schrottenholzer, Daniel Förderer, Peter Szantai-Kis, Caner Ünal, Johannes Jünger, Roman Alyunov, Bastian Buck

> This security vulnerability was found by HS-AlbSig Pentesting-Project Team (Albstadt-Sigmaringen University) (Technical contact: https://github.com/bstnbuck)
