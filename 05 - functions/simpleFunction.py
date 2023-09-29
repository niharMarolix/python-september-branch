p = 10000
r = 8
t = 10


def siAndAmount(principal, rateOfInterest, timeInYears): # the values passed inside the functions are called as paramters or positional arguements
    SI = ((principal*rateOfInterest*timeInYears))/100
    Amount = SI+principal
    print(int(Amount))
p = 20000
r = 8
t = 10
siAndAmount(p,r,t) # calling the siAndAmount function
# when we are calling a function then the passes value are arguements

