from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/funnels', methods=['POST'])
def funnels():
    # TODO (dan): Funnel opening script here
    content = request.get_json()
    print content['funnels']
    return str(content['funnels'])

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run()
