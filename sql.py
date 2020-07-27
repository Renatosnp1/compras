import sqlite3

class CreateTable():
    
        
    def createListshopping(self):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute(""" create table if not exists lista_compras(
            id integer not null primary key autoincrement,
            produto text not null,
            quantidade integer,
            preco float,
            total float);""")
        
        self.conn.close()   
        


class Addata():
    
        
    def addlistshopping(self, produto=None, quantidade=None, preco=None, total=None):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        if quantidade and preco:
            total = int(quantidade) * float(preco)
        else:
            quantidade = 0
            preco = 0.0
            total= 0
        
        self.cur.execute(""" insert into lista_compras (produto, quantidade, preco, total)
                         values (?, ?, ?, ?)""", [produto.upper(), quantidade, preco, total])
        self.conn.commit()
        self.conn.close()   
        
        
        
        
        
        
class Consultadb():
    
        
    def consultaListaCompras(self):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute(""" select * from  lista_compras order by produto ASC""")
        
        lista = self.cur.fetchall()
        self.conn.close()
        return lista
    
    
    def consultaItem(self, id):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute("select * from lista_compras where id="+str(id))
        
        lista = self.cur.fetchall()[0]
        self.conn.close()
        return lista
    
    
    def consultaSomaCompras(self):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute(""" select SUM(total) from  lista_compras """)
        
        lista = self.cur.fetchall()[0][0]
        self.conn.close()
        return lista
    
    
    
    
    
    
    
class DeleteData():

    
    def delete(self, id):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        self.cur.execute("delete from lista_compras where id="+str(id))
        self.conn.commit()   
        self.conn.close()
    
    


class UpdateData():
    
    
    def update(self, produto, quantidade, preco, id):
        self.conn = sqlite3.connect('banco.db')
        self.cur = self.conn.cursor()
        
        total = "%.2f" % (int(quantidade) * float(preco))
        
        
        self.cur.execute("""update lista_compras set produto=?, 
                         quantidade=?, 
                         preco=?, 
                         total=? 
                         where id=?""", (produto.upper(), quantidade, preco, total, id))
        
        self.conn.commit()
        self.conn.close()  