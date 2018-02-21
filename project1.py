def problem1()

def problem2()



def main()
  choice = '0'
  while choice != 'q'
    print("Please choose a problem.")
    print("Type '1' for the first problem.")
    print("Type '2' for the second problem.")
    print("Type 'q' to quit.")
    choice = input("--")

    if choice == '1'
      problem1()
    if choice == '2'
      problem2()
    if choice == 'q'
      #break out of while and exit main
    
main()
