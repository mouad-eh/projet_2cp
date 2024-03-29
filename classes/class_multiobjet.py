import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rotage2015002",
    database="projet_beta"
)
mycursor = mydb.cursor()

class MultiObjet:
    def __init__(self, multi_objet_id):
        self.multi_objet_id = multi_objet_id

    @staticmethod
    def getDescription(multi_objet_id): # this will help displaying the table
        # the subclasses are inherting this maybe i should fix that
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

class Camion(MultiObjet):
    def __init__(self, camion_id, multiobjet_id):
        super(Camion, self).__init__(multiobjet_id)
        self.camion_id = camion_id
    @staticmethod
    def getMultiObjetId(camion_id):# help to construct Camion Object by only knowing marchandise_id-got from selection-
        sql = "SELECT * FROM camion WHERE camion_id = %s"
        mycursor.execute(sql, (camion_id,))
        myresult = mycursor.fetchall()
        mydb.commit()
        return myresult[0][2]

    def inserer(self, matricule, disponibilite, description):
        mo = MultiObjet(0)
        self.multi_objet_id = mo.inserer(description)
        sql = "INSERT INTO camion (matricule, multi_objet_id, disponibilite) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (matricule, self.multi_objet_id, disponibilite))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, matricule, disponibilite, description):
        mo = MultiObjet(self.multi_objet_id)
        mo.modifier(description)
        sql = "UPDATE camion SET matricule = %s, disponibilite = %s where camion_id = %s"
        mycursor.execute(sql, (matricule, disponibilite, self.camion_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM camion WHERE camion_id = %s"
        mycursor.execute(sql, (self.camion_id,))
        mydb.commit()
        mo = MultiObjet(self.multi_objet_id)
        mo.supprimer()

class Emballage(MultiObjet):
    def __init__(self, emballage_id, client_id, dossier_id, multi_objet_id):
        super(Emballage, self).__init__(multi_objet_id)
        self.emballage_id = emballage_id
        self.client_id = client_id
        self.dossier_id = dossier_id

    @staticmethod
    def getMultiObjetId(emballage_id):# help to construct Emballage Object by only knowing marchandise_id-got from selection-
        # todo : i suppose to have static methods that can get client_id and dossier_id by only knowing names- got from line edits-
        sql = "SELECT * FROM emballage WHERE emballage_id = %s"
        mycursor.execute(sql, (emballage_id,))
        myresult = mycursor.fetchall()
        mydb.commit()
        return myresult[0][11]

    def inserer(self, num, num_emballage, genre_emballage, pieds, type_emballage,\
                date_livraison, date_restitution, num_bon_facture_restitution, description):
        mo = MultiObjet(0)
        self.multi_objet_id = mo.inserer(description)
        sql = "INSERT INTO emballage (client_id, dossier_id, num, num_emballage,\
         genre_emballage, pieds, type_emballage, date_livraison, date_restitution,\
          num_bon_facture_restitution, multi_objet_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, (self.client_id, self.dossier_id, num, num_emballage,\
                               genre_emballage, pieds, type_emballage, date_livraison, date_restitution,\
                               num_bon_facture_restitution , self.multi_objet_id))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, num, num_emballage, genre_emballage, pieds, type_emballage,\
                date_livraison, date_restitution, num_bon_facture_restitution, description):
        mo = MultiObjet(self.multi_objet_id)
        mo.modifier(description)
        sql = "UPDATE emballage SET num = %s, num_emballage = %s,\
         genre_emballage = %s, pieds = %s, type_emballage = %s, date_livraison = %s, date_restitution = %s,\
          num_bon_facture_restitution = %s, multi_objet_id = %s WHERE emballage_id = %s"
        mycursor.execute(sql, (num, num_emballage,\
                               genre_emballage, pieds, type_emballage, date_livraison, date_restitution,\
                               num_bon_facture_restitution , self.multi_objet_id, self.emballage_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM emballage WHERE emballage_id = %s"
        mycursor.execute(sql, (self.emballage_id,))
        mydb.commit()
        mo = MultiObjet(self.multi_objet_id)
        mo.supprimer()