available_cars  = ['vitara' , 'endeavour ford' , 'scorpio' , 'creta' , 'fortuner']
requested_cars = ['endeavour ford' , 'fortuner' , 'bmw']

for requested_car in requested_cars:
    if requested_car in available_cars:
        print("requested car " + requested_car + " is available")
    else:
        print("requested car " + requested_car + " is not available")
