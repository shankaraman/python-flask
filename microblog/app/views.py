from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'Miguel'}
    posts = [
        {
            'author' : {'nickname' : 'John'},
            'body' : 'John is wicked witch'
        },
        {
            'author' : {'nickname' : 'h1dd3ntru7h'},
            'body' : 'Beautiful day in Italy'
        }
    ]
    """return '''
    <html>
        <head>
            <title> Home Page </title>
        </head>
        <body>
            <h1> Hello, ''' + user['nickname'] + ''' </h1>
        </body>
    </html> 
    '''"""
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
