from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# Building a webserver
# Two main functions - handler and main()
# Main - instantiate server and specifiy what port it will listen on
# Handler code what code to excute based on what is sent to HTTP server

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>Hello!</body></html>"
        except:
def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        # //takes in a webserverHandler class which will be defined later in code
        print "Web server running on port %s" % port
        server.serve_forever()
        # a function within server

    except KeyboardInterrupt:
        #built-in exception in Python that can be triggered  when user types Ctl-C
        print "^C entered...stopping web server..."
        server.socket.close()



if __name__ == '__main__':
    main()
