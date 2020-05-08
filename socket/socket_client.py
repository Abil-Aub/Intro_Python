# создание сокета, клиент

import socket
import time

##sock = socket.socket()
##sock.connect(("127.0.0.1", 10001))
##sock.sendall("ping".encode("utf8"))
##sock.close()

# более короткая запись

sock = socket.create_connection(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf8"))
time.sleep(5)
sock.close()
