# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:00:37 2023

@author: Prince Adeyemi
"""
import json
import websocket

SOCKET = "wss://stream.binance.us:9443/ws"

def getInfo(symbol):
    global my_request
    my_request = json.dumps({'method':'SUBSCRIBE', 'params':[symbol.lower() +'@ticker'], 'id':1})

def on_open(ws):
    print('opened connection, sending request, please wait...')
    ws.send(my_request)

def on_close(ws):
    print('closed connection')

def on_error(ws, error):
    print(error)

def on_message(ws, message):
    print('Receiving data from binance, please wait ...')
    json_message = json.loads(message)
   
    print(json_message) 
  

ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_error=on_error, on_message=on_message)
ws.run_forever()
