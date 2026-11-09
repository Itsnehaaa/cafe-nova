from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Welcome.html')

@app.route('/menu')
def menu():

    item = request.args.get('item')
    size = request.args.get('size', 'regular')
    sugar = request.args.get('sugar', '0')

    return render_template(
        'Order.html',
        item=item,
        size=size,
        sugar=sugar
    )

if __name__ == '__main__':
    app.run(debug=True)