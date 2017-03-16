__author__ = 'saurabh'

import random
c=0
def transmitter(msg,gen,gen_code):

    msg1=msg+gen_code
    msg = list(msg)
    error1 = "10010101010101111111111000000111"
    error1 =list(error1)
    msg1=list(msg1)
    gen=list(gen)

    for i in range(len(msg1)-len(gen)):
        if msg1[i]== '1':
            #print(transmitted_msg1[i])
            for j in range (len(gen)):
                msg1[i+j] = str((int(msg1[i+j])+int(gen[j]))%2)
                #print(">" + (transmitted_msg1[i+j]))

    remainder=(msg1[-(len(gen)-1):])

    print ("remainder","".join(remainder))
    transmitted_msg=msg+remainder
    print ("Message to be transmited without error is","".join(transmitted_msg))
    #32 bit error generator    ''' to generate error equal to 32 bit remove comment from below line 27-28 only and comment accordingly other line'''
    #error_len = 32
    #transmitted_msg= msg+error1
    #<32 bit error generator   '''to generate error less than 32 bit remove comments from 30-32 and comment accordingly other line'''
    for l in range(1505,1533):
        error_len = 27
        transmitted_msg[l]=str(random.randint(0,1))
    #>32 bit error generator  '''to generate error less than 32 bit remove comments from 34-36 and comment accordingly other line'''
    '''for l in range(1475,1533):
        error_len = 57
        transmitted_msg[l]=str(random.randint(0,1))'''
    print("Transmitted message with error of length",error_len,"".join(transmitted_msg))
    error_check(transmitted_msg,gen)




def error_check(transmitted_msg1,gen):

    transmitted_msg1 = list(transmitted_msg1)
    #print(transmitted_msg1)
    gen = list(gen)
    #print(gen)

    for i in range(len(transmitted_msg1)-len(gen)):
        if transmitted_msg1[i]== '1':
            #print(transmitted_msg1[i])
            for j in range (len(gen)):
                transmitted_msg1[i+j] = str((int(transmitted_msg1[i+j])+int(gen[j]))%2)
                #print(">" + (transmitted_msg1[i+j]))

    error=(transmitted_msg1[-(len(gen)-1):])
    #print(error)
    error = list(error)
    for k in range(len(error)):
        if error[k] == '1':
            global c
            c+=1
            print("error detected as it has remaider","".join(error),"and in frame number",c)
            break
        elif k == (len(error)-1):

            print("No error")

#error_check("100000010000","11001")


for j in range(1000):
    rand_byte=[]
    for i in range(1520):
        a = str(random.randint(0,1))
        rand_byte.append(a)

    rand_bit="".join(rand_byte)
    new_gen="100000100110000010001110110110111"
    new_gen_code="0"*32

    #M=rand_bit+new_gen_code
    #print(M)
    transmitter(rand_bit,new_gen,new_gen_code)
