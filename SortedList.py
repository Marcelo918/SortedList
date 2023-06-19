'''
Description: This function returns the sorted list in ascending order if parameter 'reverse'
             is False. The function returns the sorted list in descending order if parameter
             'reverse' is True. 
'''

'''
# ******************************************************************************
# *                               COPYRIGHT NOTICE                             *
# ******************************************************************************
# *                                                                            *
# *  This code is authored by Marcelo Villalobos Diaz                          *
# *  You are free to use, modify, and distribute this code, provided           *
# *  you give appropriate credit by including the author's name.               *
# *                                                                            *
# *  Copyright (c) 2023 Marcelo Villalobos Diaz                                *
# *                                                                            *
# ******************************************************************************
'''

def sort(alist, reverse):
    if reverse == False:
        for j in range(0, len(alist), 1):
            for i in range(0, len(alist)-1, 1):
                if alist[i] > alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
    elif reverse == True:
        for j in range(0, len(alist), 1):
            for i in range(0, len(alist)-1, 1):
                if alist[i] < alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
    print(alist)


my_list = [5, 1, 4, 3, 2]
my_second_list = [4, 8, 0, 1, 9, 6, 3, 2, 7, 5]

sort(my_list, False)
sort(my_list, True)
sort(my_second_list, False)
sort(my_second_list, True)
