# SOMETHING FOR FUN
# TOTALLY spontaneous idea
# that game we played, where you can't say a number with 7 in it,
# or any number that's divisible by 7
# lets make a fucking program for that
# and uncover the mysteries of 7 shall we
# i just am really fed up with my compsci hw rn

def div_by_seven(num):
    if num % 7 == 0:
        return True
    else:
        return False
#11/7/21: made the divide by seven a function as well,
#to streamline the code a bit

def has_seven(num):
    test_num = str(num)
    for i in test_num: 
        if i != '7': 
            continue
        elif i == '7':
            return True
            break
#idk how to import module so. function definition. deal w it
if __name__ == '__main__':        
    print('welcome to the seven game! haha')
    print('so you can\'t say any numbers that are divisible by or that contain seven')
    print('i think some of those numbers are stupid, so i made python do it for me')

    num1 = int(input('Enter a lower bound: '))
    num2 = int(input('Enter an upper bound: '))
    if num1 <= num2:
        num_list = list(range(num1,(num2+1)))
    elif num1 > num2:
        num_list = list(range(num1,(num2-1),-1))
    else:
        print('Sorry, invalid range TwT')
    #just for debugging: delete in final product
    #print('Analyzed range:',num_list)

    forbidden_list = list()
    for num in num_list:
        if (div_by_seven(num) == True) or (has_seven(num) == True):
            forbidden_list.append(num)
            
    no_repeats = list(set(forbidden_list))
    if num1 <= num2:
        forbidden_list = sorted(no_repeats)
    elif num1 > num2:
        forbidden_list = sorted(no_repeats,reverse=True)

    if forbidden_list == []:
        print('You can say all of these numbers!')
    else:
        if len(forbidden_list) == 1:
            print('Don\'t say the number:',forbidden_list)
        else:
            print('Don\'t say the numbers:',forbidden_list)

'''
part one: nums divisible by 7, complete!
part two: IM DONE, even though it's a bit sloppy
EVERYHTING WORKS.
IM SO PROUD OF MYSELF.
truly a well spent hour
might streamline the code in a later "fuck my work" session
- 11/3/21

let code sort from min to max, or max to min automatically,
depending on the bounds entered? (FIXED: used sorted function from internet)
fix the grammar thing with number(s) (FIXED)
find a better way to do range: i stole the "less efficient"
range one from my prime numbers project
make it print the list without the brackets?
- 11/4/21
'''
