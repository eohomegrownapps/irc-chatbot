#! /usr/bin/env python
#
# Example program using irc.client.
#
# This program is free without restrictions; do anything you like with
# it.
#
# Joel Rosdahl <joel@rosdahl.net>

import sys
import argparse
import itertools

import irc.client

"The nick or channel to which to send messages"

def on_connect(connection, event):
    connection.join("#sugar")
    main_loop(connection)

def on_join(connection, event):
    main_loop(connection)

def get_lines():
    while True:
        yield sys.stdin.readline().strip()

def main_loop(connection):
    for line in itertools.takewhile(bool, get_lines()):
        print line

def on_disconnect(connection, event):
    main()

def main():

    args = get_args()

    reactor = irc.client.Reactor()
    try:
        c = reactor.server().connect("irc.freenode.net", 6667, "chatbot")
    except irc.client.ServerConnectionError:
        print(sys.exc_info()[1])
        raise SystemExit(1)

    reactor.process_forever()

if __name__ == '__main__':
    main()
