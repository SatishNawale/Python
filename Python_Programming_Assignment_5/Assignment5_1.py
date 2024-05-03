# 1. Write a recursive program which display below pattern.

# Input : 5
# Output : *    *   *   *   *

def print_pattern(No):
    if(No!=0):
        print("*", end="\t")
        No = No-1
        print_pattern(No)

def main():
    print("Please enter input : ", end = " ")
    No = int(input())
    print()
    
    print_pattern(No)

if __name__ == "__main__":
    main()