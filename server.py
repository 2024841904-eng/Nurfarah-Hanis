import socket

HOST = "127.0.0.1"
PORT = 17
QUOTE = "A clear ticket helps the next technician."

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"QOTD server ready on {HOST}:{PORT}")

    while True:
        client, address = server.accept()
        with client:
            print(f"Client connected from {address}")
            client.sendall((QUOTE + "\r\n").encode("ascii"))
        print("Quote sent. Waiting for the next client.")
