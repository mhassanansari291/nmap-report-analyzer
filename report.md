# Nmap Service Summary

- **Input file:** `/home/kali/phase2-wapt/evidence/initial-scan.txt`
- **Target:** `192.168.184.129`
- **Open services parsed:** 23

| Port | Protocol | Service | Version / Details |
|---:|:---:|---|---|
| 21 | tcp | ftp | vsftpd 2.3.4 |
| 22 | tcp | ssh | OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0) |
| 23 | tcp | telnet | Linux telnetd |
| 25 | tcp | smtp | Postfix smtpd |
| 53 | tcp | domain | ISC BIND 9.4.2 |
| 80 | tcp | http | Apache httpd 2.2.8 ((Ubuntu) DAV/2) |
| 111 | tcp | rpcbind | 2 (RPC #100000) |
| 139 | tcp | netbios-ssn | Samba smbd 3.X - 4.X (workgroup: WORKGROUP) |
| 445 | tcp | netbios-ssn | Samba smbd 3.0.20-Debian (workgroup: WORKGROUP) |
| 512 | tcp | exec | netkit-rsh rexecd |
| 513 | tcp | login? | Not provided |
| 514 | tcp | shell? | Not provided |
| 1099 | tcp | java-rmi | GNU Classpath grmiregistry |
| 1524 | tcp | bindshell | Metasploitable root shell |
| 2049 | tcp | nfs | 2-4 (RPC #100003) |
| 2121 | tcp | ccproxy-ftp? | Not provided |
| 3306 | tcp | mysql? | Not provided |
| 5432 | tcp | postgresql | PostgreSQL DB 8.3.0 - 8.3.7 |
| 5900 | tcp | vnc | VNC (protocol 3.3) |
| 6000 | tcp | X11 | (access denied) |
| 6667 | tcp | irc | UnrealIRCd |
| 8009 | tcp | ajp13 | Apache Jserv (Protocol v1.3) |
| 8180 | tcp | http | Apache Tomcat/Coyote JSP engine 1.1 |

> This tool summarizes existing scan output only. It does not scan, validate vulnerabilities, or exploit targets.
