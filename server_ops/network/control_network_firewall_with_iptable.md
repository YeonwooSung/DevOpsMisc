# Control network firewall with iptable

## Check list of iptable rules

```bash
# use either -L or --list options
$ iptables -L
$ iptables --list
```

## Open port

```bash
# add accept rule to open 8080 port for input traffic with tcp protocol
$ iptables -I INPUT -p tcp --dport 8080 -j ACCEPT 

# add accpet rule to open 8080 port for output traffic with tcp protocol
$ iptables -I OUTPUT -p tcp --dport 8080 -j ACCEPT
```

Below is the explanation of each option.

* -I: Insert a rule.
* -p: The protocol.
* --dport: The destination port.
* -j: The target of the rule.

## Close port

```bash
# delete accept rule to close 8080 port for input traffic with tcp protocol
$ iptables -D INPUT -p tcp --dport 8080 -j DROP

# delete accept rule to close 8080 port for output traffic with tcp protocol
$ iptables -D OUTPUT -p tcp --dport 8080 -j DROP
```

Below is the explanation of each option.

* -D: Delete a rule.
* -p: The protocol.
* --dport: The destination port.
* -j: The target of the rule.

## Forward port

```bash
# forward 8080 port to 80 port
$ iptables -t nat -A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
```

Below is the explanation of each option.

* -t: The table.
* -A: Append a rule.
* -p: The protocol.
* --dport: The destination port.
* -j: The target of the rule.
* --to-port: The port to forward.

## Save iptable rules

```bash
# save iptable rules
$ iptables-save > /etc/iptables/rules.v4


# use netfilter-persistent package to save iptable rules

# install netfilter-persistent package
$ apt install netfilter-persistent
# save iptable rules
$ netfilter-persistent save
```
