# Credits: https://stackoverflow.com/questions/316866/ping-a-site-in-python
import ping, socket
try:
    ping.verbose_ping('www.google.com', count=3)
    delay = ping.Ping('www.wikipedia.org', timeout=2000).do()
except socket.error as e:
    print ("Ping Error:", e)