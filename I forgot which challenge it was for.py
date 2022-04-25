# The aim was to find the biggest combinaison of the product of a list of negatives and positives number

def solution(xs):
    solution_subset = [e for e in xs if e > 1]

    # We split negative and positive and remove 0
    # In the negative something > -1 can be usefull to remove the - of a larger number
    negative = [e for e in xs if e < 0]

    negative.sort(reverse=True)
    # If impair just remove the one nearest 0
    if len(negative) % 2:
        negative.pop(0)

    # We see if the product if each pair of number give something > 1
    while negative:
        first = negative.pop()
        second = negative.pop()
        if first * second > 1:
            solution_subset.append(first)
            solution_subset.append(second)
            break
            # Since the array is sorted, we can just append everything else
            # we one is found

    print(solution_subset)
    for e in negative:
        solution_subset.append(e)
    
    total = 1
    for e in solution_subset:
        total *= e
        
    return str(total)
