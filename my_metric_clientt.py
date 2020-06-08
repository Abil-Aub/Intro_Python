import socket
import time


class ClientError(Exception):
    pass


class Client:
    def __init__(self, host, port, timeout=None):
        self._host = host
        self._port = port
        try:
            self._sock = socket.create_connection((host, port),
                                                       timeout)
        except:
            raise ClientError

    def _check(self, pl):
        plst = list(pl.split('\n'))
        for plsti in plst:
            if len(plsti.split()) != 3:
                print("Format is not correct")
                raise ClientError

    def _recv(self):
        msg = b""
        try:
            # <статус ответа><\n><данные ответа><\n\n>
            msg = b"".join([msg, self._sock.recv(1024)])

            decmsg = msg.decode()[:-2]

            if decmsg == "ok":
                return ""
            
            st, pl = decmsg.split("\n", 1)
            pl = pl.strip()

            if st == "error" or st != "ok":
                raise ClientError

            self._check(pl)

            return pl
        except:
            raise ClientError

    def put(self, name, value, timestamp=None):
        timestamp = timestamp or int(time.time())

        try:
            self._sock.sendall(
                "put {} {} {}\n".format(name, value, timestamp).encode()
            ) # <команда> <данные запроса><\n>
        except:
            raise ClientError

        self._recv()

    def get(self, name):
        try:
            self._sock.sendall(
                "get {}\n".format(name).encode()
            ) # <команда> <данные запроса><\n>
        except:
            raise ClientError

        pl = self._recv()

        data = {}
        if pl == "":
            return data

        for row in pl.split("\n"):
            name, value, timestamp = row.split()
            if name not in data:
                data[name] = []
            data[name].append((int(timestamp), float(value)))

        for k in data.keys():
            data[k] = sorted(data[k], key = lambda x: x[0])

        return data

    def close(self):
        try:
            self._sock.close()
        except:
            raise ClientError

##
##if __name__ == "__main__":
##    client = Client("127.0.0.1", 10001)
##    client.get("palm.cpu")
