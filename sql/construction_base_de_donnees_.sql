CREATE DATABASE projet_beta;
USE projet_beta;
-- Entreprise
CREATE TABLE entreprise (
	  entreprise_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	 
	  nom VARCHAR(20) NOT NULL , 
	  type VARCHAR(20) ,
	  adresse VARCHAR(20) NOT NULL ,
	  tel1 VARCHAR(20) ,
	  tel2 VARCHAR(20) ,
	  tel3 VARCHAR(20) ,
	  mob1 VARCHAR(20) ,
	  mob2 VARCHAR(20) ,
	  mob3 VARCHAR(20) ,
	  fax1 VARCHAR(20) ,
	  fax2 VARCHAR(20) ,
	  email VARCHAR(20) ,
	  siteweb VARCHAR(20) ,
	  observation VARCHAR(20) 
);

-- Documents
CREATE TABLE document (
	  document_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      nbr_clients INT NOT NULL ,
	  date_document DATE NOT NULL,
	  date_exp_document DATE NOT NULL
	
);

-- Mandat
CREATE TABLE mandat (
	  mandat_id INT NOT NULL  PRIMARY KEY,	 
	  document_id INT,
      	  FOREIGN KEY(document_id) REFERENCES document(document_id) ON UPDATE CASCADE
);

-- Gestion des clients
CREATE TABLE client (
  	  client_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	
	  entreprise_id INT ,
	  FOREIGN KEY(entreprise_id) REFERENCES entreprise(entreprise_id) ON UPDATE CASCADE ,
	  code_postal INT ,
	  num_RC INT NOT NULL, 
	  wilaya VARCHAR(20) , 
	  statut_juridique VARCHAR(20) ,
	  mandat_id INT NOT NULL,
	  FOREIGN KEY(mandat_id) REFERENCES mandat(mandat_id) ON UPDATE CASCADE ,
	  num_succursale VARCHAR(20) ,
	  num_NIF VARCHAR(20) ,
	  num_NIS VARCHAR(20) , 
	  num_art_imposition VARCHAR(20) 
);


-- RC(registre de commerce)
CREATE TABLE RC (
	  rc_id INT NOT NULL  PRIMARY KEY,	 
	  document_id  INT NOT NULL, 
      	  FOREIGN KEY(document_id) REFERENCES document(document_id) ON UPDATE CASCADE
);

-- Fournisseur
CREATE TABLE fournisseur (
	  fournisseur_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,	 
	  entreprise_id INT ,
	  FOREIGN KEY(entreprise_id) REFERENCES entreprise(entreprise_id) ON UPDATE CASCADE
);

CREATE TABLE contact (
	  contact_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  type VARCHAR(20) ,
	  entreprise_id INT ,
	  FOREIGN KEY(entreprise_id) REFERENCES entreprise(entreprise_id) ON UPDATE CASCADE
);

-- Pays
CREATE TABLE pays (
	  pays_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	 
	  code_pays INT , 
	  libelle VARCHAR(20) 
);

-- Monnaie
CREATE TABLE monnaie (
	  monnaie_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	 
	  code_monnaie VARCHAR(20) ,
	  libelle_monnaie VARCHAR(20) ,
	  taux_change FLOAT 
);

-- MutliObjet
CREATE TABLE multi_objet(
	  multi_objet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  description VARCHAR(140) -- added more chars to descripiton
);

-- Camion
CREATE TABLE camion (
	  camion_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
      matricule char(13) NOT NULL,
	  multi_objet_id INT,
	  FOREIGN KEY(multi_objet_id) REFERENCES multi_objet(multi_objet_id) ON UPDATE CASCADE ,
	  disponibilite CHAR(1) 
);

-- Navire
CREATE TABLE navire (
	  navire_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  multi_objet_id INT,
	  FOREIGN KEY(multi_objet_id) REFERENCES multi_objet(multi_objet_id) ON UPDATE CASCADE ,
	  nom VARCHAR(20) 
);

-- Marchandise
CREATE TABLE marchandise (
	  marchandise_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  designation varchar(40),
	  nature_marchandise VARCHAR(20) -- fixed a spelling mistake
);

-- Bureau_douanier
CREATE TABLE bureau_douanier (
	  bureau_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  code_bureau INT ,
	  bureau_douane VARCHAR(20) 
);

-- Bon de commande
CREATE TABLE bon_commande (
	  bon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	  date DATE , 
	  document INT,
	  FOREIGN KEY(document) REFERENCES document(document_id) ON UPDATE CASCADE ,
	  quantite INT ,
	  observation VARCHAR(20) ,
	  fournisseur_id INT,
	  FOREIGN KEY(fournisseur_id) REFERENCES fournisseur(fournisseur_id) ON UPDATE CASCADE 
);

-- Facture
CREATE TABLE facture (
	  facture_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	  num_facture INT , 
	  date DATE ,
	  num_dossier INT NOT NULL , 
	  client VARCHAR(20) NOT NULL ,
	  montant FLOAT	
);


CREATE TABLE prestation_debours (
	  debours_prestation_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
 	  debours_prestation VARCHAR(20) ,
	  type VARCHAR(1) 
);

