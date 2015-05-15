def abc_store_check():
    
    print "Welcome to the ABC age checker"
    
    print "Please enter your age"
    answer = int(raw_input())
    
    if answer < 21:
        print "Sorry, you are not old enough to shop at the ABC store"
        return False
        
    elif answer > 21:
        print "Congratulations, you may shop at the ABC store."
        return True
    
    elif answer == 21:
        print "Good try McLovin...."
        return True
        
        abc_store_check()
        
abc_store_check()
