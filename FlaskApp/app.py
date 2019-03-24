from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/calcular',methods=['POST'])
def calcular():
 
    # read the posted values from the UI
    _masa = request.form['masa']
    _largo = request.form['largo']
    _ancho = request.form['ancho']
    _espesor = request.form['espesor']

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == "__main__":
 app.run()

