from application import app, db, api
from flask import render_template, request, json, jsonify, Response,flash,redirect,url_for,session
from application.models import User,Courses,Enrollment
from application.forms import LoginForm, RegisterForm
from flask_restx import Resource

##################################
@api.route('/api','/api/')
class GetAndPost(Resource):
    #Get All
    def get(self):
        return jsonify(User.objects.all())

    #Post
    def post(self):
        data = api.payload
        user = User(user_id=data['user_id'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        user.set_password(data['password'])
        user.save()
        return jsonify(User.objects(user_id=data['user_id']))

@api.route('/api/<index>')   
class GetUpdateDelete(Resource):
    #Get One
    def get(self,index):
        return jsonify(User.objects(user_id=index))
    
    #Put
    def put(self,index):
        data = api.payload
        User.objects(user_id=index).update(**data)
        return jsonify(User.objects(user_id=index))


    #Delete
    def delete(self,index):
        User.objects(user_id=index).delete()
        return jsonify("User was removed sucessfully!")
##################################

@app.route("/")
@app.route("/home")
@app.route("/index")
def index ():
    return render_template("index.html", index = True) 

@app.route("/courses")
@app.route("/courses/<term>")
def courses (term=2025):
    classes = Courses.objects.all()
    return render_template("courses.html", courseData = classes, courses = True, term=term)

@app.route("/enrollment", methods=["GET","POST"])
def enrollment ():
    if not session.get('username'):
        return redirect(url_for('login'))
    
    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    # Note for later: Try and implement Flask-login extension
    # https://flask-login.readthedocs.io/en/latest/
    
    user_id = session.get('user_id')

    if not user_id:
        flash("You must be logged in to enroll.", "danger")
        return redirect(url_for('login'))
    
    if courseID:
        if Enrollment.objects(user_id=user_id,courseID=courseID):
            flash(f"Hey, you're already registered for this course {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id,courseID=courseID).save()
            flash(f"You succefully enrolled in {courseTitle}!", "success")
    
    def class_list():
        classes = list(User.objects.aggregate(*[
                {
                    '$lookup': {
                        'from': 'enrollment', 
                        'localField': 'user_id', 
                        'foreignField': 'user_id', 
                        'as': 'result1'
                    }
                }, {
                    '$unwind': {
                        'path': '$result1', 
                        'includeArrayIndex': 'result1_id', 
                        'preserveNullAndEmptyArrays': False
                    }
                }, {
                    '$lookup': {
                        'from': 'courses', 
                        'localField': 'result1.courseID', 
                        'foreignField': 'courseID', 
                        'as': 'result2'
                    }
                }, {
                    '$unwind': {
                        'path': '$result2', 
                        'preserveNullAndEmptyArrays': False
                    }
                }, {
                    '$match': {
                        'user_id': user_id
                    }
                }, {
                    '$sort': {
                        'courseID': 1
                    }
                }
            ]))
        
        return classes
    
    classes = class_list()
    # print("User ID:", user_id)
    # print("Classes:", class_list)
    return render_template("enrollment.html", enrollment = True, title = "Enrollment", classes = classes) 

@app.route("/login", methods = ['GET','POST'])
def login ():
    if session.get('username'):
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit()==True:
        email = form.email.data
        password = form.password.data
        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, You Successfully Logged In!","success")
            session['user_id'] = user.user_id
            session["username"] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, Something Was Not Right.","danger")
    return render_template("login.html", title="Login", form=form, login = True) 

@app.route("/register", methods = ['POST','GET'])
def register ():
    if session.get('username'):
        return redirect(url_for('index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash(f'You did it {user.first_name}! You are registered!','success')
        return redirect(url_for("index"))
    return render_template("register.html", title="New User Registration", form = form, register = True) 

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username',None)
    return redirect(url_for('index'))


# @app.route("/api/")
# @app.route("/api/<idx>")
# def api(idx=None):
#     courseData = Courses.objects.all()
#     if(idx==None):
#         jdata = courseData
#     else:
#         jdata = courseData[int(idx)]
#     return Response(json.dumps(jdata), mimetype="application/json")

@app.route("/user")
def user():
     #User(user_id=1, first_name="Dan", last_name="Burs", email="DanBurs@blt.com", password="strongpassword").save()
     users = User.objects.all()
     return render_template("user.html", users=users)