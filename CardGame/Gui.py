from PySide import QtGui,QtCore
import sys
import getpass
if not "C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame"in sys.path:
    sys.path.append("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame")
import random

import CardGame.cardFunc as CFC
reload (CFC)
a = CFC.Hero()
b = CFC.Monster()
xx = CFC.Playgame(a,b)
class CGui(QtGui.QDialog):
	def __init__(self):
		super(CGui,self).__init__()
		self.setGeometry(300,50,400,400)
		self.widget()
		self.layout()
		self.connect()
		self.timer()
		self.heroC= 300
		self.monsC= 300
	def widget(self):
		self.btn1 = QtGui.QPushButton(' BATTLE ')
		self.btn1.setFixedSize(150,30)
		self.btn1.setStyleSheet("""QPushButton{background:rgb(255,255,255); border-radius:15px};""")
		self.la1 = QtGui.QLabel('CARD GAME |')
		self.la1.setStyleSheet("QLabel{color:rgb(255,255,255)};")
		self.laRe = QtGui.QPushButton('RESTART')
		self.laRe.setFixedSize(60,20)
		self.laRe.setStyleSheet("""QPushButton{background:rgb(120,120,120); border-radius:10px};""")
		self.hide = QtGui.QLabel(' _ ')
		self.Qu = QtGui.QLabel(' X ')
		self.Qu.setStyleSheet("""QLabel{background:rgb(200,85,85)};""")
		
		self.heroLog = QtGui.QLabel('HP 300/300| READY')
		self.heroLog.setAlignment(QtCore.Qt.AlignCenter)
		self.heroLog.setFixedSize(150,20)
		self.heroLog.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:10px};""")
		self.monsLog = QtGui.QLabel('HP 300/300| READY')
		self.monsLog.setAlignment(QtCore.Qt.AlignCenter)
		self.monsLog.setFixedSize(150,20)
		self.monsLog.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:10px};""")
		self.heroHp = QtGui.QProgressBar()
		self.heroHp.setTextVisible(1)
		#self.heroHp.setRange(0,300)
		self.heroHp.setMaximum(300)
		self.heroHp.setValue(xx.Hero.hp)
		self.MonsHp = QtGui.QProgressBar()
		self.MonsHp.setTextVisible(1)
		self.MonsHp.setInvertedAppearance(True)
		#self.MonsHp.setRange(0,300)
		self.MonsHp.setMaximum(300)
		self.MonsHp.setValue(xx.Monster.hp)
		self.turn = QtGui.QLabel('00')
		self.turn.setAlignment(QtCore.Qt.AlignCenter)
		self.turn.setFixedSize(40,40)
		self.turn.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:20px};""")
		self.heroPic = QtGui.QLabel()
		self.MonsPic = QtGui.QLabel()
		self.back = QtGui.QLabel()
		self.back2 = QtGui.QLabel()
		self.vs = QtGui.QLabel("  VS  ")
		self.vs.setAlignment(QtCore.Qt.AlignCenter)
		self.vs.setFixedSize(40,40)
		self.vs.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:15px};""")
		self.nHero=QtGui.QLabel(' HERO ')
		self.nHero.setAlignment(QtCore.Qt.AlignCenter)
		self.nHero.setFixedSize(150,30)
		self.nHero.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:10px};""")
		self.nMons=QtGui.QLabel(' MONSTER ')
		self.nMons.setFixedSize(150,30)
		self.nMons.setAlignment(QtCore.Qt.AlignCenter)
		self.nMons.setStyleSheet("""QLabel{background:rgb(255,255,255); border-radius:10px};""")
		self.heroImg = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/charHero.png")
		self.MonsImg = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/charBoss.png")
		self.backImg = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/backCard.png")
		self.blankImg = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/blank.png")
		self.heroATK = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/aHero.png")
		self.heroDEF = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/dHero.png")
		self.heroBRK = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/bHero.png")
		self.monsATK = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/aBoss.png")
		self.monsDEF = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/dBoss.png")
		self.monsBRK = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/bBoss.png")
		self.allHEAL = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/heal.png")
		self.arrow = QtGui.QPixmap("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame/icon_card/AR.png")
		self.arPic = QtGui.QLabel()
		self.arPic.setFixedSize(20,20)
		self.listPic =[self.heroATK,self.heroDEF,self.heroBRK,self.allHEAL]
		#getVALUE--------------->
		self.pick =0
		self.MonsPick = 0
		self.turnC = 0
		self.S1C =5
		self.S2C =5
		self.S3C =5
		self.BC = 5
		self.Hlog =''
		self.Mlog=''
		self.W =1000
		self.H = 800
		#setpic--------->
		self.heroPic.setPixmap(self.heroImg)
		self.MonsPic.setPixmap(self.MonsImg)
		self.back.setPixmap(self.backImg)
		self.back2.setPixmap(self.backImg)
		self.slot1=QtGui.QLabel('1')
		self.slot1.setAlignment(QtCore.Qt.AlignCenter)
		self.slot1.setPixmap(self.blankImg)
		self.slot2=QtGui.QLabel('2')
		self.slot2.setAlignment(QtCore.Qt.AlignCenter)
		self.slot2.setPixmap(self.blankImg)
		self.slot3=QtGui.QLabel('3')
		self.slot3.setAlignment(QtCore.Qt.AlignCenter)
		self.slot3.setPixmap(self.blankImg)
		self.mainCard = QtGui.QLabel('$$$')
		self.mainCard.setAlignment(QtCore.Qt.AlignCenter)
		self.mainCard.setPixmap(self.backImg)
		self.arPic.setPixmap(self.arrow)
		#shadow------------------->
		shadow0= QtGui.QGraphicsDropShadowEffect(self)
		shadow0.setBlurRadius(20)
		shadow0.setOffset(5)
		shadow0.setColor(QtGui.QColor(0,0,0))
		self.slot1.setGraphicsEffect(shadow0)

		shadow1= QtGui.QGraphicsDropShadowEffect(self)
		shadow1.setBlurRadius(20)
		shadow1.setOffset(5)
		shadow1.setColor(QtGui.QColor(0,0,0))
		self.slot2.setGraphicsEffect(shadow1)

		shadow2= QtGui.QGraphicsDropShadowEffect(self)
		shadow2.setBlurRadius(20)
		shadow2.setOffset(5)
		shadow2.setColor(QtGui.QColor(0,0,0))
		self.slot3.setGraphicsEffect(shadow2)

		shadow3= QtGui.QGraphicsDropShadowEffect(self)
		shadow3.setBlurRadius(20)
		shadow3.setOffset(5)
		shadow3.setColor(QtGui.QColor(0,0,0))
		self.mainCard.setGraphicsEffect(shadow3)

		shadow4= QtGui.QGraphicsDropShadowEffect(self)
		shadow4.setBlurRadius(20)
		shadow4.setOffset(5)
		shadow4.setColor(QtGui.QColor(0,0,0))
		self.heroPic.setGraphicsEffect(shadow4)

		shadow5= QtGui.QGraphicsDropShadowEffect(self)
		shadow5.setBlurRadius(20)
		shadow5.setOffset(5)
		shadow5.setColor(QtGui.QColor(0,0,0))
		self.back.setGraphicsEffect(shadow5)

		shadow6= QtGui.QGraphicsDropShadowEffect(self)
		shadow6.setBlurRadius(20)
		shadow6.setOffset(5)
		shadow6.setColor(QtGui.QColor(0,0,0))
		self.back2.setGraphicsEffect(shadow6)

		shadow7= QtGui.QGraphicsDropShadowEffect(self)
		shadow7.setBlurRadius(20)
		shadow7.setOffset(5)
		shadow7.setColor(QtGui.QColor(0,0,0))
		self.MonsPic.setGraphicsEffect(shadow7)
		#shadow------------------->

	def layout(self):
		main = QtGui.QVBoxLayout()
		lay1= QtGui.QHBoxLayout()
		lay2= QtGui.QHBoxLayout()
		lay3= QtGui.QHBoxLayout()
		lay4 = QtGui.QHBoxLayout()
		lay5 = QtGui.QHBoxLayout()
		lay6 = QtGui.QHBoxLayout()
		lay7 = QtGui.QHBoxLayout()
		lay8 = QtGui.QHBoxLayout()
		lay9 = QtGui.QHBoxLayout()
		lay10 = QtGui.QHBoxLayout()
		heroLay= QtGui.QHBoxLayout()
		monsLay= QtGui.QHBoxLayout()
		layVS = QtGui.QHBoxLayout()
		sizelay = QtGui.QHBoxLayout()

		main.setAlignment(QtCore.Qt.AlignTop|QtCore.Qt.AlignCenter)
		lay2.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		lay3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
		lay4.setAlignment(QtCore.Qt.AlignTop)
		lay6.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
		lay7.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignTop)
		layVS.setAlignment(QtCore.Qt.AlignCenter)
		heroLay.setAlignment(QtCore.Qt.AlignLeft)
		monsLay.setAlignment(QtCore.Qt.AlignRight)
		sizelay.setAlignment(QtCore.Qt.AlignRight)

		lay2.addWidget(self.la1)
		lay2.addWidget(self.laRe)
		lay3.addWidget(self.hide)
		lay3.addWidget(self.Qu)
		lay1.addLayout(lay2)
		lay1.addLayout(lay3)
		lay4.addWidget(self.heroHp)
		lay4.addWidget(self.turn)
		lay4.addWidget(self.MonsHp)
		lay5.addLayout(lay6)
		lay5.addLayout(lay7)
		lay8.addLayout(heroLay)
		lay8.addLayout(layVS)
		lay8.addLayout(monsLay)
		lay6.addWidget(self.heroLog)
		lay7.addWidget(self.monsLog)
		layVS.addWidget(self.vs)
		heroLay.addWidget(self.heroPic)
		heroLay.addWidget(self.back)
		monsLay.addWidget(self.back2)
		monsLay.addWidget(self.MonsPic)
		lay9.addWidget(self.nHero)
		lay9.addWidget(self.btn1)
		lay9.addWidget(self.nMons)
		lay10.addWidget(self.slot1)
		lay10.addWidget(self.slot2)
		lay10.addWidget(self.slot3)
		lay10.addWidget(self.mainCard)
		sizelay.addWidget(self.arPic)
		main.addLayout(lay1)
		main.addLayout(lay4)
		main.addLayout(lay5)
		main.addLayout(lay8)
		main.addLayout(lay9)
		main.addLayout(lay10)
		main.addLayout(sizelay)
		dialog = QtGui.QDialog()
		dialog.setStyleSheet("QDialog{background:rgba(255,255,255,50); border-radius:15px}; ")
		dialog.setLayout(main)
		panel = QtGui.QVBoxLayout()
		panel.addWidget(dialog)
		self.setLayout(panel)
		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		dialog.keyPressEvent = self.quit
		
	def connect(self): 
		self.btn1.clicked.connect(self.start)
		self.hide.mousePressEvent = self.hidden
		self.Qu.mousePressEvent = self.quit
		self.laRe.mousePressEvent = self.Regame
		self.mainCard.mouseMoveEvent = self.dragMoveEvent
		self.slot1.setAcceptDrops(1)
		self.slot2.setAcceptDrops(1)
		self.slot3.setAcceptDrops(1)
		self.back.setAcceptDrops(1)
		self.slot1.dragEnterEvent = self.dragEvent_S1
		self.slot2.dragEnterEvent = self.dragEvent_S2
		self.slot3.dragEnterEvent = self.dragEvent_S3
		self.back.dragEnterEvent = self.dragEvent_back
		self.slot1.dropEvent =self.dropEvent_S1
		self.slot2.dropEvent =self.dropEvent_S2
		self.slot3.dropEvent =self.dropEvent_S3
		self.back.dropEvent = self.dropEvent_Pick
		self.slot1.mouseMoveEvent = self.dragMoveEvent_S1
		self.slot2.mouseMoveEvent = self.dragMoveEvent_S2
		self.slot3.mouseMoveEvent = self.dragMoveEvent_S3
		self.back.mouseMoveEvent = self.dragMoveEvent_pick
		self.arPic.enterEvent = self.mouseEnterEvent
		self.arPic.leaveEvent = self.mouseLeaveEvent
		self.arPic.mouseMoveEvent = self.resize

	def keyPressEvent(self,event):
		key = event.key()
		if key == QtCore.Qt.Key_Escape:
			self.close()
	def quit(self,event):
		self.close()

	def mousePressEvent(self,event):
		self.moving = True
		self.mouseClick = event.pos()

	def mouseMoveEvent(self,event):
		if self.moving:
			self.move(event.globalPos()-self.mouseClick)

	def mouseEnterEvent(self,event):
		self.setCursor(QtCore.Qt.SizeFDiagCursor)
	def mouseLeaveEvent(self,event):
		self.setCursor(QtCore.Qt.ArrowCursor)
	def timer(self):
		self.timer = QtCore.QTimer()
		self.timer.setInterval(30)
		self.timer.timeout.connect(self.setBar)
		self.aaa = 0
		self.bbb =0
		self.HTD=0
		self.MTD=0
		self.healSH =0
		self.healSM =0
		self.hpoint = 0
		self.mpoint = 0

	def start(self):
		if self.BC != 5:
			xx.battle()
			self.pick = xx.Pu
			self.MonsPick = xx.Mu
			self.setMonsCard()
			xx.action()
			self.HTD = xx.HDM
			self.MTD = xx.MDM
			self.healSH = xx.healPH
			self.healSM = xx.healPM
			self.Hheal =0
			self.Mheal =0
			if self.healSH ==1:
				self.Hheal =25
			if self.healSM ==1:
				self.Mheal = 25
			self.turnC = xx.TT
			self.Hlog= self.HTD-self.Hheal
			self.Mlog= self.MTD-self.Mheal
			self.heroLog.setText('HP : -%s'%(self.Hlog))
			self.monsLog.setText('HP : -%s'%(self.Mlog))
			self.timer.start() #will FIX
		else:
			print 'try'
	def setBar(self):
		if self.healSH ==1: #heroHEAL
			self.heroHp.setValue(self.heroC+self.hpoint)
			
			self.hpoint+=1
		if self.hpoint == 26:
			self.healSH = 0
			self.hpoint = 0
			self.heroC = self.heroHp.value()
		if self.healSM ==1: #MonsHEAL
			self.MonsHp.setValue(self.monsC+self.mpoint)
			
			self.mpoint+=1
		if self.mpoint == 26:
			self.healSM = 0
			self.mpoint = 0
			self.monsC = self.MonsHp.value()
		if self.healSH ==0 and self.healSM ==0:
			if self.HTD !=0:#heroDAMAGE
				self.heroHp.setValue(self.heroC-self.aaa)
				#print self.aaa
				#print 'hero: %s'%(self.aaa)
				self.aaa+=1
				if self.aaa == self.HTD+1:
					self.HTD = 0
					self.aaa = 0
					self.heroC = self.heroHp.value()
			if self.MTD != 0:#monsDAMAGE
				self.MonsHp.setValue(self.monsC-self.bbb)
				#print 'mon: %s'%(self.bbb)
				self.bbb+=1
				if self.bbb == self.MTD+1:
					self.MTD = 0
					self.bbb = 0
					self.monsC= self.MonsHp.value() 
		if self.heroC <= 0:
			self.heroHp.setValue(0)
		if self.monsC <= 0:
			self.MonsHp.setValue(0)
		if self.healSH ==0 and self.healSM ==0 and self.HTD ==0 and self.MTD ==0 :
			self.timer.stop()
			self.heroC = self.heroHp.value()
			self.monsC= self.MonsHp.value() 
			print self.heroHp.value()
			print self.MonsHp.value() 
			self.back.setPixmap(self.blankImg)
			self.back2.setPixmap(self.blankImg)
			self.BC = 5
		self.turn.setText('%02d'%(self.turnC)) #will FIX
		
	def setMonsCard(self):
		if self.MonsPick ==0:
			self.back2.setPixmap(self.monsATK)
		elif self.MonsPick ==1:
			self.back2.setPixmap(self.monsDEF)
		elif self.MonsPick ==2:
			self.back2.setPixmap(self.monsBRK)
		elif self.MonsPick ==3:
			self.back2.setPixmap(self.allHEAL)	
	def dragMoveEvent(self,event):
		Data = QtCore.QMimeData()
		Data.setText('main')
		drag = QtGui.QDrag(self)
		drag.setMimeData(Data)
		drag.setHotSpot(event.pos()-self.mainCard.rect().topLeft())
		drag.setPixmap(self.backImg)
		drag.start(QtCore.Qt.MoveAction)
	def dragMoveEvent_S1(self,event):
		Data = QtCore.QMimeData()
		Data.setText('S1')
		drag = QtGui.QDrag(self)
		drag.setMimeData(Data)
		drag.setHotSpot(event.pos()-self.mainCard.rect().topLeft())
		drag.setPixmap(self.listPic[self.S1C])
		drag.start(QtCore.Qt.MoveAction)
	def dragMoveEvent_S2(self,event):
		Data = QtCore.QMimeData()
		Data.setText('S2')
		drag = QtGui.QDrag(self)
		drag.setMimeData(Data)
		drag.setHotSpot(event.pos()-self.mainCard.rect().topLeft())
		drag.setPixmap(self.listPic[self.S2C])
		drag.start(QtCore.Qt.MoveAction)
	def dragMoveEvent_S3(self,event):
		Data = QtCore.QMimeData()
		Data.setText('S3')
		drag = QtGui.QDrag(self)
		drag.setMimeData(Data)
		drag.setHotSpot(event.pos()-self.mainCard.rect().topLeft())
		drag.setPixmap(self.listPic[self.S3C])
		drag.start(QtCore.Qt.MoveAction)
	def dragMoveEvent_pick(self,event):
		Data = QtCore.QMimeData()
		Data.setText('Picking')
		drag = QtGui.QDrag(self)
		drag.setMimeData(Data)
		drag.setHotSpot(event.pos()-self.mainCard.rect().topLeft())
		drag.setPixmap(self.listPic[self.BC])
		drag.start(QtCore.Qt.MoveAction)
	def dragEvent_S1(self,event):
		print 1
		event.accept()
	def dragEvent_S2(self,event):
		print 2
		event.accept()
	def dragEvent_S3(self,event):
		print 3
		event.accept()
	def dragEvent_back(self,event):
		print 'pick'
		event.accept()
	def dropEvent_S1(self,event):
		
		if event.mimeData().text() =='main':
			if self.S1C == 5:
					event.accept()
					ran = random.randint(0,3)
					if ran == 0:
						self.slot1.setPixmap(self.heroATK)
						self.S1C = ran
					elif ran == 1:
						self.slot1.setPixmap(self.heroDEF)
						self.S1C = ran
					elif ran == 2:
						self.slot1.setPixmap(self.heroBRK)
						self.S1C = ran
					elif ran == 3:
						self.slot1.setPixmap(self.allHEAL)
						self.S1C = ran
					print ran
		if event.mimeData().text() =='Picking':
			if self.S1C == 5:
				event.accept()
				self.slot1.setPixmap(self.listPic[self.BC])
				self.S1C = self.BC
				self.BC = 5
				self.back.setPixmap(self.blankImg)
		else:
			event.ignore()
	def dropEvent_S2(self,event):
		if event.mimeData().text() =='main':
			if self.S2C == 5:
				event.accept()
				ran = random.randint(0,3)
				if ran == 0:
					self.slot2.setPixmap(self.heroATK)
					self.S2C = ran
				elif ran == 1:
					self.slot2.setPixmap(self.heroDEF)
					self.S2C = ran
				elif ran == 2:
					self.slot2.setPixmap(self.heroBRK)
					self.S2C = ran
				elif ran == 3:
					self.slot2.setPixmap(self.allHEAL)
					self.S2C = ran
				print ran
		if event.mimeData().text() =='Picking':
			if self.S2C == 5:
				event.accept()
				self.slot2.setPixmap(self.listPic[self.BC])
				self.S2C = self.BC
				self.BC = 5
				self.back.setPixmap(self.blankImg)
		else:
			event.ignore()
	def dropEvent_S3(self,event):
		if event.mimeData().text() =='main':
			if self.S3C == 5:
				event.accept()
				ran = random.randint(0,3)
				if ran == 0:
					self.slot3.setPixmap(self.heroATK)
					self.S3C = ran
				elif ran == 1:
					self.slot3.setPixmap(self.heroDEF)
					self.S3C = ran
				elif ran == 2:
					self.slot3.setPixmap(self.heroBRK)
					self.S3C = ran
				elif ran == 3:
					self.slot3.setPixmap(self.allHEAL)
					self.S3C = ran
				print ran
		if event.mimeData().text() =='Picking':
			if self.S3C == 5:
				event.accept()
				self.slot3.setPixmap(self.listPic[self.BC])
				self.S3C = self.BC
				self.BC = 5
				self.back.setPixmap(self.blankImg)
		else:
			event.ignore()
	def dropEvent_Pick(self,event):
		if self.BC == 5:
			if event.mimeData().text() =='S1':
				event.accept()
				self.back.setPixmap(self.listPic[self.S1C])
				xx.Hero.pick = self.S1C
				self.BC =self.S1C
				self.slot1.setPixmap(self.blankImg)
				self.S1C =5
			elif event.mimeData().text() =='S2':
				event.accept()
				self.back.setPixmap(self.listPic[self.S2C])
				xx.Hero.pick = self.S2C
				self.BC=self.S2C
				self.slot2.setPixmap(self.blankImg)
				self.S2C =5
			elif event.mimeData().text() == 'S3':
				event.accept()
				self.back.setPixmap(self.listPic[self.S3C])
				xx.Hero.pick = self.S3C
				self.BC=self.S3C
				self.slot3.setPixmap(self.blankImg)
				self.S3C =5
		else:
			event.ignore()
	def Regame(self,event):
		self.back.setPixmap(self.backImg)
		self.back2.setPixmap(self.backImg)
		self.heroC= 300
		self.monsC= 300
		self.heroHp.setValue(self.heroC)
		self.MonsHp.setValue(self.monsC)
		xx.TT =0
		self.turnC = xx.TT
		self.turn.setText('%02d'%(self.turnC))
		self.heroLog.setText('HP 300/300| READY')
		self.monsLog.setText('HP 300/300| READY')
		self.BC =5
		self.S1C=5
		self.S2C=5
		self.S3C=5
		self.slot1.setPixmap(self.blankImg)
		self.slot2.setPixmap(self.blankImg)
		self.slot3.setPixmap(self.blankImg)
	def resize(self,event):
		x = event.x()
		y = event.y()
		self.W +=x
		self.H +=y
		self.setFixedSize(QtCore.QSize(self.W,self.H))
	def hidden(self,event):
		self.showMinimized()
try:
	window.close()
except:
	pass
app = QtGui.QApplication(sys.argv)
window=CGui()
window.show()
app.exec_()