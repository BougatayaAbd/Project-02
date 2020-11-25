from flask import Flask,render_template

app = Flask(__name__)

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