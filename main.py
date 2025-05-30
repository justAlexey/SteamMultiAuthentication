from account import Account
from dotenv import load_dotenv
import os


def main():
    account = Account(os.getenv("SHARED_SECRET"))
    print(account.generate_guard_code())


if __name__ == "__main__":
    load_dotenv()
    main()