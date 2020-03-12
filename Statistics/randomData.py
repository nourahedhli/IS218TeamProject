import random
import pprint


def random_code():
    random.seed(6)
    randomData1 = []
    randomData2 = []
    i = 0
    while i < 6:
        rand_value = random.randint(1, 50)
        randomData1.append(rand_value)
        value = random.random()
        rand_value_decimal = round(value, 2)
        randomData2.append(rand_value_decimal)
        i += 1
        randomData1.sort()
        randomData2.sort()
        num_list = randomData2 + randomData1

        return num_list


def random_code_withoutSeed():
    randomData1 = []

    i = 1
    while i < 3:
        y = random.randint(4, 300)
        randomData1.append(y)
        x = "{0:.2f}".format(random.random())
        randomData1.append(x)
        i += 1

    # pprint.pprint(randomData1)
    return randomData1


def random_select():
    random.seed(6)
    randomData1 = []

    i = 0
    rand_list = [10,20,30,40,50,60]
    rand_valueList = random.choices(rand_list,k=4)
    i+=1
    #rand_value = random.choice(rand_list)
    #randomData1.append(rand_value)

    #pprint.pprint(rand_value)
    #pprint.pprint(rand_valueList)
    #return rand_value
    return rand_valueList


def random_select_no_seed():
    random.seed()
    randomData1 = []

    i = 0
    rand_list = [10, 20, 30, 40, 50, 60]
    rand_valueList = random.choices(rand_list, k=4)
    i += 1

    rand_value = random.choice(rand_list)
    randomData1.append(rand_value)

    #pprint.pprint(randomData1)
    #pprint.pprint(rand_valueList)

    return rand_valueList