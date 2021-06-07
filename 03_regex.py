import re
import sys

def check_phone(number):
    phoneRegex = re.compile(r'''(
    ( (\d{3}|\(\d{3}\))?              #region code
    (\s|-)?                         #separator
    (\d{3})                         #first 3 digits
    (\s|-)?                         #separator
    (\d{2})                         #digits
    (\s|-)?                         #separator
    (\d{2}) )                       #digits
    |
    (\d{4}|\(\d{4}\))?              #four digit region code
    ( (\s|-)?(\d{2}) ){3}           # and six digit phone number
        )''', re.VERBOSE)

    if phoneRegex.search(number):
        print ("This is a valid phone number")
    else:
        print ("This is not a valid phone number")


def check_email(email):
    emailRegex = re.compile(r'''(
    (\w+)    #username
    @
    (\w+)   #hostname
    \.
    (\w{2,3}) #extension
    )''', re.VERBOSE)

    if emailRegex.search(email):
        print("This is a valid email")
    else:
        print ("This is not a valid email")

def check_ip(ip):
    ipRegex = re.compile(r'''(
    ^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3} # numbers from 0 to 255 separated by .
    (?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$
    )''', re.VERBOSE)
    if ipRegex.search(ip):
        print ("This is a valid ip address")
    else:
        print ("This is not a valid ip address")


def check_mac(mac):
    macRegex = re.compile(r'(([0-9a-f]{4}(:|\.)){3}[0-9a-f])')
    if macRegex.search(mac):
        print("This is a valid mac address")
    else:
        print("This is not a valid mac address")
menu = 0

while True:
    menu = input("""
    1. Check phone number
    2. Check email
    3. Check ip address
    4. Check mac address
    0. Exit
    """)
    if menu == "1":
        check_phone(input("Enter phone number:"))
    if menu == "2":
        check_email(input("Enter email:"))
    if menu == "3":
        check_ip(input("Enter ip address:"))
    if menu == "4":
        check_mac(input("Enter mac address:"))
    if menu == "0":
        sys.exit()
