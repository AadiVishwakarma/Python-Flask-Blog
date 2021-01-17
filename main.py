from flask import Flask, render_template,request , session , redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
from flask_mail import Mail
import os
from werkzeug.utils import secure_filename
import math

with open('config.json','r') as c:
    parameters = json.load(c)["parameters"]

''' since working in local server'''
local_server = True  

app = Flask(__name__)

#necessary to have secret key in flask
app.secret_key = 'secret-key'

app.config['UPLOAD_FOLDER'] = parameters['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = parameters['gmail-user'],
    MAIL_PASSWORD=  parameters['gmail-password']
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = parameters['prod_uri']
    
db = SQLAlchemy(app)

class Contacts(db.Model):
    '''
    Sno,name,email,phoneNum,msg,date
    '''
    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50),  nullable=False)
    phoneNum = db.Column(db.String(15), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),nullable=True)
    

class Posts(db.Model):

    Sno = db.Column(db.Integer, primary_key=True)
    postTitle = db.Column(db.String(80), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(30),  nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12),nullable=True)  
    img_file = db.Column(db.String(20),nullable=True)     



@app.route('/')
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(parameters['no_of_posts']))
    #[0: parameters['no_of_posts']]
    #posts = posts[]
    page = request.args.get('page')
    if(not str(page).isnumeric()):
        page = 1
    page= int(page)
    posts = posts[(page-1)*int(parameters['no_of_posts']): (page-1)*int(parameters['no_of_posts'])+ int(parameters['no_of_posts'])]
    #Pagination Logic
    #First
    if (page==1):
        prev = "#"
        next = "/?page="+ str(page+1)
    elif(page==last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)



    return render_template('index.html', parameters=parameters, posts=posts, prev=prev, next=next)
   
@app.route('/about')
def about(): 
    return render_template('about.html', parameters=parameters)  

@app.route('/dashboard', methods=['GET','POST'])
def dashboard(): 
    #if user is already logged in
    if ('user' in session and session['user'] == parameters['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html',parameters = parameters , posts = posts)

    if request.method=='POST':
        username= request.form.get('uname')
        userpass= request.form.get('inputPass')
        if(username == parameters['admin_user'] and userpass == parameters['admin_password']):
           
            #set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html',parameters=parameters, posts = posts)
    
    return render_template('login.html', parameters=parameters)


@app.route("/post/<string:post_slug>",methods=['GET'])
def post_route(post_slug): 
    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html', parameters=parameters, post = post)        

@app.route('/edit/<string:Sno>',methods=['GET','POST'])
def edit(Sno):
    if ('user' in session and session['user'] == parameters['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('postTitle')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()

            if Sno == '0':
                post = Posts(postTitle = box_title, slug = slug, content =content, tagline =tline, img_file =img_file, date = date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(Sno=Sno).first()
                post.postTitle = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file  
                post.date = date
                db.session.commit()
                return redirect('/edit/'+Sno)
        post = Posts.query.filter_by(Sno=Sno).first()
        return render_template('edit.html', parameters = parameters, post = post, Sno=Sno)

@app.route('/contact',methods=['GET','POST'])
def contact(): 
    if(request.method == 'POST'):
        ''' Add entry to database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        entry = Contacts(name = name, phoneNum = phone, msg = message , email = email , date = datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from '+ name,
                            sender = email, 
                            recipients =[parameters['gmail-user']],
                            body = message + "\n" + phone)
        flash("Thanks for submitting your details. We will get back to you soon.", "success")
    return render_template('contact.html', parameters=parameters)

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if ('user' in session and session['user'] == parameters['admin_user']):
        if (request.method == 'POST'):
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))) #join the upload folder with filename
            return "Uploaded Successfully !"


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route('/delete/<string:Sno>',methods=['GET','POST'])
def delete(Sno):
    if ('user' in session and session['user'] == parameters['admin_user']):
        post = Posts.query.filter_by(Sno = Sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')


app.run(debug=True)  