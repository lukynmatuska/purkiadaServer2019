# -*- coding: utf-8 -*-
import threading
import time
import logging

try:
    import dominate
    from dominate.tags import *
except Exception as e:
    logging.info("Error: \"{}\"\n".format(e))

menuList = []

class HtmlPage():
    """Class for making an ground of MUI HTML pages"""

    def __init__(self, title, content, filename):
        self.lastAdd = ""
        self.title = "{} - PurkiadaServer".format(title)
        self.titleMin = str(title)
        self.menuButtonName = title

        global menuList
        #logging.info("menuList: {}".format(menuList))
        #logging.info("self.titleMin: {}".format(self.titleMin))
        if self not in menuList:
            menuList.append(self)

        self.menuList = menuList #['Home', 'About', 'Contact', "Login", "Register", "Status"]
        """if not self.menuButtonName in self.menuList:
            self.menuList.append(self.menuButtonName)"""
        if type(content) == list:
            self.content = content
        else:
            self.content = []
            for c in content:
                self.content.append(c)
        
        self.htmlFileName = filename

        self.update()#title, content, filename)
        self.save()

    def __str__(self):
        return self.titleMin
        
    def update(self):#, title, content, filename):
        global menuList
        if self not in menuList:
            menuList.append(self)
        self.page = dominate.document(title = self.title) #Object for HTML page

        with self.page.head: #Head editing
            link(rel='stylesheet', href="http://cdn.muicss.com/mui-0.9.30/css/mui.min.css")#style.css')
            script(type='text/javascript', src="http://cdn.muicss.com/mui-0.9.30/js/mui.min.js")#script.js")
            script(type='text/javascript', src="timer.js")#script.js")
            #meta(http-equiv="refresh", content="9")
            # <meta http-equiv="refresh" content="7;url=http://carodky.buchticka.eu/">

        with self.page.body: #Body editing
            with div(cls="mui-container"):
                with div(cls="mui-panel"):
                    with div(style="text-align:center"):
                        h1(self.title)
                        #logging.info("self.menuList: {}".format(self.menuList))
                        for name in self.menuList:  # MENU generating
                            #logging.info("NAME: {}".format(name))
                            if name == "home" or name == "Home":
                                with a(href='./index.html'):
                                    button(name.titleMin, style="margin-left:auto;margin-right:auto;margin-top:auto;margin-bottom:auto;",cls="mui-btn mui-btn--primary mui-btn--raised")
                                    #p(name, style="margin-left:auto;margin-right:auto;margin-top:auto;margin-bottom:auto;",cls="mui-btn mui-btn--primary mui-btn--raised")
                            else:
                                with a(href='./%s.html' % name):#   with a(href='./{}.html'.format(name)):
                                    button(name.titleMin, style="margin-left:auto;margin-right:auto;margin-top:auto;margin-bottom:auto;",cls="mui-btn mui-btn--primary mui-btn--raised")
                                    #p(name, style="margin-left:auto;margin-right:auto;margin-top:auto;margin-bottom:auto;",cls="mui-btn mui-btn--primary mui-btn--raised")
                                    
                    hr()
                    if type(self.content) == str and self.content != "":
                        p(self.content)
                        div(self.content)
                    elif type(self.content) == list:
                        for c in self.content:
                            if not type(c) == type(div()):
                                p(c)
                            else:
                                div(c)
                    else:
                        str(self.content)
                        
                    with div(cls="paticka", style="text-alig: center;"):
                        hr()
                        with p("Copyright &copy; 2018, ", style="text-align: center; font-size: 75%; border=0%; padding=0%"):
                            a("Buchticka.eu Team", href="https://buchticka.eu")
                            #pass #a("posta@buchticka.eu", href="mailto:posta@buchticka.eu", cls="blind")
            #print(self.page)
            return self.page

    def save(self):
        #self.htmlFileName = "index" #"mealList"
        self.i = 1
        while True:
            try:
                if self.i == 1:
                    self.f1 = open(".\\panel\{}.html".format(self.htmlFileName), "w")
                    #self.i = ""
                else:
                    self.f1 = open(".\\panel\{}{}.html".format(self.htmlFileName,self.i), "w")
                self.f1.write(str(self.update()))#doc))
                #f1.write(str(week.offerHtml))#doc))
                self.f1.close()
                #print("\nFILE NAME: {}{}.html".format(self.htmlFileName, self.i))
                break
            except Exception as e:
                logging.info("Error: \"{}\"".format(e))
                self.i += 1

        #self.htmlFileName = "index"
        while True:
            try:
                self.f2 = open("C:\\xampp\\htdocs\\purkiadaServer2019\\{}.html".format(self.htmlFileName), "w")
                self.f2.write(str(self.update()))
                self.f2.close()
                #print("FILE NAME: C:\\xampp\\htdocs\\purkiadaServer2018\\{}.html".format(self.htmlFileName))
                break
            except Exception as e:
                logging.info("Error: \"{}\"".format(e))
                #print("Error with saving html file! to C:\\xampp\\htdocs\\purkiadaServer2018\\")

    def add(self, a, text="Undefined"):
        #self.content += "{}".format(a)
        self.casteTexty = ["Active users:", "Nikdo se jeste nepripojil!"]
        self.poprve = True
        try:
            if self.lastAdd == a:
                self.save()
            elif a not in self.content and text not in self.casteTexty:
                self.content.append(a)
                #logging.info("Added: {}".format(a))
                
                #logging.info("Type: {}".format(type(self.content[self.content.index(a)-1])))
                #logging.info("Type: {}".format(type(self.content[self.content.index(a)])))
                i = 1
                while not type(self.content[self.content.index(a)-i]) == type(self.content[self.content.index(a)]):
                    #logging.info("Type: {}".format(type(self.content[self.content.index(a)-i])))
                    i+=1
                    
                if text != "user" and type(self.content[self.content.index(a)-i]) == type(self.content[self.content.index(a)]) and self.content[self.content.index(a)-i] != self.content[self.content.index(a)]:
                    #logging.info("Deleting: {}".format(self.content[self.content.index(a)-i]))
                    del self.content[self.content.index(a)-i]
                #logging.info(str(self.content))
                #self.update()
                self.save()

            elif self.poprve:
                self.content.append(a)
                #logging.info("Added: {}".format(a))
                #self.update()
                self.save()
                self.poprve = False

        except Exception as e:
            logging.info(e)
            
        
