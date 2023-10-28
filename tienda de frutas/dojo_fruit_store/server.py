from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    # Captura los datos del formulario
    strawberry_quantity = int(request.form['strawberry_quantity'])
    raspberry_quantity = int(request.form['raspberry_quantity'])
    apple_quantity = int(request.form['apple_quantity'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    payment_method = request.form['payment']
    total_fruits = strawberry_quantity + raspberry_quantity + apple_quantity
    print(f"Cobrando a {first_name} por {total_fruits} frutas. Método de pago: {payment_method}")
    return render_template("checkout.html", strawberry=strawberry_quantity, raspberry=raspberry_quantity, apple=apple_quantity, first_name=first_name, last_name=last_name, student_id=student_id)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__ == "__main__":
    app.run(debug=True)


