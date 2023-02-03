# DNS

Domain Name Server (DNS) is a standard protocol that helps Internet users discover websites using human readable addresses.
Like a phonebook which lets you look up the name of a person and discover their number, DNS lets you type the address of a website and automatically discover the Internet Protocol (IP) address for that website.

Without DNS, the Internet would collapse - it would be impossible for people and machines to access Internet servers via the friendly URLs they have come to know.

## DNS Propagation

Unlike a phone book, DNS records are commonly updated, meaning that a server’s IP address can change without affecting end users.
Users continue to use the same domain name, and are automatically redirected to the new address.
A DNS A or AAAA Record points a domain or subdomain to an IP, and a CNAME record points a domain or subdomain to another domain name.

After you register a new domain name or when you update DNS servers on your domain name, it usually takes about 12-36 hours for the domain name servers world-wide to be updated and able to access the information.

DNS allows for multiple hostnames to correspond to a single IP address - this can be used for virtual hosting, when many websites are served from a single host.
A single hostname can also resolve to many IP addresses, in order to distribute load to multiple servers.

## DNS Resolutions

Typically, when you connect to a local network, Internet service provider (ISP) or WiFi network, the modem or router sends network configuration information to your local device, including one or more DNS servers.
These are the initial DNS servers your device will use to translate host names to IP addresses.

A component called a DNS Resolver is responsible for checking if the host name is available in local cache, and if not, contacts a series of DNS Name Servers, until eventually it receives the IP of the website or service you are trying to reach.
If everything is working well, this can take less than a second.
The process is known as DNS resolution of a hostname to IP address.

## DNS lookup utility

`dig (domain information groper)` is a flexible tool for interrogating DNS name servers.
It performs DNS lookups and displays the answers that are returned from the name server(s) that were queried.
Most DNS administrators use dig to troubleshoot DNS problems because of its flexibility, ease of use and clarity of output.
Other lookup tools tend to have less functionality than dig.

### SOA Record

The SOA record is the start of authority record for a domain.
It contains information about the domain, such as the name of the primary name server, the email address of the domain administrator, the domain serial number, and several timers relating to refreshing the zone.

```bash
$ dig google.com soa
```

By running the above command, you will get the following output (the output may vary depending on the time)):

```
; <<>> DiG 9.10.6 <<>> google.com soa
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6540
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	SOA

;; ANSWER SECTION:
google.com.		24	IN	SOA	ns1.google.com. dns-admin.google.com. 506571425 900 900 1800 60

;; Query time: 5 msec
;; SERVER: 168.126.63.1#53(168.126.63.1)
;; WHEN: Fri Feb 03 18:31:25 KST 2023
;; MSG SIZE  rcvd: 89
```

### NS Record

The NS record is the name server record for a domain.
It contains information about the name servers for a domain.

```bash
$ dig google.com ns
```

By running the above command, you will get the following output (the output may vary depending on the time)):

```
; <<>> DiG 9.10.6 <<>> google.com ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 7991
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 9

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;google.com.			IN	NS

;; ANSWER SECTION:
google.com.		156762	IN	NS	ns2.google.com.
google.com.		156762	IN	NS	ns1.google.com.
google.com.		156762	IN	NS	ns4.google.com.
google.com.		156762	IN	NS	ns3.google.com.

;; ADDITIONAL SECTION:
ns1.google.com.		161093	IN	A	216.239.32.10
ns2.google.com.		163162	IN	A	216.239.34.10
ns3.google.com.		163196	IN	A	216.239.36.10
ns4.google.com.		163169	IN	A	216.239.38.10
ns1.google.com.		183453	IN	AAAA	2001:4860:4802:32::a
ns2.google.com.		171291	IN	AAAA	2001:4860:4802:34::a
ns3.google.com.		163196	IN	AAAA	2001:4860:4802:36::a
ns4.google.com.		163196	IN	AAAA	2001:4860:4802:38::a

;; Query time: 4 msec
;; SERVER: 168.126.63.1#53(168.126.63.1)
;; WHEN: Fri Feb 03 18:32:53 KST 2023
;; MSG SIZE  rcvd: 287
```
