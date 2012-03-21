port = 8026
import SimpleHTTPServer,SocketServer
H = SimpleHTTPServer.SimpleHTTPRequestHandler
d = SocketServer.TCPServer(("", port), H)
print "http://localhost:" + str(port)
d.serve_forever()
