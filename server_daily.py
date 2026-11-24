import argparse
import socket
from datetime import date

HOST = "127.0.0.1"
PORT = 17

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

TIPS = {
    "Monday": "Lock your screen before leaving your desk.",
    "Tuesday": "Take your laptop with you when you leave your car.",
    "Wednesday": "Check the sender before opening an attachment.",
    "Thursday": "Keep drinks away from your laptop.",
    "Friday": "Include the error message in your support ticket.",
    "Saturday": "Keep your laptop bag closed when it rains.",
    "Sunday": "Back up your important files regularly.",
}

parser = argparse.ArgumentParser()
parser.add_argument("--day", choices=DAYS, help="Choose a day for the demo")
args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"QOTD server ready on {HOST}:{PORT}")
    if args.day:
        print(f"Demo day: {args.day}")

    while True:
        client, address = server.accept()
        with client:
            day = args.day or DAYS[date.today().weekday()]
            message = f"{day}: {TIPS[day]}\r\n"
            client.sendall(message.encode("ascii"))
            print(f"Sent the {day} tip to {address}")
