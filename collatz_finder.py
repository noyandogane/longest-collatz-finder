number = 0
restart = False
longest_chain_len = 0
longest_chain = []
answer = 0
chain = []
highest_number = 0
lc_highest_number = 0

def start(number, restart, longest_chain, longest_chain_len, highest_number, lc_highest_number): # start function
    print("\n" * 100)
    if restart is False:        
        print("Welcome to the Collatz Conjecture finder!\n")
        print("The Collatz Conjecture is a conjecture in mathematics that concerns a sequence defined as follows:\nStart with any positive integer n.\n"
        "Then each term is obtained from the previous term as follows:\nIf the previous term is even, the next term is one half the previous term.\n"
        "If the previous term is odd, the next term is 3 times the previous term plus 1.\n\n"
        "The conjecture is that no matter what value of n, the sequence will always reach 1.")
        print("This program will find the longest chain of numbers that can be reached from a starting number.")
        print("\n")
        print("Author: @noyandogane\n")
        print("Github: github.com/noyandogane\n\n")
        
        try:
            number = int(input("Please enter a number to start the program: "))
            print("\n" * 2)                
        except ValueError:
            while True:
                try:
                    number = int(input("Invalid input!\nPlease enter a number: "))
                    print("\n" * 2)
                except ValueError:
                    continue
                else:
                    break                 
                                              
    iterations = 0
    highest_number = number
    chain.clear()    
    if number % 2 == 0:
        chain.append(str(number) + "↓↓")
    else:
        chain.append(str(number) + "↑↑")

    collatz(number, iterations, longest_chain, longest_chain_len, highest_number, lc_highest_number, chain, restart)


def longest_chain_var(chain, longest_chain, longest_chain_len, lc_highest_number, highest_number): # function to update the longest chain
    if len(chain) > longest_chain_len:
        print("New longest chain found!")
        longest_chain_len = len(chain)
        lc_highest_number = highest_number
        longest_chain = chain.copy()
    return longest_chain, longest_chain_len, lc_highest_number
 

def collatz(number, iterations, longest_chain, longest_chain_len, highest_number, lc_highest_number, chain, restart):  # collatz function    
    while True:
        if number % 2 == 0:
            number = int(number / 2)
            chain.append(str(number) + "↓↓")
        else:
            number = 3 * number + 1
            if number > highest_number:
                highest_number = number
            chain.append(str(number) + "↑↑")
        iterations += 1

        if number == 1:
            if len(chain) > longest_chain_len:
                longest_chain, longest_chain_len, lc_highest_number = longest_chain_var(chain, longest_chain, longest_chain_len, lc_highest_number, highest_number)

            print("\n" * 100)
            print("Best chain so far:")
            print("=" *50)
            print("Starting number: \n" + str(longest_chain[0][0]))
            print("Chain length: \n" + str(longest_chain_len))
            print("The highest number ever reached: \n" + str(lc_highest_number))
            print("The longest chain found: ", longest_chain)
            iterations += 1            
            print("=" *50, "\n")
            print("Current chain")
            print("=" *50)
            print("Starting number:")
            print(chain[0][0])
            print("Highest number:")
            print(highest_number)
            print("Chain length:")
            print(len(chain))
            print("Chain: ", chain)
            print("=" *50)

            try:
                answer = input("If you want to try a new number enter a number again, if you want to reset the best chain enter reset: ")
                if answer == "reset":
                    longest_chain.clear()
                    longest_chain_len = 0
                    lc_highest_number = 0
                    lc_highest_number = 0
                    print("Best chain reset!")
                answer = int(answer)
            except ValueError:
                while True:
                    try:
                        answer = input("Invalid input!\nPlease enter a number or to reset the best chain enter reset: ")
                        print("\n" * 2)
                    except ValueError:
                        continue
                    else:
                        restart = True
                        number = answer
                        start(number, restart, longest_chain, longest_chain_len, highest_number, lc_highest_number)
            else:
                restart = True
                number = answer
                start(number, restart, longest_chain, longest_chain_len, highest_number, lc_highest_number)            
       
            
start(number, restart, longest_chain, longest_chain_len, highest_number, lc_highest_number) # start the program
