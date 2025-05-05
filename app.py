from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Find Largest Number</title>
</head>
<body>
    <h2>Enter three numbers</h2>
    <form method="post">
        A: <input type="number" name="a"><br><br>
        B: <input type="number" name="b"><br><br>
        C: <input type="number" name="c"><br><br>
        <input type="submit" value="Find Largest">
    </form>

    {% if result %}
        <h3>The largest number is: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        result = max(a, b, c)
    return render_template_string(HTML, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
