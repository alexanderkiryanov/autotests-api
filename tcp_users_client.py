import socket

def client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    message = input(f"Введите сообщение для сервера: ").strip()
    client_socket.sendall(message.encode())

    messages_list = []
    while True:
        single_msg = client_socket.recv(1024)
        if not single_msg:
            break
        messages_list.append(single_msg.decode())

    client_socket.close()

    response = "\n".join(messages_list)
    print(response)

if __name__ == "__main__":
    client()