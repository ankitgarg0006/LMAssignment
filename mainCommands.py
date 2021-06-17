
items = {}

inventoryItems = {}

users = {}

userCart = {}

import sys, os

class Item:
	def __init__(self):
		pass
	
	@staticmethod
	def createItem(itemCategory, brand, price):
		try:
			commonName = str(itemCategory).strip().lower() + "|||" + str(brand).strip().lower()

			if commonName in items:
				items[commonName]["price"] = float(price)
			else:
				items[commonName] = {
					"IC": itemCategory,
					"brand": brand,
					"price": float(price)
				}
			
			print("Item created successfully")
		except Exception as error:
			print("Error Occurred ", error)



class Inventory:
	def __init__(self):
		pass
	
	@staticmethod
	def addInventory(itemCategory, brand, quantity):
		try:
			commonName = str(itemCategory).strip().lower() + "|||" + str(brand).strip().lower()
			if commonName in items:
				if commonName in inventoryItems:
					inventoryItems[commonName]["quantity"] += int(quantity)
				else:
					inventoryItems[commonName] = {
						"IC": itemCategory,
						"brand": brand,
						"quantity": int(quantity)
					}
				
				print("Item created successfully")
			else:
				print("Please create the item first!!")
		except Exception as error:
			print("Error Occurred: ", error)


	@staticmethod
	def getInventory():
		try:
			if len(inventoryItems) > 0:
				inventoryItemsString = []
				for k, v in inventoryItems.items():
					inventoryItemsString.append(str(v["IC"]) + " " + str(v["brand"]) + " " + str(v["quantity"]))
				
				print("\n".join(inventoryItemsString))
			else:
				print("Inventory is blank.")
		except Exception as error:
			print("Error Occurred: ", error)


	@staticmethod
	def search(searchType, listItems, searchType2=None, listItems2=[]):
		try:
			itemsFetched = []

			for k, v in inventoryItems.items():
				listItems = [str(i).strip().lower() for i in listItems]
				listItems2 = [str(i).strip().lower() for i in listItems2]
				
				itemCat, brandName = k.split("|||")

				if str(searchType).lower().strip() in ["brand"]:
					if searchType2 is not None:
						if str(searchType2).lower().strip() in ["category"]:
							if (brandName in listItems) and (itemCat in listItems2):
								itemsFetched.append(str(v["IC"]) + " " + str(v["brand"]) + " " + str(v["quantity"]))
					else:
						if brandName in listItems:
							itemsFetched.append(str(v["IC"]) + " " + str(v["brand"]) + " " + str(v["quantity"]))
				
				elif str(searchType).lower().strip() in ["category"]:
					if searchType2 is not None:
						if str(searchType2).lower().strip() in ["brand"]:
							if (itemCat in listItems) and (brandName in listItems2):
								itemsFetched.append(str(v["IC"]) + " " + str(v["brand"]) + " " + str(v["quantity"]))
					else:
						if itemCat in listItems:
							itemsFetched.append(str(v["IC"]) + " " + str(v["brand"]) + " " + str(v["quantity"]))
				
				else:
					print("You can search only within brand, category")


			print("\n".join(itemsFetched))
		except Exception as error:
			print("Error Occured: ", error)

class Users:
	def __init__(self):
		pass
	
	@staticmethod
	def addUser(userName, walletAmount):
		try:
			if userName not in users:
				users[userName] = float(walletAmount)
			else:
				users[userName] += float(walletAmount)
		except Exception as error:
			print("Error Occurred: ", error)


	@staticmethod
	def getUserWalletAmount(userName):
		try:
			if userName in users:
				print(users[userName])
			else:
				print("User is not registered yet!!")
		except Exception as error:
			print("Error Occurred: ", error)

	
	@staticmethod
	def setUserWalletAmount(userName, walletAmountToAdd):
		try:
			if userName not in users:
				users[userName] = float(walletAmountToAdd)
			else:
				users[userName] += float(walletAmountToAdd)
		except Exception as error:
			print("Error Occurred: ", error)

		

