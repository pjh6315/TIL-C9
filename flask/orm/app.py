from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#flask
app = Flask(__name__)

# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#sqlalchemy 초기화
db = SQLAlchemy(app)

# migrate 초기화
migrate = Migrate(app,db)

# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    memo = db.Column(db.Text)
    
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
#정리
#Create
#INSERT INTO users(username, email) VALUES ('nwith','dasdad@gmail.com')
#user = User(username='dadd',email='dsads@gmail.com')
#db.session.add(user)
#db.session.commit()

# read
#SELECT * FROM user;
#users = User.query.all() # 복수

# SELECT * FROM users WHERE username='ddd';
#users = User.query.filter_by(username='ddd').all()

# SELECT * FROM users WHERE username='ddd' LIMIT1;
#users = User.query.filter_by(username='ddd').first()

# SELECT * FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key 만 get으로 가져올수있음

# SELECT * FROM users WHERE email LIKE '%water%'
#users = User.query.filter(User.email.like("%water%")).all()

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all
 
# OFFSET
# users = User.query.offset(2).all()

# ORDER LIMIT OFFSET
# users = User.query.order_by(User.username).limit(1).offset(1).all()

#[DELETE]
# DELETE FROM users WHERE id=1;
# user = User.query.get(1)
# db.session.delete(user)
# db.session.commit()

#[UPDATE]
# UPDATE users SET username = 'pjh' WHERE id=2;
# user = User.query.get(2)
# user.username = 'godjh'
# db.session.commit()

