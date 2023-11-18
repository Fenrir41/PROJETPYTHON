class Etudiant:
	def __init__(self,id, nom, prenom, email, login ,password,suspended=False):
		self.id = id
		self.nom = nom
		self.prenom = prenom
		self.email = email
		self.login = login
		self.password = password
		self.suspended = suspended
		self.livres_empruntes = []
	def __str__(self):
		return f"{self.id},{self.nom},{self.prenom},{self.email},{self.login},{self.password},{self.suspended} \n"


def emprunter_livre(self, livre):
        if len(self.livres_empruntes) < 3:
            	self.livres_empruntes.append(livre)
            	return True
        else:
            	return False
    
def rendre_livre(self, livre):
	if livre in self.livres_empruntes:
		self.livres_empruntes.remove(livre)
            	return True
        else:
           	return False


