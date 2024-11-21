AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

def startProgram():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("\n1. PRINT all Authorized Vehicles")
    print("2. Exit")
    
startProgram()
response = input("")
if (response == "1"):
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for cars in AllowedVehiclesList:
        print(cars)
        
    startProgram()
    response = input("")
if (response == "2"):
    print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")