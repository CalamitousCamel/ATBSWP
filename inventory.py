bag={'arrow':12, 'gold':42, 'rope': 1, 'torch':6, 'dagger':1}
dragonloot=['gold', 'dagger', 'gold', 'gold', 'ruby']

def lsinventory(var):
	total=0
	print('Inventory:')
	for i,n in var.items():			#dictionary var.key() and var.value() variables are passed to i and n respectively
		print(str(n)+' '+i)
		total=total+n
	print('Total number of items: '+str(total))

def addtoinventory(playerbag,loot):
	for lootitem in loot:						# gets each item in loot list
			if lootitem in playerbag.keys():	# compares it to playerbag's key list
				playerbag[lootitem]+=1			# adds 1 for every matching list item
			else:
				playerbag.setdefault(lootitem,1)# or makes a new one and gives it a value of 1

lsinventory(bag)
addtoinventory(bag,dragonloot)
print()
lsinventory(bag)