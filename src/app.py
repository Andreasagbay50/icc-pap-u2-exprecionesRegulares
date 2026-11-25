import re


def main():
    runEjemplo1()
    runEjemplo2()
    runEjemplo3()
    
def runEjemplo1():
    patron = "ab*"
    palabras = ["a", "ab", "abbb", "abab", "b", ""]

    for p in palabras:
 
        print(p, "->", bool(re.fullmatch(patron, p)))
        


def runEjemplo2():
    regex = r"[TO][0-9]{3}"
    lista = ["T001", "O120", "T01", "X001", "T0001"]

    for codigo in lista:
       res= re.fullmatch(regex,codigo)
        print(f "{codigo},  => {bool(res)}"):

    
    
if __name__== "__main__":
    main()
