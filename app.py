from flask import Flask, render_template
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms import validators

class MyForm(Form):
    name = StringField('name', validators=[validators.DataRequired()])
    select = SelectField('Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])

SECRET_KEY = 'secret'
HOST='0.0.0.0'
PORT=5000

app = Flask(__name__)
app.config.from_object(__name__)

# /bung is the app route ie. http://192.168.10.1:5000/bung
@app.route('/bung', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        print "wow, I got '%s' lang '%s'" % (form.name.data, form.select.data)
    return render_template('submit.html', form=form)


# this runs a debugging web server. IF there is an error it brings up a pythond debugger in the current page
if __name__ == "__main__":
    app.run(debug=True, host=app.config['HOST'], port=app.config['PORT'])