class Cart:
	def __init__(self):
		pass
	
	@staticmethod
	def addToCart(userName, itemCategory, brand, quantity):
		try:
			if userName in users:
				commonName = str(itemCategory).strip().lower() + "|||" + str(brand).strip().lower()

				if commonName in inventoryItems:
					if inventoryItems[commonName]["quantity"] >= int(quantity):
						if userName in userCart:
							if commonName in userCart[userName]:
								userCart[userName][commonName] += int(quantity)
							else:
								userCart[userName][commonName] = int(quantity)
						else:
							# Create the Item
							userCart[userName] = {
								commonName: int(quantity)
							}
					else:
						print("Quantity of items not available!!")
				else:
					print("Item is not in inventory!!")
			else:
				print("User is not registered. Please create the user first!!")
		except Exception as error:
			print("Error Occurred: ", error)


	
	@staticmethod
	def updateCart(userName, itemCategory, brand, quantity):
		try:
			if userName in users:
				commonName = str(itemCategory).strip().lower() + "|||" + str(brand).strip().lower()

				if commonName in inventoryItems:
					if inventoryItems[commonName]["quantity"] >= int(quantity):
						if userName in userCart:
							if commonName in userCart[userName]:
								userCart[userName][commonName] += int(quantity)
							else:
								# userCart[userName][commonName] = int(quantity)
								print("Item is not added yet. Please add the item.")
						else:
							# # Create the Item
							# userCart[userName] = {
							#     commonName: int(quantity)
							# }
							print("Cart is blank. Please add the item.")
					else:
						print("Quantity of items not available!!")
				else:
					print("Item is not in inventory!!")
			else:
				print("User is not registered. Please create the user first!!")
		except Exception as error:
			print("Error Occurred: ", error)


	
	@staticmethod
	def removeFromCart(userName, itemCategory, brand):
		try:
			if userName in users:
				commonName = str(itemCategory).strip().lower() + "|||" + str(brand).strip().lower()

				if commonName in inventoryItems:
					if userName in userCart:
						if commonName in userCart[userName]:
							userCart[userName].pop(commonName)
						else:
							# userCart[userName][commonName] = int(quantity)
							print("Item is not added yet.")
					else:
						# # Create the Item
						# userCart[userName] = {
						#     commonName: int(quantity)
						# }
						print("Cart is blank. Please add the item.")
				else:
					print("Item is not in inventory!!")
			else:
				print("User is not registered. Please create the user first!!")
		except Exception as error:
			print("Error Occurred: ", error)


	@staticmethod
	def getCart(userName):
		try:
			if userName in users:
				if userName in userCart:
					totalAmount = 0
					totalStringItems = []
					for k, v in userCart[userName].items():
						totalAmount += (v * items[k]["price"])
						totalStringItems.append(str(items[k]["IC"] + " " + str(str(items[k]["brand"] + " " + str(v)))))

					print(", ".join(totalStringItems))
					print("Total Cart Amount is: ", totalAmount)
				else:
					# # Create the Item
					# userCart[userName] = {
					#     commonName: int(quantity)
					# }
					print("Cart is blank. Please add the item.")
			else:
				print("User is not registered. Please create the user first!!")
		except Exception as error:
			print("Error Occurred: ", error)


	
	@staticmethod
	def cartCheckout(userName):
		try:
			if userName in users:
				if userName in userCart:
					totalAmount = 0
					totalStringItems = []

					isNotSuccess = False
					for k, v in userCart[userName].items():
						if int(v) <= inventoryItems[k]["quantity"]:
							totalAmount += (v * items[k]["price"])
						else:
							isNotSuccess = True
							break

					if not isNotSuccess:
						if totalAmount <= users[userName]:
							# Clear the Cart and Update the Wallet
							users[userName] -= totalAmount

							# Update the Inventory
							for k, v in userCart[userName].items():
								inventoryItems[k]["quantity"] -= v

							userCart.pop(userName)
						else:
							print("Wallet amount is insufficient!!")
					else:
						print("Inventory has insufficient quantity of items!")

				else:
					print("Cart is blank. Please add the item.")
			else:
				print("User is not registered. Please create the user first!!")
		except Exception as error:
			print("Error Occurred: ", error)