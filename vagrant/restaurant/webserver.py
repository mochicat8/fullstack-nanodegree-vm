
### Database stuff
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

## cgi allows form handling from post requestsa
import cgi

from database_setup import Base, Restaurant, MenuItem
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/edit"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output =""

                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/edit'><h2>Enter new Restaurant Name</h2><input name="newRestaurantName" type="text" ><input type="submit" value="Submit"> </form>'''
                self.wfile.write(output)
                return


            if self.path.endswith("/restaurants"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                names = "<ul>"

                for instance in session.query(Restaurant).order_by(Restaurant.name):
                    names += "<li>" + instance.name + "<a href=/restaurants/" + str(instance.id)  + "/edit>Edit</a>" + " <a href='#'>Delete</a>" + "</li>"

                names += "</ul>"
                output = ""
                output += "<html><body>"
                output += "<h1>Hello!</h1>"
                output += "<a href='/restaurants/new'>Make a New Restaurant Here </a>"
                output += names
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return

            if self.path.endswith("/restaurants/new"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output =""

                output += '''<form method='POST' enctype='multipart/form-data' action='/restaurants/new'><h2>Enter new Restaurant</h2><input name="newRestaurantName" type="text" ><input type="submit" value="Submit"> </form>'''
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:

            if self.path.endswith('/restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    restaurantName = fields.get('newRestaurantName')
                restaurant1 = Restaurant(name=restaurantName[0])
                session.add(restaurant1)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()
                return

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webServerHandler)
        print "Web Server running on port %s" % port
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()
