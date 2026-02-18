from flask import Flask , render_template, request,redirect,session
from flask_sqlalchemy import SQLAlchemy
import bcrypt
app=Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(100))
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()
      
@app.route('/')
def home():
    return render_template('index.html')
@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        Username = request.form['Username']
        email = request.form['email']
        password = request.form['password']
        
        # Validation logic
        error = None
        
        # Check if name is not empty
        if not Username or Username.strip() == '':
            error = 'Name should not be empty'
        # Check if email is not empty
        elif not email or email.strip() == '':
            error = 'Email should not be empty'
        # Check if password is not empty
        elif not password or password.strip() == '':
            error = 'Password should not be empty'
        # Check if password is at least 6 characters
        elif len(password) < 6:
            error = 'Password should be at least 6 characters'
        # Check if email is unique
        elif User.query.filter_by(email=email).first():
            error = 'Email already registered'
        
        # If no error, create the user
        if error is None:
            new_user = User(name=Username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        
        return render_template("register.html", error=error)
    
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid Password')
        
    return render_template("login.html")
@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template("dashboard.html", user=user)
    return redirect('/login')
@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')
if __name__ == '__main__':
    app.run(debug=True)