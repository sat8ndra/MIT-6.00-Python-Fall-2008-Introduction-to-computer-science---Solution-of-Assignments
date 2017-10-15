### Problem Set 1
### Name: Satyendra gupta
### Collaborators: None
### Time: 10:00
###
prime = True
number = 3
devisor = 2
for prime_count in range(0,1000):
    if prime_count == 999 :  ##this condition check 1000th prime number count and print 
        print(number - 1 )
        break
    while prime :
        ##prime is logical variable default set to true for loop continuation
        if (number%devisor) == 0 : ##if devisor compleatly devides the number then skip the number by incrementing it
            number = number + 1
            devisor = 2  ## and devisor reset to 2 for next number
        else :
            if number > (devisor + 1) :   ##if number not devised then increment the devisor and recheck it
                devisor = devisor + 1
            else :
                number = number + 1   ##if denominator exceeds the numerator then increament number and reset the devisor 2 .it also represent that number is prime, but we have

                                    ## incremented the number so that the prime number will be number -1
                devisor = 2
                prime = False
    prime = True
