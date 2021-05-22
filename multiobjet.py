import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="projet"
)
mycursor = mydb.cursor()

#La classe parent
class MultiObjet:
    def __init__(self, id, description):
        self.id = id
        self.description = description


#Objet Marchandise :
class Marchandise(MultiObjet):
    # le constructeur de la classe Marchandise
    def __init__(self, marchandise_id, type, description):
        MultiObjet.__init__(self, marchandise_id, description)
        self.type = type


    # la methode existe pour verifier l'existence de la marchandise dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM marchandises WHERE marchandise_id = %s "
        mycursor.execute(sql, (self.id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    # la methode inserer pour inserer une marchandise dans la base de donnees
    def inserer(self):
        if not Marchandise.existe(self):
            sql = "INSERT INTO marchandises(marchandise_id, type, description) VALUES (%s, %s, %s)"
            sauv = (self.id, self.type, self.description)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : Marchandise existante!")


    # la methode modifier_type() pour modifier le type d'une marchandise dans la base de donnees
    def modifier_type(self, description):
        if Marchandise.existe(self):
            sql = "UPDATE marchandises SET type = %s where marchandise_id = %s"
            sauv = (description, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Marchandise inexistante!")


    # la methode modifier_descr() pour modifier la description d'une marchandise dans la base de donnees
    def modifier_descr(self, description):
        if Marchandise.existe(self):
            sql = "UPDATE marchandises SET description = %s where marchandise_id = %s"
            sauv = (description, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Marchandise inexistante!")

    #La methode supp() pour supprimer la marchendise de la base de donnees
    def supp(self):
        if Marchandise.existe(self):
           sql = "DELETE FROM marchandises WHERE marchandise_id = %s"
           mycursor.execute(sql, (self.id,))
           mydb.commit()
           print("Suppression avec succes!")
        else :
           print("Suppression avec echec : Marchandise inexistante!")


#l'objet Camion
class Camion(MultiObjet):
    #le constructeur de la classe Camion
    def __init__(self, camion_id, description, disponibilite):
        MultiObjet.__init__(self, camion_id, description)
        self.disponibilite = disponibilite

    # la methode existe() pour verifier l'existence du camion dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM camions WHERE camion_id = %s"
        mycursor.execute(sql, (self.id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else: # s'il existe
            bool = True
        return bool

    # la methode inserer() pour inserer un camion dans la base de donnees
    def inserer(self):
        if not Camion.existe(self):  # ss'il n'existe pas
            sql = "INSERT INTO camions(camion_id, description, disponibilite) VALUES (%s, %s, %s)"
            sauv = (self.id, self.description, self.disponibilite)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
        else:
         print("Insertion avec echec : Camion existant!")

    # la methode supp() pour supprimer le camion de la base de donnees
    def supp(self):
        if Camion.existe(self):
            sql = "DELETE FROM camions WHERE camion_id = %s"
            mycursor.execute(sql, (self.id, ))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec : Camion inexistant!")

    # la methode modifier_descr() pour modifier la description d'un camion dans la base de donnees
    def modifier_descr(self, description):
        if Camion.existe(self):
            sql = "UPDATE camions SET description = %s WHERE camion_id = %s"
            sauv = (description, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Camion inexistant!")


    # la methode modifier_disp() pour modifier la disponibilite d'un camion dans la base de donnees
    def modifier_dispo(self, disponibilite):
        if Camion.existe(self):
            sql = "UPDATE camions SET disponibilite = %s WHERE camion_id = %s"
            sauv = (disponibilite, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Camion inexistant!")

#Objet Conteneur
class Conteneur(MultiObjet):
    #le constructeur de la classe Conteneur
    def __init__(self, conteneur_id, description, fraude):
        MultiObjet.__init__(self, conteneur_id, description)
        self.fraude = fraude

    # la methode existe() pour verifier l'existence du conteneur dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM conteneurs WHERE conteneur_id = %s"
        mycursor.execute(sql, (self.id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0: # s'il n'existe pas
            bool = False
        else: # s'il existe
            bool = True
        return bool

    # la methode inserer() pour inserer un conteneur dans la base de donnees
    def inserer(self):
        if not Conteneur.existe(self):  # ss'il n'existe pas
            sql = "INSERT INTO conteneurs(conteneur_id, description,fraude) VALUES (%s, %s, %s)"
            sauv = (self.id, self.description, self.fraude)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : Conteneur existant!")

    # la methode supp() pour supprimer un conteneur de la base de donnees
    def supp(self):
        if Conteneur.existe(self):
            sql = "DELETE FROM conteneurs WHERE conteneur_id = %s"
            mycursor.execute(sql, (self.id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec : Conteneur inexistant!")

    # la methode modifier_descr() pour modifier la description d'un conteneur dans la base de donnees
    def modifier_descr(self, description):
        if Conteneur.existe(self):
            sql = "UPDATE conteneurs SET description = %s WHERE conteneur_id = %s"
            sauv = (description, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Conteneur inexistant!")

    # la methode modifier_fraude() pour modifier le d'un conteneur dans la base de donnees
    def modifier_fraude(self, fraude):
        if Conteneur.existe(self):
            sql = "UPDATE conteneurs SET fraude=%s WHERE conteneur_id = %s"
            sauv = (fraude, self.id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Conteneur inexistant!")


#l'objet Designation
class Designation:
    #le constructeur de la classe Designation
    def __init__(self, designation_id, prixUnit, typeDebours):
        self.designation_id = designation_id
        self.prix_unit = prixUnit
        self.type_debours = typeDebours

    #la methode existe() pour verifier l'existence de la designation dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM designations WHERE designation_id = %s"
        mycursor.execute(sql, (self.designation_id, ))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  #s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    #la methode inserer() pour inserer une designation dans la base de donnees
    def inserer(self):
        if not Designation.existe(self):
            sql = "INSERT INTO designations(designation_id, prix_unit, type_debours) VALUES (%s, %s, %s)"
            val = (self.designation_id, self.prix_unit, self.type_debours)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : Designation existante!")

    # la methode supp() pour supprimer une designation de la base de donnees
    def supp(self):
        if Designation.existe(self):
            sql = "DELETE FROM designations WHERE designation_id = %s"
            mycursor.execute(sql, (self.designation_id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec : Designation inexistante!")

    # la methode modifier_prix() pour modifier le prix d'une designation dans la base de donnees
    def modifier_prix(self, prix):
        if Designation.existe(self):
            sql = "UPDATE designations SET prix_unit = %s WHERE designation_id = %s"
            sauv = (prix, self.designation_id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Designation inexistante!")

    # la methode modifier_debours() pour modifier le type de debours d'une designation dans la base de donnees
    def modifier_debours(self, debours):
        if Designation.existe(self):
            sql = "UPDATE designations SET type_debours = %s WHERE designation_id = %s"
            sauv = (debours, self.designation_id)
            mycursor.execute(sql, sauv)
            mydb.commit()
            print("Modification avec succes!")
        else:
            print("Modification avec echec : Designation inexistante!")

#Objet Provenance :
class Provenance:
    # le constructeur de la classe Provenance
    def __init__(self, provenance_id, nom):
        self.provenance_id = provenance_id
        self.nom = nom

    # la methode existe() pour verifier l'existence de la provenance dans la base de donnees
    def existe(self):
        sql = "SELECT * FROM provenances WHERE provenance_id = %s"
        mycursor.execute(sql, (self.provenance_id,))
        myresult = mycursor.fetchall()
        row_count = mycursor.rowcount

        if row_count == 0:  # s'il n'existe pas
            bool = False
        else:  # s'il existe
            bool = True
        return bool

    # la methode inserer() pour inserer une provenance dans la base de donnees
    def inserer(self):
        if not Provenance.existe(self):
            sql = "INSERT INTO provenances(provenance_id, nom) VALUES (%s, %s)"
            val = (self.provenance_id, self.nom)
            mycursor.execute(sql, val)
            mydb.commit()
            print("Insertion avec succes!")
        else:
            print("Insertion avec echec : Provenance existante!")

    # la methode supp() pour supprimer une provenance de la base de donnees
    def supp(self):
        if Provenance.existe(self):
            sql = "DELETE FROM provenances WHERE provenance_id = %s"
            mycursor.execute(sql, (self.provenance_id,))
            mydb.commit()
            print("Suppression avec succes!")
        else:
            print("Suppression avec echec : Provenance inexistante!")


#march = Marchandise(4, 'HHHH', 'nnnn')
#march.inserer()
#march.supp()
#res = march.existe()
#print(res)
#march.modifier_type('SSSS')
#march.modifier_descr('ssss')

#cam = Camion(4, 'Chevrolet2013', 'I')
#cam.inserer()
#cam.supp()
#res = cam.existe()
#print(res)
#cam.modifier_descr('Mercedes1987')
#cam.modifier_dispo('I')

#con = Conteneur(4, 'AAAA', 'xxxx')
#con.inserer()
#con.supp()
#res = con.existe()
#print(res)
#con.modifier_descr('BBBB')
#con.modifier_fraude('gggg')

#des = Designation(2, 13.50 , 'xxxx')
#des.inserer()
#des.supp()
#res = des.existe()
#print(res)
#des.modifier_prix(10.5)
#des.modifier_debours('XXXX')

#pro = Provenance(4, 'Algerie')
#res = pro.existe()
#print(res)
#pro.inserer()
#pro.supp()