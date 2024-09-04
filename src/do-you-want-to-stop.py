# You should write a loop around this question, and keep asking until
# the answer is "yes" (lower case).
answer = "no"

while answer == "no":
    print("Hello, World!")
    
    while True:
        stop = input("Do you want to stop?: ").lower()
        
        if stop in ["yes", "no"]:
            answer = stop
            if answer == "yes":
                print("Stopped.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
