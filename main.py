# -*- coding: utf-8 -*-

#A little message: "You absolutely do NOT let an algorithm mindlessly devour a whole bunch of data that you haven't vetted even a little bit."

from chatbot.logic.CommonWordsResponder import chatbot as CommonWordsResponder
import socket
import sys
import datetime

server = "irc.freenode.net"
channel = "#sugar"
botnick = "chatbot"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "connecting to:"+server
irc.connect((server, 6667))
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" : A simple learning chatbot\n")
irc.send("NICK "+ botnick +"\n")
irc.send("PRIVMSG nickserv :iNOOPE\r\n")
irc.send("JOIN "+ channel +"\n")
chat = CommonWordsResponder.Chatbot()
directory = "logs"
logname = directory+"/"+"{:%Y-%m-%d-%H:%M}_chat.log".format(datetime.datetime.now())
print "Connected"
while True:
	text=irc.recv(2040)
	if text.find('PING') != -1:                          #check if 'PING' is found
		irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
	if text.find(botnick+": ") != -1:
		reply = text.split(botnick+":",1)[1].strip()
		print reply		  
		sentenceoriginal = reply
		sentence = chat.responder.listify(sentenceoriginal)
		if len(sentence)>0:
			r = chat.reply(sentenceoriginal)
			print r	
			irc.send('PRIVMSG '+channel+' :'+r+'\r\n')
			#irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
			with open(logname,'a') as file:
				file.write("User:    "+sentenceoriginal+"\n")
				file.write("Chatbot: "+r+"\n")
			chat.quit()


#while True:
	#print corpus
	#print dictionary
	#sentenceoriginal = sys.stdin.readline()
	#pdb.set_trace()
	#sentenceoriginal = sentenceoriginal.rstrip()
	#sentence = chat.responder.listify(sentenceoriginal)
	#if len(sentence)>0 and sentence[0] == "quit":
	#	chat.quit()
	#	break
	#r = chat.reply(sentenceoriginal)	
	#print r
	#sys.stdout.write("> ")

	#with open(logname,'a') as file:
	#	file.write("User:	 "+sentenceoriginal+"\n")
	#	file.write("Chatbot: "+r+"\n")
