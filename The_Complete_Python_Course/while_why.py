
    
# the_force = input('Do you believe you in the force ? (yes/no): ')

# print('May the force  be with you !')

while the_force:

    the_force = input('Do you believe in the force ? (yes/no): ')
     
    if the_force == "yes": 
        print("The force will guide you !")
    else:
        print('you are the darkside !')
        break


order_66 = input('Would you like to initiate Order 66, if you believe in the darkside of the force ?(yes/no)')
    
if order_66 == "yes":
    print(f'Emperor will execute order 66 !')
