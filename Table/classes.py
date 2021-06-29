import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nednassim2001",
    database="projet"
)
mycursor = mydb.cursor()


#La classe Pays
class Pays():
    # le constructeur de la classe Pays
    def __init__(self, pays_id):
        self.pays_id = pays_id
    
    #Methode existe() pour verifier si le pays existe dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM pays WHERE pays_id = %s"
        mycursor.execute(sql, (self.pays_id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    #Methode inserer() pour inserer un pays dans la base de donnees
    def inserer(self, code_pays, libelle):
        sql = "INSERT INTO pays (code_pays, libelle) VALUES (%s, %s)"
        val = (code_pays, libelle)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.lastrowid

    #Methode modifier() pour modifier un pays dans la base de donnees
    def modifier(self, code_pays, libelle):
        sql = "UPDATE pays SET code_pays = %s, libelle = %s WHERE pays_id = %s"
        mycursor.execute(sql, (code_pays, libelle, self.pays_id))
        mydb.commit()

    #Methode supprimer() pour supprimer un pays de la base de donnees 
    def supprimer(self):
        sql = "DELETE FROM pays WHERE pays_id = %s"
        mycursor.execute(sql, (self.pays_id,))
        mydb.commit()

#La classe Monnaie
class Monnaie():
    # le constructeur de la classe Monnaie
    def __init__(self, monnaie_id):
        self.monnaie_id = monnaie_id

    #Methode existe() pour verifier si la monnaie existe dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM monnaie WHERE monnaie_id = %s"
        mycursor.execute(sql, (self.monnaie_id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    #Methode inserer() pour inserer un monnaie dans la base de donnees
    def inserer(self, code_monnaie, libelle_monnaie, taux_change):
        sql = "INSERT INTO monnaie (code_monnaie, libelle_monnaie, taux_change) VALUES (%s, %s, %s)"
        val = (code_monnaie, libelle_monnaie, taux_change)
        mycursor.execute(sql, val)
        mydb.commit()

    #Methode modifier() pour modifier un monnaie dans la base de donnees
    def modifier(self, code_monnaie, libelle_monnaie, taux_change):
        sql = "UPDATE monnaie SET code_monnaie = %s, libelle_monnaie = %s, taux_change =%s where monnaie_id = %s"
        mycursor.execute(sql, (code_monnaie, libelle_monnaie, taux_change, self.monnaie_id))
        mydb.commit()

    #Methode supprimer() pour supprimer un monnaie de la base de donnees 
    def supprimer(self):
        sql = "DELETE FROM monnaie WHERE monnaie_id = %s"
        mycursor.execute(sql, (self.monnaie_id, ))
        mydb.commit()
