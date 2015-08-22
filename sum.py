def sum(numberList):
  if len(numberList) == 1:
     return numberList[0]		
  return numberList[0]+sum(numberList[1:])
	
	
