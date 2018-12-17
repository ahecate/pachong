
available_toppings = ['mu','ol','gp','pe','pi','ex']

requested_toppings=['ol','gp','pe']

requested_toppings.append('meat')
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print('Adding ' + requested_topping + '.')
        else:
            print('Sorry. We don\'t have '+requested_topping+'.')
            
    print('\nFinished making your Pizza!')

else:
    print('Are you sure you want a plain pizza?')



