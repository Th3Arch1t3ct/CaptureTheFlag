Magic Conch Writeup
-----------------------------
Solving this was as easy as writing a *PowerShell* script that takes one argument and determines whether or not it is a valid IPv4 or IPv6 address.

Example:
```
PS C:\Users\arch1t3ct> solve.ps1 192.168.1.1
IPv4
PS C:\Users\arch1t3ct> solve.ps1 FE80:CD00:0000:0CDE:1257:0000:211E:729C
IPv6
PS C:\Users\arch1t3ct> solve.ps1 999.999.999.999
Invalid
```
--------------------------------
PowerShell provides an easy way to handle command line arguments
```PowerShell
$ip_addr = arg[0]
```

Regex is the easiest and most straightforward way of validating the argument passed:
```PowerShell
$ipv4Regex = ''
$ipv6Regex = ''
```

Lastly, just do the validation!
```PowerShell
if($ip_addr -match '\b$ipv4Regex\b'){
  Write-Output "IPv4"
} elseif($ip_addr -match '\b$ipv6Regex\b') {
  Write-Output "IPv6"
} else {
  Write-Output "Invalid"
}
```
