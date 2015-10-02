class box:
	def __init__(self, n):
		self.b = n
		self.bdimx = 0
		self.bdimy = 0
		self.bdimz = 0
		self.cornx = 0
		self.corny = 0
		self.cornz = 0
		self.free = True

class Tower:
	def __init__(self):
		self.tvalue = 0
		self.tloss = 0
		self.tdim1 = 0
		self.tdim2 = 0
		self.tBoxes = []
		self.bbasis = -1

def bestTowerUsing(b):
	#for all three height combos, generate a tower
	#return best tower
	return

def generateTower(b):
	#generate a tower using given b dimensions
	# Algo #2
	return

def sort(TNew):
	#Sort tower set based on tloss
	return

def reduceSet(TNew):
	#remove all towers nondisjunct with previous towers
numboxes = 100
boxes = []

for i in range(0,numboxes):
	nBox = box(i)
	boxes.append(nBox)
int nsteps = 20

TSet = []
BFree = []

for istep in range(nsteps):
	TNew = []
	BFree = []
	for i in range(numboxes):
		if boxes[i].free:
			BFree.append(boxes[i])

	for freeBox in BFree:
		tnext = bestTowerUsing(freeBox)
		TNew.append(tnext)

		if istep == nsteps - 1:
			assert True

			for fbox in tnext:
				fbox.free = False
	
	if isteps < nsteps - 1:
		sort(TNew)
		reduceSet(TNew)
	#Should BFree be updated here? I think it should. Not explicitly mentioned in the paper though
	#If Bfree is not updated, then the next step will be exactly the same as this one. Makes no sense
	for tower in TNew:
		'''
		for bbox in tower:
			bbox.free = False
		'''
		TSet.append(tower)
sort(TSet)
