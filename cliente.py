from urllib.request import urlopen
import bs4

class ClienteWeb(object):
        def __init__(self):
                super(ClienteWeb, self).__init__()
                pass

        def buscar_Activitats(self, html):
                arbre = bs4.BeautifulSoup(html)
                activitats = arbre.find_all("div","featured-links-item")
                return activitats

        def descarregar_html(self):
                f = urlopen("http://www.eps.udl.cat/ca/")
                html = f.read()
                f.close()
                return html

        def run(self):
            html = self.descarregar_html()
            print(html)
            pass

if __name__ == "__main__":
    c = ClienteWeb()
    c.run()
