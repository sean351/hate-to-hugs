from flask import Flask
from flask import request
from flask import render_template

# print a nice greeting.


# some bits of text for the page.
# header_text = '''
#     <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
# instructions = '''
#     <p><em>Hint</em>: This is a RESTful web service! Append a username
#     to the URL (for example: <code>/Thelonious</code>) to say hello to
#     someone specific.</p>\n'''
# home_link = '<p><a href="/">Back</a></p>\n'
# footer_text = '</body>\n</html>'
#
# EB looks for an 'application' callable by default.
application = Flask(__name__)

# url_for('static', filename='scripts.js')
# add a rule for the index page.
# application.add_url_rule('/', 'index', (lambda: header_text +
#     say_hello() + instructions + footer_text))

# add a rule when the page is accessed with a name appended to the site
# URL.
# application.add_url_rule('/<username>', 'hello', (lambda username:
#     header_text + say_hello(username) + home_link + footer_text))

@application.route('/')
def index():
    return render_template('index.html')

def say_hello(username = "World"):
    return render_template('postHtml.html', name=username)
    # return '<p>Hello %s!</p>\n' % username

@application.route('/postHtml', methods = ['GET', 'POST'])
def postHtml(something = "IDK"):
    if request.method == 'GET':
        return render_template('postHtml.html')

    if request.method == 'POST':
        html = request.form['html']
        print('Type of html: ' + str(type(html)))
        censorHtml(html)
        return render_template('postHtml.html')


def censorHtml(html):
    print("I'm now in the consor function")

#
# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
