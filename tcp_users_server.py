import socket
import websocket

def server():

    history = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ("localhost", 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)
    print("Сервер запущен и ждет подключений ...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Подключение с адресом: {client_address} подключился к сети")

        data = client_socket.recv(1024).decode()
        if data:
            history.append(data)
            print(f"Пользователь с адресом {client_address} отправил сообщение: {data}")

        all_messages = "\n".join(history)
        client_socket.sendall(all_messages.encode())

        client_socket.close()

if __name__ == "__main__":
    server()