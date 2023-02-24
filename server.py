from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])         
def checkout():
    selected_fruits = []
    total_quantity = 0
    for fruit in ['strawberry', 'raspberry', 'apple', 'blueberry']:
        quantity = int(request.form.get(fruit, 0))
        if quantity >0:
            selected_fruits.append({'name': fruit, 'quantity' : int(quantity)})
            total_quantity += int(quantity)
    first_name = request.form["first_name"]
    last_name= request.form['last_name']
    student_id = request.form['student_id']
    current_time = datetime.now().strftime('%B %d, %Y %I:%M:%S %p')
    print(f"Charging {first_name} {last_name} for {total_quantity} fruits")

    return render_template("checkout.html", first_name=first_name, last_name=last_name, student_id=student_id, selected_fruits=selected_fruits, total_quantity = total_quantity, current_time=current_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    