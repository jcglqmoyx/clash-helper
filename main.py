import sys

import mail_tm
from clash_nodes.fly import Fly
from clash_nodes.gou import *
from mail_tm import get_first_message


def main():
    if len(sys.argv) < 2:
        print("Available commands: [1: fly, 2: 加速狗]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "1":
        fly = Fly()
        fly.register()
    elif command == "2":
        email, password = mail_tm.register()
        send_verification_code_to_email(email)
        msg = get_first_message(mail_tm.login(email, password))
        verification_code = extract_verification_code_from_email(msg)
        register(email, password, verification_code)
        cookies = login(email, password)
        link = get_subscription_link(cookies)
        import pyperclip
        pyperclip.copy(link)
        print(link)
    else:
        print(f"Unknown command: {command}")
        print("Available commands: [1: fly, 2: 加速狗]")
        sys.exit(1)


if __name__ == '__main__':
    main()
