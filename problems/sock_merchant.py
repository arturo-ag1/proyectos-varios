#!/bin/python3

#John works at a clothing store. He has a large pile of socks that he must pair by color for sale.
# Given an array of integers representing the color of each sock, determine how many pairs of socks
# with matching colors there are.


import math

sockList = [10,20,20,10,10,30,50,10,20]
socksIgnored = []
socksNumber = 9

def setHyphens(sockNumber,tmpSockList):
	amount = 0
	for i in range(len(tmpSockList)):
		if tmpSockList[i] == sockNumber:
			tmpSockList[i] = "-"


def sockMerchant(socksNumber,sockList):
	tmpSockList = sockList.copy()
	sockPairs = 0
	for sock in tmpSockList:
		if(sock != "-"):
			if math.floor(tmpSockList.count(sock)/2) > 0:
				sockPairs = sockPairs + math.floor(tmpSockList.count(sock)/2)
				setHyphens(sock,tmpSockList)

	return sockPairs

sockPairs = sockMerchant(socksNumber,sockList)

print("Socks Merchant:")
print(sockList)
print("-----------")
print(sockPairs)
