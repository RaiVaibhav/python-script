# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
from urllib import request,parse
import sys
import json

# base url to the api
url = "https://maps.googleapis.com/maps/api/directions/json?"

# block to exit
def exit_point():
    e = input("Exit(y/n): ")
    if e=='Y' or e=='y':
        print("\nThanks for using this service. HAPPY TRAVELLING.\n")
        sys.exit(1)
    elif e=='n' or e=='N':
        main()
    else:
        print("Invalid option")
        exit_point()


def travel_time(frm,to,mode):
    try:
        new_url = url + parse.urlencode({'origin':frm,'destination':to,'mode':mode})
        data = request.urlopen(new_url).read().decode()
        try:
            js = json.loads(data)
        except:
            js = None
        if not js or 'status' not in js or js['status']!='OK':
            print('==== Failure To Retrieve ====')
            exit_point()
        return js["routes"][0]["legs"][0]["duration"]["text"]
    except SystemExit:
        sys.exit(1)
    except:
        print("Check your network connection")
        sys.exit(1)


def main():
    try:
        frm = input("Origin : ").lower();
        if len(frm)<1:
            exit_point()
        to = input("Destination : ").lower();
        if len(to)<1:
            exit_point()
        mode = input("Mode(Driving,Train,Walking) : ").lower();
        while mode not in ["driving","train","walking"]:
            if len(mode)<1:
                exit_point()
            print("Choose from given options only")
            mode = input("Mode(Driving,Train,Walking) : ").lower();
        if mode=='train':
            mode='transit'
        netTime = travel_time(frm,to,mode)
        print("\nIt will take %s to travel from %s to %s." %(netTime, frm, to))
        exit_point()
    except KeyboardInterrupt:
        print("A Keyboard Interrupt was issued by user.\nThank you for using this service.\n")
        sys.exit(1)
    except SystemExit:
        sys.exit(1)
    except:
        print("Error: Invalid keystroke")
        exit_point()

if __name__ =='__main__':
    main()
