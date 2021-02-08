import cherrypy

"""
    def index(self):
        page = self.creationPage("index")
        return page
    index.exposed = True
"""

class MonCV(object):
    @cherrypy.expose

    def rendu(self, page):
        """ Va chercher le contenu du fichier {}.html
            Renvoi le contenu de la page au format texte
        """

        page = 'pagesHTML/{}'.format(page)
        with open(page,'r') as html:
            page = html.readlines()
        result = str()
        for ligne in page:
            result += ligne
        return result

    def creationPage(self, url):
        """ Génére l'arborescence de toutes les pages
            Renvoi la page completer (Haut + Menu + contenu etc.)
        """
        page = self.rendu("haut.html")
        page += self.rendu("menu.html")
        page += self.rendu("{}.html".format(url))
        page += self.rendu("bas.html")
        return page

    def index(self):
        page = self.creationPage("index")
        return page
    index.exposed = True

    def artistique(self):
        page = self.creationPage("artistique")
        return page
    artistique.exposed = True

    def experience(self):
        page = self.creationPage("experience")
        return page
    experience.exposed = True

    def formation(self):
        page = self.creationPage("formation")
        return page
    formation.exposed = True       

    def projets(self):
        page = self.creationPage("projets")
        return page
    projets.exposed = True

    def apropos(self):
        page = self.creationPage("apropos")
        return page
    apropos.exposed = True
    
    def social(self):
        page = self.creationPage("social")
        return page
    social.exposed = True

cherrypy.quickstart(MonCV(), config="monCV.conf")