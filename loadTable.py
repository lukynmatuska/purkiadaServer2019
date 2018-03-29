# -*- coding: utf-8 -*-
import xlrd
import logging
#import threading

logging.basicConfig(level=logging.DEBUG,
                    format='[%(threadName)-10s] %(message)s',
                    )

class TableToTxt():
	"""Class for converting xlsx table to txt file."""

	def __init__(self, tableLocation="table.xlsx", txtLocation="usersFromTable.txt"):
		self.tableLoc = tableLocation
		self.txtLoc = txtLocation
		self.reload()
		


	def reload(self):
		self.workbook = xlrd.open_workbook(self.tableLoc)
		self.sheet = self.workbook.sheet_by_index(0)
		self.data = [[self.sheet.cell_value(r,c) for c in range(self.sheet.ncols)] for r in range(self.sheet.nrows)]
		self.users = []
		for i in range(1, len(self.data)):
			if self.data[i][4] != "":
				self.users.append(self.data[i][4]) #1
		self.pswds = []
		for i in range(1, len(self.data)):
			if self.data[i][3] != "":
				self.pswds.append(self.data[i][3]) #2
		logging.info("Successfully loaded {} users.".format(len(self.users)))
		self.save()

	def save(self):
		self.txtFile = open(self.txtLoc, "w")
		povedeno = True
		for user in self.users:
			if user != "":
				try:
					self.txtFile.write("{}-{}\n".format(user, self.pswds[self.users.index(user)]))
				except:
					logging.info("Error with saving user \"{}\"".format(self.users))
					povedeno = False
		self.txtFile.close()
		if povedeno:
			logging.info("Successfully saved {} users.".format(len(self.users)))


"""
#fileLocation = "c:\\temp\\table.xlsx"
fileLocation = "table.xlsx"
workbook = xlrd.open_workbook(fileLocation)
sheet = workbook.sheet_by_index(0)
#sheet.cell_value(0,0)
#print(sheet.nrows)
#print(sheet.ncols)
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

users = []
for i in range(1, len(data)):
    users.append(data[i][4])#1
#print("Users: {}\n".format(users))

pswds = []
for i in range(1, len(data)):
    pswds.append(data[i][3])#2
#print("Pswds: {}".format(pswds))import xlrd

file = open("usersFromTable.txt", "w")
for user in users:
    if user != "":
        try:
            file.write("{}-{}\n".format(user, pswds[users.index(user)]))
        except:
            print("Error with saving user \"{}\"".format(user))
file.close()"""

"""

file1 = TableToTxt()

def start():
	global file1
	file1.reload()

d = threading.Thread(name="Data from table", target=start)#UpdateHtml
d.setDaemon(True)
d.start()
d.join(1)"""