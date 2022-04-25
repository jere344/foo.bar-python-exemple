#Fuel Injection Perfection
#The fuel control mechanisms have three operations:

#Add one fuel pellet
#Remove one fuel pellet
#Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half,
#the safety controls will only allow this to happen if there is an even number of pellets)
#Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations
#needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, 
#so there won't ever be more pellets than you can express in that many digits.

#For example:

#answer(4) returns 2: 4 -> 2 -> 1  
#answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1


def solution(n):
    n = int(n)
    cycle = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            cycle += 1

        else:
            plus_one_cycle = 1
            t_plus = n + 1
            while t_plus % 2 == 0:
                t_plus = t_plus / 2
                plus_one_cycle += 1

            minus_one_cycle = 1
            t_minus = n - 1
            while t_minus % 2 == 0:
                t_minus = t_minus / 2
                minus_one_cycle += 1

            if t_minus < t_plus:
                n = t_minus
                cycle += minus_one_cycle

            elif t_minus > t_plus:
                n = t_plus
                cycle += plus_one_cycle
            else:
                if minus_one_cycle < plus_one_cycle:
                    n = t_minus
                    cycle += minus_one_cycle
                else:
                    n = t_plus
                    cycle += plus_one_cycle

    return cycle
