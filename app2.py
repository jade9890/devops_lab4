from flask import Flask, request, render_template_string 

from calculate import Calculations 

app2 = Flask(__name__) 

 

 

# Simple HTML template 

TEMPLATE = """ 

<!DOCTYPE html> 

<html> 

<head> 

    <title>Lab 4 Calculator</title> 

</head> 

<body> 

    <h1>Hello, Welcome to Lab 4</h1> 

    <form method="post"> 

        <label>Enter first number:</label> 

        <input type="number" name="a" step="any" required><br><br> 

        <label>Enter second number:</label> 

        <input type="number" name="b" step="any" required><br><br> 

        <button type="submit">Calculate</button> 

    </form> 

    {% if results %} 

        <h2>Results:</h2> 

        <ul> 

            <li>Sum: {{ results['sum'] }}</li> 

            <li>Difference: {{ results['difference'] }}</li> 

            <li>Product: {{ results['product'] }}</li> 

            <li>Quotient: {{ results['quotient'] }}</li> 

        </ul> 

    {% endif %} 

</body> 

</html> 

""" 

 

@app2.route("/", methods=["GET", "POST"]) 

def home(): 

    results = None 

    if request.method == "POST": 

        try: 

            a = float(request.form["a"]) 

            b = float(request.form["b"]) 

            calc = Calculations(a, b) 

            results = { 

                "sum": calc.get_sum(), 

                "difference": calc.get_difference(), 

                "product": calc.get_product(), 

                "quotient": calc.get_quotient(), 

            } 

        except Exception as e: 

            results = {"error": str(e)} 

 

    return render_template_string(TEMPLATE, results=results) 

 

if __name__ == "__main__": 

    app2.run(host="0.0.0.0", port=5000) 
