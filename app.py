import os
import cgi
from flask import Flask, request
from jinja2 import Environment, FileSystemLoader


app = Flask(__name__)
env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
image_template = env.get_template('img.html')
home_template = env.get_template('home.html')


@app.route('/')
def imgcard():
    img = request.args.get('img', None)
    if img:
        return image_template.render(img=img)
    return home_template.render()


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
