from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

@app.route('/')
def index():
    ##########Best Books names#########

    beststory1 = "Histoire 01"
    beststory2 = "Histoire 02"
    beststory3 = "Histoire 03"

    ##########Best Books prices#########

    beststory1price = 0
    beststory2price = 0
    beststory3price = 0

    ####################################

    if (beststory1price == 0):
        beststory1price = str(beststory1price)
        beststory1price = "Gratuit"
    else:
        beststory1price = str(beststory1price)
        beststory1price = beststory1price + " MAD"
    if (beststory2price == 0):
        beststory2price = str(beststory2price)
        beststory2price = "Gratuit"
    else:
        beststory2price = str(beststory2price)
        beststory2price = beststory2price + " MAD"
    if (beststory3price == 0):
        beststory3price = str(beststory3price)
        beststory3price = "Gratuit"
    else:
        beststory3price = str(beststory3price)
        beststory3price = beststory3price + " MAD"
    return render_template("index.html", beststory1=beststory1, beststory2=beststory2, beststory3=beststory3, beststory1price=beststory1price, beststory2price=beststory2price, beststory3price=beststory3price)
@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/seconnecter', methods=['GET', 'POST'])
def seconnecter():
    if request.method == 'POST':
        userDetails = request.from
        name = userDetails['name']
        email = userDetails['email']
        password = userDetails['password']
    return render_template('seconnecter.html')
if __name__ == "__main__":
    app.run(debug=True)
