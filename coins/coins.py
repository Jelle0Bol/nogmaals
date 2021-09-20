# name of student: Jelle Bol
# number of student: 99067766
# purpose of program: Adding 2,3,5 euromunten
# function of program: change for money
# structure of program:
Uiteindelijk = '' 

toPay = int(float(input('Amount to pay: '))* 100) #
payed = int(float(input('Payed amount: ')) * 100) #
change = payed - toPay #

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(float(input('How many coins of ' + str(coinValue) +  ' cents did you return? '))) #
      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
      qtyVijf = nrCoinsReturned
      qtyVijf = str(qtyVijf)
      print ('Je hebt ' + qtyVijf + ' van 500 teruggegeven')
      coinValue = 300 
    elif coinValue == 300:
      qtyDrie = nrCoinsReturned
      qtyDrie = str(qtyDrie)
      print ('Je hebt ' + qtyDrie + ' van 300 teruggegeven')
      coinValue = 200
    elif coinValue == 200:
      qtyTwee = nrCoinsReturned
      qtyTwee = str(qtyTwee)
      print ('Je hebt' + qtyTwee + ' van 200 teruggegeven')
      coinValue = 50
    elif coinValue == 50:
      qtyNVijf = nrCoinsReturned
      qtyNVijf = str(qtyNVijf)
      print ('Je hebt ' + qtyNVijf + ' van 50 teruggegeven')
      coinValue = 20
    elif coinValue == 20:
      qtyNTwee = nrCoinsReturned
      qtyNTwee = str(qtyNTwee)
      print ('Je hebt ' + qtyNTwee + 'van 20 teruggekregen')
      coinValue = 10
    elif coinValue == 10:
      qtyNEen = nrCoinsReturned
      qtyNEen = str(qtyNEen)
      print ('Je hebt ' + qtyNEen + 'van 10 teruggekregen')
      coinValue = 5
    elif coinValue == 5:
      vijf = nrCoinsReturned
      vijf = str(vijf)
      print('Je hebt' + vijf + 'van 5 teruggekregen')
      coinValue = 2
    elif coinValue == 2:
      qtyNNTwee = nrCoinsReturned
      qtyNNTwee = str(qtyNNTwee)
      print('Je hebt ' + qtyNNTwee + 'van 2 teruggekregen') 
      coinValue = 1
    else:
      coinValue = 0


if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print ('Done')