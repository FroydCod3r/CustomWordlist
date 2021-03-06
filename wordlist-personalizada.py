import sys
import string
import time
from string import maketrans

table1 = maketrans('aioO', '@100')
table2 = maketrans('aeioOs', '43100$')
table3 = maketrans('aeiou', 'AEIOU')
table4 = maketrans('IilLsS', '1111$$')
list_tables = [table1, table2, table3, table4]

wordlist = open('wordlist.txt', 'w')

def brute_force(number,modo):
    ano2=str(number)[2:]

    with open(sys.argv[1]) as file:
        for line in file:
            wordlist.write(line)
            line=line.rstrip('\n')
            line2 = line+str(number)+"\n"
            wordlist.write(line2)
            line2 = line+"@"+str(number)+"\n"
            wordlist.write(line2)

            for table in list_tables:
                wordlist.write(line.translate(table)+str(number)+"\n")
                wordlist.write(line.translate(table)+"@"+str(number)+"\n")
                wordlist.write((line.translate(table)+"@"+str(number)+"\n").upper())
                wordlist.write((line.translate(table)+str(number)+"\n").upper())
                wordlist.write((line.translate(table)+"@"+str(number)+"\n").lower())
                wordlist.write((line.translate(table)+str(number)+"\n").lower())
                wordlist.write((line.translate(table)+"@"+str(number)+"\n").capitalize())
                wordlist.write((line.translate(table)+str(number)+"\n").capitalize())
                wordlist.write((line.translate(table)+"@"+str(number)+"\n").title())
                wordlist.write((line.translate(table)+str(number)+"\n").title())
                wordlist.write((line.translate(table)+"@"+str(number)+"\n").swapcase())
                wordlist.write((line.translate(table)+str(number)+"\n").swapcase())

    if modo == 1:
        with open(sys.argv[1]) as file:
            for line in file:
                wordlist.write(line)
                line=line.rstrip('\n')
                line2 = line+str(ano2)+"\n"
                wordlist.write(line2)
                line2 = line+"@"+str(ano2)+"\n"
                wordlist.write(line2)

                for table in list_tables:
                    wordlist.write(line.translate(table)+str(ano2)+"\n")
                    wordlist.write(line.translate(table)+"@"+str(ano2)+"\n")
                    wordlist.write((line.translate(table)+"@"+str(ano2)+"\n").upper())
                    wordlist.write((line.translate(table)+str(ano2)+"\n").upper())
                    wordlist.write((line.translate(table)+"@"+str(ano2)+"\n").lower())
                    wordlist.write((line.translate(table)+str(ano2)+"\n").lower())
                    wordlist.write((line.translate(table)+"@"+str(ano2)+"\n").capitalize())
                    wordlist.write((line.translate(table)+str(ano2)+"\n").capitalize())
                    wordlist.write((line.translate(table)+"@"+str(ano2)+"\n").title())
                    wordlist.write((line.translate(table)+str(ano2)+"\n").title())
                    wordlist.write((line.translate(table)+"@"+str(ano2)+"\n").swapcase())
                    wordlist.write((line.translate(table)+str(ano2)+"\n").swapcase())

def main():

    if len(sys.argv) < 2:
        print("\n Exemplo: python "+ sys.argv[0] + " palavras.txt \n")
        sys.exit(0)
    else:
        modo = input("\n[-] Qual modo deseja que seja executado? \n(1) Humano\n(2) Insano\n")
        if int(modo) == 1:
            number = input("\n[-] Qual o ano (yyyy)? ")
            while len(str(number)) < 4:
                number = input("\n[-] Digite o ano no formato YYYY: ")
            brute_force(number,modo)
        else:
            print ("\n")
            print ("*"*38)
            print ("**** YEAH!!!!!! Rock Your PC! :-D ****")
            print ("*"*38)
            for torta in range(9999):
                number='{:d}'.format(torta).zfill(4)
                brute_force(number,modo)
            print ("Loading... 25%")
            time.sleep(1)
            for torta in range(999):
                number='{:d}'.format(torta).zfill(3)
                brute_force(number,modo)
            print ("Loading... 50%")
            time.sleep(2)
            for torta in range(99):
                number='{:d}'.format(torta).zfill(2)
                brute_force(number,modo)
            print ("Loading... 75%")
            time.sleep(1)
            for torta in range(9):
                number='{:d}'.format(torta).zfill(1)
                brute_force(number,modo)
            print ("Loading... 100%")
            time.sleep(2)

        with open(sys.argv[1]) as file:
            for line in file:
                line=line.rstrip('\n')
                for table in list_tables:  
                    wordlist.write(line.translate(table)+"\n")
                    wordlist.write((line.translate(table)+"\n").upper())
                    wordlist.write((line.translate(table)+"\n").lower())
                    wordlist.write((line.translate(table)+"\n").capitalize())
                    wordlist.write((line.translate(table)+"\n").title())
                    wordlist.write((line.translate(table)+"\n").swapcase())

    print ("\n[-][-] FINISH!!!!")
    wordlist.close()

if __name__ == '__main__':
  main()