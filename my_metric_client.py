import time
import socket
from collections import defaultdict


class ClientError(Exception):
    pass


class Client():
    def __init__(self, server_ip, server_port, timeout=None):
        self._sip = server_ip
        self._sport = server_port
        self._timeout = timeout

    def get(self, metric_name):
        toget = defaultdict(list)
        tosend = "get {}\n".format(metric_name)

        with socket.create_connection((self._sip, self._sport), self._timeout) \
             as sock:
            try:
                sock.send(tosend.encode("utf-8"))
            except socket.error:
                raise ClientError()

            torecv = sock.recv(1024)
            torecv = torecv.decode("utf-8")
            torecv = [i.split() for i in torecv.split('\n')[1:] if len(i) > 1]
            [toget[i[0]].append((int(i[2]), float(i[1]))) for i in torecv]
        if metric_name == '*':
            return toget
        else:
            toget = {metric_name: toget.get(metric_name)}
            return toget

    def put(self, metric_name, metric_value, timestamp=None):

        if timestamp is None:
            timestamp = int(time.time())

        tosend = "put {} {} {}\n".format(metric_name, metric_value, timestamp)

        with socket.create_connection((self._sip, self._sport), self._timeout) \
             as sock:
            try:
                sock.sendall(tosend.encode("utf-8"))
            except socket.error:
                raise ClientError()
