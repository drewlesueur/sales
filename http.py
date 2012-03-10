import SimpleHTTPServer,SocketServer
H = SimpleHTTPServer.SimpleHTTPRequestHandler
d = SocketServer.TCPServer(("", 8025), H)
d.serve_forever()
