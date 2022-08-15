#Q1/Write a method that will remove any given character from a String?
def chr():
    TEXT_STR=input("Enter any text:")
    Excluded_Character=input("Enter a letter to remove it from the text:")
    TEXT_STR=TEXT_STR.replace(Excluded_Character,'')
    print(TEXT_STR)
chr()
#Q2/Write a program to find all prime numbers up to a given range of numbers?

def Pnumber(Any_Num):
    is_prime = False
    if Any_Num > 1:
        for i in range(2, Any_Num):
            if (Any_Num % i) == 0:
                is_prime = True
                print("Not prime ")
                break
    if not is_prime:
        print("iS Prime number")
        
N=2
while N>1:
    N=int(input("ENTER Number:"))
    Pnumber(N)

#Q3/write a function that count how many the given character repeated in a given string?
test_string =input("ENTER string:")
char_rep=input("Enter Rep_Char:")
count_rep=0
for i in test_string:
    if i == char_rep:
        count_rep+=1
print('count number in string:',count_rep)
