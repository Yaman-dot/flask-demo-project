from flask import Flask, render_template_string, render_template, request
import pickle
import numpy as np
import math, time
app = Flask(__name__)
with open(r"D:\Documents\University\ThirdYear\First Semester\Applied Analytical Models\Labs\FlaskApp\models\model.pkl", 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    html = r"FlaskApp\templates\index.html"
    return render_template('index.html', name="Yaman Abulaban", age=22)

@app.route('/about')
def about():
    return """<p>This is the about page</p>

        <a href="/"> Home</a>
    """

@app.route('/user/<name>')
def user(name):
    return f"Hey there {name}"
@app.route('/square/<int:number>')
def square(number):
    return f"The square root of {number} is {number**2}"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"The sum of {a} and {b} is {a+b}"
@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    bp = float(request.form['bp'])
    chol = float(request.form['chol'])
    hr = float(request.form['hr'])
    
    features = np.array([[age, bp, chol, hr]])
    prediction = model.predict(features)[0]
    
    result = "Heart Disease" if prediction == 1 else "No Heart Disease"
    return render_template('result.html', result=result)
@app.route('/form')
def form():
    return render_template('form.html')
@app.route('/filters')
def filters():
    return render_template('filters.html', name="Sasha", price=12.412)
# 🌀 Donut animation (HTML + JS version)
@app.route('/donut')
def donut_page():
    html = """
    <html>
    <head>
      <title>ASCII Donut</title>
      <style>
        body {
          background: black;
          color: lime;
          font-family: monospace;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 100vh;
          overflow: hidden;
        }
        pre {
          font-size: 10px;
          line-height: 10px;
        }
      </style>
    </head>
    <body>
      <pre id="donut"></pre>
      <script>
        let A=1, B=1;
        const asciiframe=()=> {
          const b=[], z=[];
          A+=0.07; B+=0.03;
          const cA=Math.cos(A), sA=Math.sin(A), cB=Math.cos(B), sB=Math.sin(B);
          for(let k=0;k<1760;k++){b[k]=k%80==79?"\\n":" ";z[k]=0;}
          for(let j=0;j<6.28;j+=0.07){
            const ct=Math.cos(j),st=Math.sin(j);
            for(let i=0;i<6.28;i+=0.02){
              const sp=Math.sin(i),cp=Math.cos(i),h=ct+2,D=1/(sp*h*sA+st*cA+5),
              t=sp*h*cA-st*sA,x=0|(40+30*D*(cp*h*cB-t*sB)),
              y=0|(12+15*D*(cp*h*sB+t*cB)),o=x+80*y,
              N=0| (8*((st*sA-sp*ct*cA)*cB-sp*ct*sA-st*cA-sp*ct*cA));
              if(22>y&&y>0&&x>0&&80>x&&D>z[o]){
                z[o]=D;
                b[o]=".,-~:;=!*#$@"[N>0?N:0];
              }
            }
          }
          document.getElementById("donut").innerHTML=b.join("");
        }
        setInterval(asciiframe, 50);
      </script>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run()
