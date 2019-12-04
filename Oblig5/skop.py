"""
Oppgave 3: Skop
"""
"""
Først vil minFunksjon defineres, ingenting inni dets skop vil kjøres før den kalles på.
Deretter hovedrogram defineres, tilsvarende vil skje. 
Så vil hovedprogram bli kalt på, slik at alt innenfor skopet til hovedprogram vil bli kjørt.
Følgende lokale variabler (lokale for hovedprogram) blir definert, a = 42 og b = 0. b vil 
så skrives ut til konsollen. b settes så lik a, som er 42. a kaller så på minFunksjon() 
og skal settes som funksjonens returverdi. Da kjøres alt innefoner minFunksjons skop. 
Det kjøres en for-løkke, der følgende lokale variabler (lokale for minFunksjon) blir definert:
c får verdi 2, og printes så. c blir omdefinert til c+1, b blir definert lik 10. 
b blir så satt lik b + a, som gir feilmelding fordi a ikke er definert innen minFunksjon eller 
som en global variabel. Programmet kjører ikke videre. 
"""

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()