-- Gestion de dossier
CREATE TABLE dossier (
	  dossier_id INT NOT NULL PRIMARY KEY, 
	  client_id INT NOT NULL, 
	  ref_client_dossier VARCHAR(20) ,   
	  sit_dossier VARCHAR(20) , 
	  date_reception DATE , 
	  lieu_reception VARCHAR(20) , 
	  num_facture INT NOT NULL ,  
	  monnaie INT NOT NULL , 
	  nature_dossier VARCHAR(20) , 
	  mode_transport VARCHAR(20) , 
	  compagnie_transport VARCHAR(20) , 
	  num_titre_transport VARCHAR(20) , 
	  navire INT NOT NULL , 
	  date_arrivee DATE , 
	  date_main_levee DATE , 
	  lieu_entreposage VARCHAR(20) ,
	  bureau_douane VARCHAR(20) , 
	  receveur_douane VARCHAR(20) ,
	  num_gros VARCHAR(20) ,  
	  num_article VARCHAR(20) , 
	  S_G VARCHAR(20) , 
	  date_echange DATE , 
	  date_declaration DATE , 
	  num_declaration VARCHAR(20) , 
	  valeur_DA INT , 
	  montant_droits_taxes INT NOT NULL , 
	  date_visite_douane DATE , 
	  date_liquidation DATE , 
	  date_recevabilite_cheque DATE , 
	  date_aquittement_droits_taxes DATE , 
	  num_quittance_douane VARCHAR(20) , 
	  date_bon_enlever DATE , 
	  num_bon_enlever VARCHAR(20) , 
	  date_livraison DATE , 
	  lieu_livraison VARCHAR(20) , 
	  parc_vide VARCHAR(20) , 
	  observation_dynamique VARCHAR(100) , 
	  declarant INT NOT NULL , 
	  observation_statique VARCHAR(150) , 
      id_pays_fournisseur INT NOT NULL ,
      id_fournisseur INT NOT NULL ,
      lieu_transfert VARCHAR(50) ,
      pieces_jointes VARCHAR(50) 
);
-- tableau des marchandises 
CREATE TABLE table_marchandises(
       id INT NOT NULL auto_increment primary KEY ,
       id_dossier INT NOT NULL ,
       marchandise VARCHAR(50) NOT NULL ,
       type_marchandise VARCHAR(40) NOT NULL ,
       nbr_colis INT NOT NULL ,
       poids_brut INT NOT NULL ,
       poids_net INT NOT NULL 
);

-- Pesronne
CREATE TABLE personne (
	 id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	 nom  VARCHAR(20) ,
	 prenom VARCHAR(20) ,
	 tel VARCHAR(20) ,
	 email VARCHAR(20) ,
	 adresse VARCHAR(20) 
);
-- Utilisateur
CREATE TABLE utilisateur (
	  utilisateur_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  personne_id INT,
	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE,
	  identifiant VARCHAR(20),
	  mot_de_passe VARCHAR(20) 
);

-- Declarant
CREATE TABLE declarant (
	  declarant_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  personne_id INT,
	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE,
	  photo BLOB,
	  badge_douane DATE ,
	  nbr_J_V_1 FLOAT ,
	  badge_police DATE ,
	  nbr_J_V_2 FLOAT 
);

-- Chauffeur
CREATE TABLE chauffeur (
	  chauffeur_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  personne_id INT,
	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE
);

-- Douanier
CREATE TABLE douanier (
	  douanier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  personne_id INT,
	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE
);

-- Expert
CREATE TABLE expert (
	  expert_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  personne_id INT,
	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE
);

-- Representant
CREATE TABLE representant (
	  representant_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    	  personne_id INT,
 	  FOREIGN KEY(personne_id) REFERENCES personne(id) ON UPDATE CASCADE,
	  entreprise_id INT,
	  FOREIGN KEY(entreprise_id) REFERENCES entreprise(entreprise_id) ON UPDATE CASCADE
);

-- Bon de sorite
CREATE TABLE bon (
	  bon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  declarant VARCHAR(20) ,
	  num_dossier INT ,
	  date DATE , 
	  agent VARCHAR(20) ,
	  transit VARCHAR(20) 
);

CREATE TABLE bon_sortie (
	  sortie_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  bon_id INT ,
	  FOREIGN KEY(bon_id) REFERENCES bon(bon_id) ON UPDATE CASCADE
);
-- Bon de visite
CREATE TABLE bon_visite (
	  visite_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  bon_id INT ,
	  FOREIGN KEY(bon_id) REFERENCES bon(bon_id) ON UPDATE CASCADE
);
 
-- Conteneur
CREATE TABLE emballage (
	  emballage_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	  client_id INT,
      FOREIGN KEY(client_id) REFERENCES client(client_id) ON UPDATE CASCADE,
	  dossier_id INT,
      FOREIGN KEY(dossier_id) REFERENCES dossier(dossier_id) ON UPDATE CASCADE,
	  num INT,
	  num_emballage VARCHAR(20) , 
	  genre_emballage VARCHAR(20) ,
      pieds VARCHAR(20),
	  type_emballage VARCHAR(20),
	  date_livraison DATE ,
	  date_restitution DATE ,
	  num_bon_facture_restitution VARCHAR(20),
	  multi_objet_id INT,
	  FOREIGN KEY(multi_objet_id) REFERENCES multi_objet(multi_objet_id) ON UPDATE CASCADE
);
INSERT INTO personne(nom, prenom) VALUES('admin', 'admin');
INSERT INTO utilisateur VALUES('1', '1', 'admin', 'admin');