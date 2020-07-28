from flask import Flask, render_template, url_for, redirect, request
from sql import Consultadb, Addata, DeleteData, UpdateData

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lista/')
def lista():
    consuta_db = Consultadb()
    compras = consuta_db.consultaListaCompras()
    total = consuta_db.consultaSomaCompras()
    if not total:
        total = 0
    return render_template('lista.html', compras=compras, total="%.2f" % total ) 



@app.route('/adicionar/')
def adicionar():
    return render_template('cadastro.html')





@app.route('/salvarbanco/', methods=["GET", "POST"])
def salvarbanco():
    
    if request.method == "POST":
        produto = request.form['produto']
        quantidade = request.form['quantidade']
        valor = request.form['valor']
        if produto != "":
            s = Addata()
            
            if quantidade and valor:
                quantidade = int(quantidade)
                valor = "%.2f" % float(valor)
                
            s.addlistshopping(produto, quantidade, valor)
        
            # return redirect(url_for('adicionar'))
    
    return redirect(url_for('adicionar'))




@app.route('/lista/delete/<int:id>')
def delete(id):
    d = DeleteData()
    d.delete(id)
    return redirect(url_for('lista'))




@app.route('/update/<id>')
def update(id=None):
    consuta_db = Consultadb()
    item = consuta_db.consultaItem(id)
    return render_template('cadastroupdate.html', item=item)



@app.route('/updatedb/<int:id>', methods=["GET", "POST"])
def updatedb(id):
    if request.method == "POST":
        produto = request.form["produto"]
        quantidade = request.form["quantidade"]
        valor = request.form["valor"]
        
        up = UpdateData()
        up.update(produto, int(quantidade), float(valor), id)
        
        return redirect(url_for('lista'))
    
    
    
if __name__ =="__main__":
    app.run(debug=True)
    