home = HtmlPage("index", "Ahoj svete! z Homu", "Index")
status = HtmlPage("Status", ["Purkiada Server Panel was started!"], "Status")
contact = HtmlPage("Contact", "Ahoj svete! z contact", "Contact")
about = HtmlPage("About", "Ahoj svete! z about", "About")
login = HtmlPage("Login", "Ahoj svete! z login", "Login")
register = HtmlPage("Register", "Ahoj svete! z Register", "Register")
#print(".: Websites creation SUCCES COMPLETED! :.")

for page in [home, status, contact, about, login, register]:
    page.save()

logging.basicConfig(level=logging.DEBUG,
                    format='[%(threadName)-10s] %(message)s',
                    )
def saveIt():
    while True:
        time.sleep(60)
        #home.save()
        status.save()
        logging.info("HTML saved at {}".format(time.asctime( time.localtime(time.time()) )))

def UpdateHtml():
    logging.info('Running...')
    while True:
        #saveIt()#home.update()
        time.sleep(30)
        status.update()
        logging.info("HTML updated at {}".format(time.asctime( time.localtime(time.time()) )))
        #print("updated at {}".format(time.time()))
        status.save()
        logging.info("HTML saved   at {}".format(time.asctime( time.localtime(time.time()) )))
        #print("Saved at {}".format(time.time()))       

#time.sleep(2)
def deamonStop():
    logging.info('Exiting')

d = threading.Thread(name="Server panel", target=UpdateHtml)#UpdateHtml
d.setDaemon(True)

def non_daemon():
    logging.info('Starting')
    logging.info('Exiting')

#t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
#t.start()

d.join(1)
#print 'd(isAlive()', d.isAlive())
#t.join()    
#print("Stoppped")
