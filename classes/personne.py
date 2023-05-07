import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rotage2015002",
    database="projet_beta"
)
mycursor = mydb.cursor()

class Personne:
    def __init__(self, personne_id):
        self.personne_id = personne_id

    def inserer(self, nom, prenom, tel, email, adresse):
        sql = "INSERT INTO personne (nom, prenom, tel, email, adresse) VALUES (%s, %s, %s, %s, %s)"
        val = (nom, prenom, tel, email, adresse)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self,  nom, prenom, tel, email, adresse):
        sql = "UPDATE personne SET nom=%s, prenom=%s, tel=%s, email=%s, adresse=%s where id=%s"
        val = ( nom, prenom, tel, email, adresse, self.personne_id)
        mycursor.execute(sql, val)
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM personne WHERE id=%s"
        mycursor.execute(sql, (self.personne_id,))
        mydb.commit()

class Utilisateur(Personne):
    def __init__(self, utilisateur_id, personne_id):
        super().__init__(personne_id)
        self.utilisateur_id = utilisateur_id

    @staticmethod
    def getPersonneId(utilisateur_id):
        sql = "SELECT * FROM utilisateur WHERE utilisateur_id=%s"
        mycursor.execute(sql, (utilisateur_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO utilisateur(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id, ))
        mydb.commit()
        return mycursor.lastrowid


    def modifier(self,nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE utilisateur SET personne_id=%s WHERE utilisateur_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.utilisateur_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM utilisateur WHERE utilisateur_id=%s"
        mycursor.execute(sql, (self.utilisateur_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()


class Represantant(Personne):
    def __init__(self, represantant_id, personne_id):
        super().__init__(personne_id)
        self.represantant_id = represantant_id

    @staticmethod
    def getPersonneId(represantant_id):
        sql = "SELECT * FROM representant WHERE representant_id=%s"
        mycursor.execute(sql, (represantant_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO representant(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id, ))
        mydb.commit()
        return mycursor.lastrowid


    def modifier(self,nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE representant SET personne_id=%s WHERE representant_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.represantant_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM representant WHERE representant_id=%s"
        mycursor.execute(sql, (self.represantant_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()



class Expert(Personne):
    def __init__(self, expert_id, personne_id):
        super().__init__(personne_id)
        self.expert_id = expert_id

    @staticmethod
    def getPersonneId(expert_id):
        sql = "SELECT * FROM expert WHERE expert_id=%s"
        mycursor.execute(sql, (expert_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO expert(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id, ))
        mydb.commit()
        return mycursor.lastrowid


    def modifier(self,nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE expert SET personne_id=%s WHERE expert_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.expert_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM expert WHERE expert_id=%s"
        mycursor.execute(sql, (self.expert_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()


class Douanier(Personne):
    def __init__(self, douanier_id, personne_id):
        super().__init__(personne_id)
        self.douanier_id = douanier_id

    @staticmethod
    def getPersonneId(douanier_id):
        sql = "SELECT * FROM douanier WHERE douanier_id=%s"
        mycursor.execute(sql, (douanier_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO douanier(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id,))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE douanier SET personne_id=%s WHERE douanier_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.douanier_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM douanier WHERE douanier_id=%s"
        mycursor.execute(sql, (self.douanier_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()


class Declarant(Personne):
    def __init__(self, declarant_id, personne_id):
        super().__init__(personne_id)
        self.declarant_id = declarant_id

    @staticmethod
    def getPersonneId(declarant_id):
        sql = "SELECT * FROM declarant WHERE declarant_id=%s"
        mycursor.execute(sql, (declarant_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO declarant(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id,))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE declarant SET personne_id=%s WHERE declarant_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.declarant_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM declarant WHERE declarant_id=%s"
        mycursor.execute(sql, (self.declarant_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()

class Chauffeur(Personne):
    def __init__(self, chauffeur_id, personne_id):
        super().__init__(personne_id)
        self.chauffeur_id = chauffeur_id

    @staticmethod
    def getPersonneId(chauffeur_id):
        sql = "SELECT * FROM chauffeur WHERE chauffeur_id=%s"
        mycursor.execute(sql, (chauffeur_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, nom, prenom, tel, email, adresse):
        personne = Personne(0)
        self.personne_id = personne.inserer(nom, prenom, tel, email, adresse)
        sql = "INSERT INTO chauffeur(personne_id) VALUES (%s)"
        mycursor.execute(sql, (self.personne_id,))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, nom, prenom, tel, email, adresse):
        personne = Personne(self.personne_id)
        personne.modifier(nom, prenom, tel, email, adresse)
        sql = "UPDATE chauffeur SET personne_id=%s WHERE chauffeur_id=%s"
        mycursor.execute(sql, (personne.personne_id, self.chauffeur_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM chauffeur WHERE chauffeur_id=%s"
        mycursor.execute(sql, (self.chauffeur_id,))
        mydb.commit()
        personne = Personne(self.personne_id)
        personne.supprimer()

