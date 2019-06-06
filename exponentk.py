def check_Power(N,k):
    if N <= 0 or k <=0:
        print "not a valid input"
    else:
        for i in range (1,20):
            x = k**i
            if x > N :
                print " false"
                break
            elif x == N:
                print "true"
                print k,"power ",i,"is",N
                break

check_Power(244140625,5)
check_Power(4096, 16)
check_Power(0, 16)
check_Power(1,1)
