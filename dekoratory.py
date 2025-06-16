def dekorator(funkcja):
    def opakowanie():
        print("Coś przed funkcją")
        funkcja()
        print("Coś po funkcji")
    return opakowanie

@dekorator
def przywitaj():
     print("Cześć!")

przywitaj()

###################################################
###################################################