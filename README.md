All it really does, is spam the living hell out of enumerated file upload vulnerabilities and path permissions issues that should have been taken care of by their administrators.

This is also known as host-header injection.

How it works is...

1. Reads a list of known directory traversal vulns from a wordlist
2. Generates a gigantic list of HTTP GET/POST/PUT requests,
3. Hammers the router with it for half an hour
4. And find out which one of the payloads made it.

You want to be looking at a traversal vulnerablity. that throws a code 302 or lower. That is the only chance we have at getting a stable shell to immediately work with.

Be warned, that it's quite tough. The first thing you should do if you land a shell is immediately get out of the environment, escalate your privileges and add yourself as a new username="admin". This app was specifically designed to launch Weevely PHP payloads, in both it's raw execuable form and as a embedded malware component on webpages.

With someone's index.html is in the root web directory, with rwx permissions, then the payload will definitely go off even if its embedded as script tags in the html webpage. If someone loads your website. It goes off. Inside of THEIR webbrowser. And if they were to escape the sandbox of the web browser, then they got a lot to worry about.

# This already is working with...

1. Three working payloads from
  a. A Weevely PHP Penetration Testing Webshell
  b. A embedded PHP of that variant inside of a file called index.htm (it is created when the attack starts) due to the nature of POST requests
  c. A NodeJS Metasploit reverse shell, easily upgradable to Meterpreter.
  
Shell injection vulnerabilities are in fact, disturbingly common. If you own a wordpress, try running this against it to audit it.

# Official Steps

1. Generate a vulnerability report with dotdotpwn
2. Generate your own payloads using Weevely, Metasploit, Pupy, CoinHive, etc.
3. Load all of the obfuscated code into the script urlinjector.py

Point your cannon at whatever unsecured domain you found, and let it rip! Keep your reverse shell listeners running at ALL TIMES. If a web app payload embedded into a webpage snares someone, their reverse shell will be connecting IMMEDIATELY.
