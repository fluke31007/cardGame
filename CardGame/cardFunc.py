import random
class stat(object):
	"""docstring for stat"""
	def __init__(self):
		self.HP = 0
		self.atk = 0
		self.defend =0
		self.brk =0


class Hero(stat):
	"""docstring for Hero"""
	def __init__(self):
		super(Hero, self).__init__()
		self.hp = 300
		self.atk = 50
		self.deff = 30
		self.brk = 70
		self.pick = 0
class Monster(stat):
	"""docstring for Monster"""
	def __init__(self):
		super(Monster, self).__init__()
		self.hp = 300
		self.atk = 40
		self.deff = 30
		self.brk = 50

		self.cardM = random.randint(0,3)
	def setAi(self):
		self.cardM = random.randint(0,3)

class Playgame(object): 
	def __init__(self,Hero,Monster):
		super(Playgame,self).__init__()
		self.Hero = Hero
		self.Monster= Monster
		self.Pu= 0
		self.Mu =0
		self.TT =0
		self.HDM = 0
		self.MDM =0
		self.healP =0
	def battle(self):
		self.Monster.setAi()
		self.Mu = self.Monster.cardM
		self.Pu = self.Hero.pick


	def action(self):
		if self.Hero.hp <=0:
			self.Hero.hp =0
		if self.Monster.hp <=0:
			self.Monster.hp = 0
		if self.Pu==0 and self.Mu==0:
			#self.Hero.hp = self.Hero.hp-self.Monster.atk
			#self.Monster.hp = self.Monster.hp-self.Hero.atk

			self.HDM = 40
			self.MDM = 50
			self.TT +=1
			self.healPH = 0
			self.healPM = 0
			print'-	--------------'
			print'you use card Attack: %s'%(self.Pu)
			print'Monster use card Attack: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==0 and self.Mu ==1:
			#self.Monster.hp = self.Monster.hp-(self.Hero.atk-self.Monster.deff)

			self.TT +=1
			self.HDM=0
			self.MDM=20
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card Attack: %s'%(self.Pu)
			print'Monster use card Defend: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==0 and self.Mu ==2:
			#self.Monster.hp = self.Monster.hp-self.Hero.atk

			self.TT +=1
			self.HDM=0
			self.MDM=50
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card Attack: %s'%(self.Pu)
			print'Monster use card BRK: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==1 and self.Mu ==0:
			#self.Hero.hp = self.Hero.hp-(self.Monster.atk-self.Hero.deff)
			self.TT +=1
			self.HDM=10
			self.MDM =0
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card Defend: %s'%(self.Pu)
			print'Monster use card Attack: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==1 and self.Mu ==1:
			self.TT +=1
			self.HDM=0
			self.MDM=0
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card Defend: %s'%(self.Pu)
			print'Monster use card Defend: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==1 and self.Mu ==2:
			#self.Hero.hp = self.Hero.hp-self.Monster.brk

			self.TT +=1
			self.HDM=50
			self.MDM=0
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card Defend: %s'%(self.Pu)
			print'Monster use card BRK: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==2 and self.Mu ==0 :
			#self.Hero.hp = self.Hero.hp-self.Monster.atk

			self.TT +=1
			self.HDM=40
			self.MDM=0
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card BRK: %s'%(self.Pu)
			print'Monster use card Attack: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==2 and self.Mu ==1 :
			#self.Monster.hp = self.Monster.hp-self.Hero.brk

			self.TT +=1
			self.HDM=0
			self.MDM=70
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card BRK: %s'%(self.Pu)
			print'Monster use card Defend: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==2 and self.Mu ==2 :
			#self.Monster.hp = self.Monster.hp-self.Hero.brk
			#self.Hero.hp = self.Hero.hp-self.Monster.brk
			
			self.TT +=1
			self.HDM=50
			self.MDM=70
			self.healPH = 0
			self.healPM = 0
			print'---------------'
			print'you use card BRK: %s'%(self.Pu)
			print'Monster use card BRK: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==3 and self.Mu==0 :
			self.healPH = 1
			self.healPM =0
			#self.Hero.hp = self.Hero.hp-self.Monster.atk
			
			self.TT +=1
			self.HDM=40
			self.MDM=0
			print'---------------'
			print'you use card HEAL: %s'%(self.Pu)
			print'Monster use card Attack: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==3 and self.Mu==1:
			self.healPH = 1
			self.healPM = 0

			self.TT +=1
			self.HDM=0
			self.MDM=0
			print'---------------'
			print'you use card HEAL: %s'%(self.Pu)
			print'Monster use card Defend: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==3 and self.Mu==2:
			self.healPH = 1
			self.healPM =0
			#self.Hero.hp = self.Hero.hp-self.Monster.brk
			
			self.TT +=1
			self.HDM=50
			self.MDM=0
			print'---------------'
			print'you use card HEAL: %s'%(self.Pu)
			print'Monster use card Brk: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==3 and self.Mu==3:

			self.TT +=1
			self.healPH = 1
			self.healPM = 1
			self.HDM=0
			self.MDM=0
			print'---------------'
			print'you use card HEAL: %s'%(self.Pu)
			print'Monster use card HEAL: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==0 and self.Mu==3:
			#self.Monster.hp = self.Monster.hp-self.Hero.atk

			self.TT +=1
			self.healPH = 0
			self.healPM = 1
			self.HDM=0
			self.MDM=50
			print'---------------'
			print'you use card Attack: %s'%(self.Pu)
			print'Monster use card HEAL: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==1 and self.Mu==3:
			self.TT +=1
			self.healPH = 0
			self.healPM = 1
			self.HDM=0
			self.MDM=0
			print'---------------'
			print'you use card Deffend: %s'%(self.Pu)
			print'Monster use card HEAL: %s'%(self.Mu)
			print'---------------'
		elif self.Pu==2 and self.Mu==3:
			#self.Monster.hp = self.Monster.hp-self.Hero.brk
			self.TT +=1
			self.healPH = 0
			self.healPM = 1
			self.HDM=0
			self.MDM=70
			print'---------------'
			print'you use card BRK: %s'%(self.Pu)
			print'Monster use card HEAL: %s'%(self.Mu)
			print'---------------'
		elif self.Hero.hp>300:
			self.Hero.hp = 300
		elif self.Monster.hp>300:
			self.Monster.hp = 300
a = Hero()
b = Monster()
xx = Playgame(a,b)
