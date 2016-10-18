from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def root():
  return app.send_static_file('index.html')

@app.route('/<path:path>')
def static_proxy(path):
  return app.send_static_file(path)

if __name__ == '__main__':
  app.run()
