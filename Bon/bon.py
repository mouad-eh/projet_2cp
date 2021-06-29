import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nednassim2001",
    database="projet1"
)
mycursor = mydb.cursor()

class Bon:
    def __init__(self, bon_id):
        self.bon_id = bon_id

    def inserer(self, declarant, num_dossier, date, agent, transit):
        sql = "INSERT INTO bon (declarant, num_dossier, date, agent, transit) VALUES (%s, %s, %s, %s, %s)"
        val = (declarant, num_dossier, date, agent, transit)
        mycursor.execute(sql, val)
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, declarant, num_dossier, date, agent, transit):
        sql = "UPDATE bon SET declarant=%s, num_dossier=%s, date=%s, agent=%s, transit=%s where bon_id=%s"
        val = (declarant, num_dossier, date, agent, transit, self.bon_id)
        mycursor.execute(sql, val)
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM bon WHERE bon_id=%s"
        mycursor.execute(sql, (self.bon_id,))
        mydb.commit()

class Bon_sortie(Bon):
    def __init__(self, bon_sortie_id, bon_id):
        super().__init__(bon_id)
        self.bon_sortie_id = bon_sortie_id

    @staticmethod
    def getBonId(bon_sortie_id):
        sql = "SELECT * FROM bon_sortie WHERE sortie_id=%s"
        mycursor.execute(sql, (bon_sortie_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, declarant, num_dossier, date, agent, transit):
        bon = Bon(0)
        self.bon_id = bon.inserer(declarant, num_dossier, date, agent, transit)
        sql = "INSERT INTO bon_sortie(bon_id) VALUES (%s)"
        mycursor.execute(sql, (self.bon_id, ))
        mydb.commit()
        return mycursor.lastrowid


    def modifier(self, declarant, num_dossier, date, agent, transit):
        bon = Bon(self.bon_id) 
        bon.modifier(declarant, num_dossier, date, agent, transit)
        sql = "UPDATE bon_sortie SET bon_id=%s WHERE sortie_id=%s"        
        mycursor.execute(sql, (bon.bon_id, self.bon_sortie_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM bon_sortie WHERE sortie_id=%s"
        mycursor.execute(sql, (self.bon_sortie_id,))
        mydb.commit()
        bon = Bon(self.bon_id) 
        bon.supprimer()

class Bon_visite(Bon):
    def __init__(self, bon_visite_id, bon_id):
        super().__init__(bon_id)
        self.bon_visite_id = bon_visite_id

    @staticmethod
    def getBonId(bon_visite_id):
        sql = "SELECT * FROM bon_visite WHERE visite_id=%s"
        mycursor.execute(sql, (bon_visite_id,))
        myresult = mycursor.fetchall()
        return myresult[0][1]

    def inserer(self, declarant, num_dossier, date, agent, transit):
        bon = Bon(0)
        self.bon_id = bon.inserer(declarant, num_dossier, date, agent, transit)
        sql = "INSERT INTO bon_visite(bon_id) VALUES (%s)"
        mycursor.execute(sql, (self.bon_id, ))
        mydb.commit()
        return mycursor.lastrowid

    def modifier(self, declarant, num_dossier, date, agent, transit):
        bon = Bon(self.bon_id) 
        bon.modifier(declarant, num_dossier, date, agent, transit)
        sql = "UPDATE bon_visite SET bon_id=%s WHERE visite_id=%s"
        mycursor.execute(sql, (bon.bon_id, self.bon_visite_id))
        mydb.commit()

    def supprimer(self):
        sql = "DELETE FROM bon_visite WHERE visite_id=%s"
        mycursor.execute(sql, (self.bon_visite_id,))
        mydb.commit()
        bon = Bon(self.bon_id) 
        bon.supprimer()
