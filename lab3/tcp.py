import json
import socket
import time

class TCPPacket:
    def __init__(self, source_port=None, destionation_port=None, syn_n=0, ack_n=0, window_size=None, 
                 data='', ack=False, syn=False, fin=False, rst=False) -> None:
        self.source_port = source_port
        self.destionation_port = destionation_port

        self.SYN = syn_n
        self.ACK = ack_n

        self.flags = {
            'ACK': ack,
            'SYN': syn,
            'FIN': fin,
            'RST': rst
        }

        self.window_size = window_size

        self.data = data

    def __str__(self) -> str:
        return json.dumps({
            'SOURCE_PORT': self.source_port,
            'DESTINATION_PORT': self.destionation_port,
            'SYN': self.SYN,
            'ACK': self.ACK,
            'FLAGS': self.flags,
            'WINDOW_SIZE': self.window_size,
            'DATA': self.data
        }, indent=4)

    def send(self, socket: socket.socket) -> None:
        socket.sendall(self.__str__().encode())
        time.sleep(1)
    
    def receive(self, socket: socket.socket) -> None:
        packet = json.loads(socket.recv(1024).decode())
        self.__init__(packet['SOURCE_PORT'], packet['DESTINATION_PORT'], packet['SYN'], packet['ACK'],
                      packet['WINDOW_SIZE'], packet['DATA'], ack=packet['FLAGS']['ACK'], 
                      syn=packet['FLAGS']['SYN'], fin=packet['FLAGS']['FIN'], rst=packet['FLAGS']['RST'])
        time.sleep(1)


def divide_into_packages(tcp_packet: TCPPacket, window_size: int) -> list[TCPPacket]:
    chunk_size = window_size // 8
    data = [tcp_packet.data[i:i+chunk_size] for i in range(0, len(tcp_packet.data), chunk_size)]
    
    packets = []
    for d in data:
        packet = TCPPacket(tcp_packet.source_port, tcp_packet.destionation_port, 
                           tcp_packet.SYN, tcp_packet.ACK, tcp_packet.window_size, d, 
                           tcp_packet.flags['ACK'], tcp_packet.flags['SYN'], tcp_packet.flags['FIN'], 
                           tcp_packet.flags['RST'])
        packets.append(packet)

    return packets