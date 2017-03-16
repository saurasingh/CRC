__author__ = 'saurabh'

def transmitter(msg,gen,gen_code):

    msg1=msg+gen_code
    msg = list(msg)

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
            print("error detected as it has remainder","".join(error))
            break
        elif k == (len(error)-1):

            print("No error")

transmitter("100000010000","11001","0000")
error_check("100000010000","11001")


