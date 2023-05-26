from time import *
import random as r

def mistake (partest,usertest):
    errer = 0
    for i in range (len(partest)):
        try:
            if partest[i] != usertest[i]:
                errer = errer + 1
        except :
            errer = errer + 1
    return errer


def speed_time (time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__':       
    while True:
        ck = input (' Ready To Test : yes / no :')
        if ck == "yes":

            test = ["Kaiun islam freekancer","najmul islam freelacer,","mirajul ialam freelacet"]
            test1 = r.choice(test)
            print ("\t*****   Thping Speed  *****")
            print (test1)
            print ()
            print ()
            time_1 = time()
            testinput = input ("Enter : ")
            time_2 = time()

            print ('Speed : ', speed_time (time_1,time_2,testinput),"w/sec")
            print ("Error : ", mistake (test1,testinput) ) 

        elif ck == "no":
            print ("Thank You")
            break
        else:
            print (" Wrong Input ")


