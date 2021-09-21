def atand(list): #输入项可以是列表或者元组 
    number_a=-len(list)
    print("这里有"+str(-number_a)+"个数据")
    str_b=" "
    while number_a<0:
        number_c=list[number_a]
        str_b=str_b+"&"+str(number_c)
        number_a=number_a+1
    return str_b