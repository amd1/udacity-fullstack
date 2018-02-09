def withdraw(balance, request):
    print "="*40
    balance1=balance
    request1=request
    if request <= 0:
        print("Enter an amount greater than Zero plz !")
    else:
        if request > balance:
            print("Your balane is not enough !")
        else:
            while request > 0:
                if request >= 100:
                    request -= 100
                    print("give 100")
                elif request >= 50:
                    request -= 50
                    print("give 50")
                elif request >= 10:
                    request -= 10
                    print("give 10")
                elif request >= 5:
                    request -= 5
                    print("give 5")
                else:
                    if request < 5:
                        print("give " + str(request))
                    request = 0
            print "current balance is " +str(balance1-request1)
    print "="*40



withdraw(500, 500)
withdraw(500, -10)
withdraw(500, 0)
withdraw(500, 277)
