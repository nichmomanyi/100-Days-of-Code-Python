# numbers = [1,2,3]
# new_numbers = [number + 1 for number in numbers]

# news = [x*2 for x in range(1,5)]
# print(news)
def add(*numbers):
    sum=0
    for n in numbers:
        sum+=n
    print (sum)

add(3,5,6,4)

def calculate(**math):
    print(math)
    # for key, value in math.items():
    #     #print(key)
    #     print(value)
    print(math["add"])


calculate(add = 5, multiply = 6)