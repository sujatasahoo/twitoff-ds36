#from flask import Flask, render_template
#from.models import DB, User, Tweet
# factory


# def create_app():
#from flask import Flask


##app = Flask(__name__)
# Tell our app where to find


# @app.route("/")
#def hello_world():##
# return "render_template!"


# @app.route("/another")
# def hello_world():
# return "another page"


# DB.drop_all()
# creat tables according to the classes in models.py
# DB.create_all()
# return render_template('base.html', title='Reset DB')


# @app.route('/populate')
# def populate():
#ryan = User(id=1, username='Ryan')


# tweet
# tweets = (comes from DB.backref)


# def __repr__(self):
# return f"<user>"


# class Tweet(DB.Model):
# id
#id = DB.Column(DB.BigInteger, primery_key=True)
# text
#text = DB.Column(DB.Unicode(300))
# user_id
# user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
# 'user.id'), nullable=False)
# user
# Going to add an attribute to both tables(User and Tweet)
#user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))


# copy from app.py
# Tell our app where to find

# def create_app():


# @app.route("/")
# def hello_world():
# return "Hello, World!"


# @app.route("/another")
# def hello_world():
# return "another page"


# DB.drop_all()
# creat tables according to the classes in models.py
# DB.create_all()
# return render_template('base.html', title='Reset DB')


# @app.route('/populate')
# def populate():


# @app.route("/")
# def hello_world():
# return render_template('base.html', title='DS36')

# @app.route("/another")
# def another():
# return render_template('base.html', title='another')
# return app

# populate function for module-1
# def populate():
#ryan = User(id=1, username='Ryan')
# DB.session.add(ryan)
#jack = User(id=2, username='jack')
# DB.session.add(jack)
#tweet1 = Tweet(id=1, text='Ryan tweet', user=ryan)
# DB.session.add(tweet1)
#tweet2 = Tweet(id=2, text='Jack tweet', user=jack)
# DB.session.add(tweet2)
# DB.session.commit()
# return render_template('base.html', title='Populate')
