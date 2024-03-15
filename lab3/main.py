import socket
import threading
import time

from constants import IP_ADDRESS, SERVER_PORT, WINDOW_SIZE, MESSAGE
from tcp import TCPPacket, divide_into_packages
from output import red, blue


server_address = (IP_ADDRESS, SERVER_PORT)

BUFF_CLIENT = -1
BUFF_SERVER = 1

def server():
    global BUFF_CLIENT

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(server_address)

        # start server
        server_socket.listen(1)
        print(red('[SERVER] Server is running and waiting for connections...'), '\n')
        time.sleep(1)

        # get client connection
        client_socket, client_address = server_socket.accept()
        print(red(f'[SERVER] Establish connection from {client_address}'), '\n')
        time.sleep(1)

        # get connection request from client and procces it to send back
        packet = TCPPacket()
        packet.receive(client_socket)

        packet.SYN += packet.ACK 
        packet.flags['ACK'] = True 

        print(red('[SERVER] Send to client:'))
        print(packet, '\n')
        packet.send(client_socket)
        
        packet.receive(client_socket)

        # SYN Flooding (Server side)
        # while packet.data != 'GET DATA':
        #     packet.receive(client_socket)

        if packet.data == 'GET DATA':
            BUFF_CLIENT = packet.SYN + len(packet.data)
            packet.data = MESSAGE
            packets = divide_into_packages(packet, WINDOW_SIZE)

            last_packet = None
            i = 0

            for packet_ in packets:
                # fictional statement
                if i > 0:
                    packet.receive(client_socket)

                # TCP Reset Attack (Server side)
                # if packet.flags['RST']:
                #     raise Exception('Resetting the connection due to RST flag!!!')

                # send one of the packets sing buffer variables
                packet_.ACK = BUFF_CLIENT
                packet_.flags['ACK'] = True
                packet_.SYN = BUFF_SERVER

                print(red('[SERVER] Send to client:'))
                print(packet_, '\n')
                packet_.send(client_socket)

                last_packet = packet_
                i += 1

            packet.receive(client_socket)

            # form and send finish request to client
            last_packet.flags['FIN'] = True
            last_packet.data = 'FINISH SEND DATA'

            print(red('[SERVER] Send to client:'))
            print(last_packet, '\n')
            last_packet.send(client_socket)

            # get from client confirmation to disconnect
            last_packet.receive(client_socket)
            if last_packet.data == 'FINISH SESSION':
                print(red('[SERVER] Disconnection!!!'), '\n')

                client_socket.close()
                server_socket.close()

    finally:
        client_socket.close()
        server_socket.close()


def client():
    global BUFF_SERVER

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # start client
        client_socket.connect(server_address)
        print(blue('[CLIENT] The connection to the server is established.'), '\n')

        client_port = client_socket.getsockname()[1]

        # get connection request
        packet = TCPPacket(client_port, SERVER_PORT, 0, 1, WINDOW_SIZE, 'GET CONNECTION', syn=True)
        print(blue('[CLIENT] Send to server:'))
        print(packet, '\n')
  
        packet.send(client_socket) 

        while True:
            packet.receive(client_socket)
            
            # SYN Flooding (Client side)
            # while True:
            #     print(blue('[CLIENT] Send to server:'))
            #     print(packet, '\n')
            #     packet.send(client_socket)

            # TCP Reset Attack (Client side)
            # packet.flags['RST'] = True

            # send confirmation to server about finishing connection
            if packet.flags['FIN']:
                packet.data = 'FINISH SESSION'

                print(blue('[CLIENT] Send to server:'))
                print(packet, '\n')
                packet.send(client_socket)

                break
            
            # procces ACK and SYN with buffer variables
            if BUFF_CLIENT != -1:
                BUFF_SERVER = packet.SYN + len(packet.data)
                packet.ACK = BUFF_SERVER
                packet.SYN = BUFF_CLIENT

            packet.flags['ACK'] = False
            packet.data = 'GET DATA'          

            print(blue('[CLIENT] Send to server:'))
            print(packet, '\n')
            packet.send(client_socket)
                
    finally:
        client_socket.close()


if __name__ == '__main__':
    server_thread = threading.Thread(target=server)
    client_thread = threading.Thread(target=client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
