import webapp2
import jinja2
import os
import random

from google.appengine.api import urlfetch
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())

class ContactPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/contact.html')
        self.response.write(about_template.render())
        
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/contact.html')
        self.response.write(about_template.render())
        
app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/contact', ContactPage),
    ('/about', AboutPage),
], debug=True)


accounts = [
    {
        "username": "Roy",
        "password": "showmeme"
    },
    {
        
    }
]