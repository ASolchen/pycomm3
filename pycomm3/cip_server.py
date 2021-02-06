# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Ian Ottoway <ian@ottoway.dev>
# Copyright (c) 2014 Agostino Ruscito <ruscito@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

__all__ = ['CIPServer']

import logging
import ipaddress
from functools import wraps
from os import urandom
from typing import Union, Optional

from .exceptions import DataError, CommError, RequestError
from .tag import Tag
from .bytes_ import Pack, Unpack
from .const import (PATH_SEGMENTS, ConnectionManagerInstance, PRIORITY, ClassCode, TIMEOUT_MULTIPLIER, TIMEOUT_TICKS,
                    TRANSPORT_CLASS, PRODUCT_TYPES, VENDORS, STATES, MSG_ROUTER_PATH,
                    ConnectionManagerService, Services)
from .packets import DataFormatType, RequestTypes
from .socket_ import Socket
from socketserver import TCPServer, StreamRequestHandler

class CIPServerStreamRequestHandler(StreamRequestHandler):
        
    def handle(self):
        # Receive and print the data received from client

        print("Recieved one request from {}".format(self.client_address[0]))

        msg = self.rfile.readline().strip()

        print("Data Recieved from client is:".format(msg))

        print(msg)  

        # Send some data to client

        #self.wfile.write("Hello Client....Got your message".encode())





class CIPServer:
    """
    A base CIP server.  Used to listen for and communicate with CIP scanner.
    """
    __log = logging.getLogger(f'{__module__}.{__qualname__}')
    def __init__(self):
        self.request_handler = CIPServerStreamRequestHandler
    
    def open(self):
        self.server = TCPServer(("0.0.0.0", 44818), self.request_handler)
        self.server.serve_forever()






