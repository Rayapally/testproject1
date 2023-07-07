def vehicles(cost):


    if(cost > 30000):
        print("cars")

    else:
        print("bikes")


cost = int(input("Enter the cost :"))
vehicles(cost)