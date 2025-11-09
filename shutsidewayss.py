def shutdown():
    response = input("Do you want to shut down yes or no: ")
    
    if response == "yes":
        print("Shutting down")
    elif response == "no":
        print("Shutdown aborted.")
    else:
        print("Sorry")
shutdown()