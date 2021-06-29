DROP DATABASE projet1;
CREATE DATABASE projet1;
USE projet1;

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
	  libelle VARCHAR(45) 
);

-- Monnaie
CREATE TABLE monnaie (
	  monnaie_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,	 
	  code_monnaie VARCHAR(45) ,
	  libelle_monnaie VARCHAR(45) ,
	  taux_change FLOAT 
);

-- MutliObjet
CREATE TABLE multi_objet(
	  multi_objet_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  description VARCHAR(140) -- added more chars to descripiton
);

-- Conteneur
CREATE TABLE emballage (	
	  multi_objet_id INT,
	  FOREIGN KEY(multi_objet_id) REFERENCES multi_objet(multi_objet_id) ON UPDATE CASCADE ,
	  client VARCHAR(20) ,
	  num_dossier VARCHAR(20) , 
	  emballage_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	  num_emballage VARCHAR(20) , 
	  genre VARCHAR(20) ,
	  type_emballage VARCHAR(20),
	  date_livraison DATE ,
	  date_restitution DATE ,
	  num_bon_facture_restitution VARCHAR(20) 
);

-- Camion
CREATE TABLE camion (
	  camion_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
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
	  multi_objet_id INT,
	  FOREIGN KEY(multi_objet_id) REFERENCES multi_objet(multi_objet_id) ON UPDATE CASCADE ,
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
	  num_dossier VARCHAR(20) , 
	  client VARCHAR(20) ,
	  num_declaration VARCHAR(20) ,
	  fournisseur VARCHAR(20) , 
	  montant FLOAT ,
	  monnaie VARCHAR(20) ,
	  num_titre_transport VARCHAR(20) ,
	  nature_marchandise VARCHAR(20) 
);


CREATE TABLE prestation_debours (
	  debours_prestation_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
 	  debours_prestation VARCHAR(20) ,
	  type VARCHAR(20) 
);

CREATE TABLE debours_prestation (
	  debours_prestation_id INT ,
          FOREIGN KEY(debours_prestation_id) REFERENCES prestation_debours(debours_prestation_id) ON UPDATE CASCADE ,
	  facture_id INT,
	  FOREIGN KEY(facture_id) REFERENCES facture(facture_id) ON UPDATE CASCADE ,
	  montant FLOAT 	
);

-- Gestion de dossier
CREATE TABLE informations_generales (
	  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  num_dossier VARCHAR(20) , 
	  client VARCHAR(20) ,
	  ref_client_dossier VARCHAR(20) ,  
	  sit_dossier VARCHAR(20) ,
	  date_reception DATE ,
	  lieu_reception VARCHAR(20) ,
	  fournisseur VARCHAR(20) ,
	  num_facture VARCHAR(20) , 
	  montant FLOAT ,
	  monnaie VARCHAR(5) ,
	  nature_marchandise VARCHAR(20) ,
	  nature_dossier VARCHAR(20) ,
	  mode_transport VARCHAR(20) ,
	  compagnie_transport VARCHAR(20) ,
	  num_titre_transport VARCHAR(20) ,
	  nbr_TC VARCHAR(20) , 
	  navire VARCHAR(20) ,
	  date_arrivee DATE ,
	  date_main_levee DATE ,
	  nbr_colis INT ,
	  poids_brut INT ,
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
	  montant_droits_taxes INT , 
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
	  observation_dynamique VARCHAR(50) ,
	  declarant VARCHAR(20) ,
	  observation_statique VARCHAR(50) 
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



CREATE TABLE grille_saisie (
	  grille_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	  regime VARCHAR(20) ,
	  douanier VARCHAR(20) , 
	  bureau_douane VARCHAR(20) ,	 
	  nbr_articles INT ,
	  num_rep INT ,
	  mode_paiement VARCHAR(20) ,
	  fournisseur_client VARCHAR(20) ,
	  adresse_fournisseur VARCHAR(20) ,
	  pays_fournisseur VARCHAR(20) , 
	  mode_livraison VARCHAR(20) ,
	  mode_financement VARCHAR(20) ,
	  type_operation VARCHAR(20) ,
	  nature_transaction VARCHAR(20) ,
	  relation_acheteur_vendeur VARCHAR(20) ,
	  pays_provenance VARCHAR(20) , 
	  transport_interieur VARCHAR(20) ,
	  nature_declaration VARCHAR(20) ,
	  type_manifeste VARCHAR(20) ,
	  annee_gros INT ,
	  num_gros INT ,
	  num_art VARCHAR(20) ,
	  S_G VARCHAR(1) ,
	  type_dedouanement VARCHAR(20) ,
	  nbr_colis INT ,
	  poids_net FLOAT ,
	  poids_brut FLOAT ,
	  wilaya VARCHAR(20) ,
	  agence VARCHAR(20) ,
	  num_domiciliation_bancaire VARCHAR(20) ,
	  date_domiciliation  DATE ,
	  type_domiciliation  VARCHAR(20) ,
	  bureau VARCHAR(20) ,
	  annee INT ,
	  num_declaration VARCHAR(20) ,
	  regime_precedent VARCHAR(20) ,
	  B_depart VARCHAR(20) ,
	  B_arrivee VARCHAR(20) ,
	  num VARCHAR(20) ,
	  duree INT , 
	  taux FLOAT ,
	  montant_caution FLOAT ,
	  lieu VARCHAR(20) 
);

-- Dossier
CREATE TABLE dossier (
	  dossier_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  informations_generales_id INT,
	  FOREIGN KEY(informations_generales_id) REFERENCES informations_generales(id) ON UPDATE CASCADE , 
	  grille_id INT,
	  FOREIGN KEY(grille_id) REFERENCES grille_saisie(grille_id) ON UPDATE CASCADE
);
-- Bon de sorite
CREATE TABLE bon (
	  bon_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	  declarant VARCHAR(50) ,
	  num_dossier INT ,
	  date DATE , 
	  agent VARCHAR(50) ,
	  transit VARCHAR(50) 
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
 

