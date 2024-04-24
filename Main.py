from flask import Flask , render_template
from flask.templating import _render
app=Flask(__name__)
@app.route('/')
def homePage():
    return render_template('Index')

app.run(debug=True)
