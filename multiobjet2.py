import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rotage2015002",
    database="projet1"
)
mycursor = mydb.cursor()

class MultiObjet:
    def __init__(self, multi_objet_id):
        self.multi_objet_id = multi_objet_id

    @staticmethod
    def getDescription(multi_objet_id): # this will help displaying the table
        sql = "SELECT * FROM multi_objet WHERE multi_objet_id = %s"
        mycursor.execute(sql, (multi_objet_id,))
        myresult = mycursor.fetchall()
        mydb.commit()
        return myresult[0][1]

    def inserer(self, description):
        sql = "INSERT INTO multi_objet (description) VALUES (%s)"
        mycursor.execute(sql,(description,))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, description):
        sql = "UPDATE multi_objet SET description = %s where multi_objet_id = %s"
        mycursor.execute(sql, (description,self.multi_objet_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM multi_objet WHERE multi_objet_id = %s"
        mycursor.execute(sql, (self.multi_objet_id,))
        mydb.commit()

class Navire(MultiObjet):
    def __init__(self, navire_id, multi_objet_id):
        super().__init__(multi_objet_id)
        self.navire_id = navire_id

    @staticmethod
    def getMultiObjetId(navire_id):# help to construct navire Object by only knowing navire_id-got from selection-
        sql = "SELECT * FROM navire WHERE navire_id = %s"
        mycursor.execute(sql, (navire_id,))
        myresult = mycursor.fetchall()
        mydb.commit()
        return myresult[0][1]

    def inserer(self, navire, description):
        mo = MultiObjet(0)
        self.multi_objet_id = mo.inserer(description)
        sql = "INSERT INTO navire (multi_objet_id, nom) VALUES (%s, %s)"
        mycursor.execute(sql, (self.multi_objet_id, navire))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, nom, description):
        mo = MultiObjet(self.multi_objet_id) #multi_objet_id is supposed to be set
        mo.modifier(description)
        sql = "UPDATE navire SET nom = %s where navire_id = %s"
        mycursor.execute(sql, (nom, self.navire_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM navire WHERE navire_id = %s"
        mycursor.execute(sql, (self.navire_id,))
        mydb.commit()
        mo = MultiObjet(self.multi_objet_id) #multi_objet_id is supposed to be set
        mo.supprimer()

class Marchandise(MultiObjet):
    def __init__(self, marchandise_id, multi_objet_id):
        super().__init__(multi_objet_id)
        self.marchandise_id = marchandise_id

    @staticmethod
    def getMultiObjetId(marchandise_id):# help to construct marchandise Object by only knowing marchandise_id-got from selection-
        sql = "SELECT * FROM marchandise WHERE marchandise_id = %s"
        mycursor.execute(sql, (marchandise_id,))
        myresult = mycursor.fetchall()
        mydb.commit()
        return myresult[0][1]

    def inserer(self, nature_marchandise, description):
        mo = MultiObjet(0)
        self.multi_objet_id = mo.inserer(description)
        sql = "INSERT INTO marchandise (multi_objet_id, nature_marchandise) VALUES (%s, %s)"
        mycursor.execute(sql, (self.multi_objet_id, nature_marchandise))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, nature_marchandise, description):
        mo = MultiObjet(self.multi_objet_id)
        mo.modifier(description)
        sql = "UPDATE marchandise SET nature_marchandise = %s where marchandise_id = %s"
        mycursor.execute(sql, (nature_marchandise, self.marchandise_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM marchandise WHERE marchandise_id = %s"
        mycursor.execute(sql, (self.marchandise_id,))
        mydb.commit()
        mo = MultiObjet(self.multi_objet_id)
        mo.supprimer()

