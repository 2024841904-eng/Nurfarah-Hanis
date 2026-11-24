import socket

with socket.create_connection(("127.0.0.1", 17)) as client:
    with client.makefile("r", encoding="ascii") as reply:
        quote = reply.read()

print("Quote of the Day:")
print(quote.strip())
