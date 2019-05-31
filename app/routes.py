from app import app
from app.models import model
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Derek'}
    return render_template('index.html', title='Home', user=user)
    
@app.route('/user/<name>')
def user_page(name):
    user = {'name': name}
    return render_template('index.html', title='Home', user=user)
    
    
@app.route('/sendBreakfast', methods=['GET', 'POST'])
def handleBreakfast():
    if request.method == 'GET':
        return "You're getting the breakfast page!"
    else:
        userdata = dict(request.form)
        # Store the nickname in a variable for easy reference
        nickname = userdata['nickname'] # Note that we access the first item in the list provided by the "nickname key"
        # Store the breakfast in a variable for easy reference
        breakfast = userdata['breakfast']
        
        nickname = model.shout(userdata['nickname'])
        breakfast = model.shout(userdata['breakfast'])
        # Use those variables to create a dynamic result for our user
        return "Hello, " + nickname + "! I hear you had " + breakfast + " for breakfast! Sounds delicious."