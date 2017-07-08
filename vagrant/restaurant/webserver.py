from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi
# Building a webserver
# Two main functions - handler and main()
# Main - instantiate server and specifiy what port it will listen on
# Handler code what code to excute based on what is sent to HTTP server

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/restaurant"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
            # if self.path.endswith("/hola"):
            #     self.send_response(200)
            #     self.send_header('Content-type', 'text/html')
            #     self.end_headers()
            #
            #     output = ""
            #     output += '<html><body>Hola&iexcl; </body><a href="/hello">Back</a</html>'
            #     self.wfile.write(output)
            #     print output
            #     return
        except IOError:
            self.send_error(404, "File Not Found %s" % self.path)

    # def do_POST(self):
    #     try:
    #         self.send_response(301)
    #         self.send_header('Content-type', 'text/html')
    #         self.end_headers()
    #         ctype, pdict = cgi.parse_header(
    #             self.headers.getheader('content-type'))
    #         if ctype == 'multipart/form-data':
    #             fields = cgi.parse_multipart(self.rfile, pdict)
    #             messagecontent = fields.get('message')
    #         output = ""
    #         output += "<html><body>"
    #         output += " <h2> Okay, how about this: </h2>"
    #         output += "<h1> %s </h1>" % messagecontent[0]
    #         output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
    #         output += "</body></html>"
    #         self.wfile.write(output)
    #         print output
    #     except:
    #         pass

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
