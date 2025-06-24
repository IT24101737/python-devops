from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

list = Flask(__name__)
list.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mylist.sqlite'
list.config ['SQLALCHEMY_TRACK_MODIFICATION']=False
db = SQLAlchemy(list)

class MyList(db.Model):
   c_id=db.Column(db.Integer,primary_key=True)
   c_name=db.Column(db.String(500))

@list.route('/')
def home():
    return 'Welcome to GOOD LIST'


@list.route('/insert',methods=['POST'])
def home2():
    c_name=request.form.get('c_name')
    new_c_name = Myapp(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()
    return redirect(url_for('home1'))

@list.route("/delete/<int:c_id>")
def delete(c_id):
    c_name=Mylist.query.get_or_404('c_name')
    db.session.delete(c_name)
    db.session.commit()
    return redirect(url_for('home1'))

@list.route('/base1')
def home1():
    my_list=Mylist.query.all()
    var="Hello this is variable"
    return render_template("base.html", var=var, my_list=my_list)

if __name__=='__main__':
    list.run()


