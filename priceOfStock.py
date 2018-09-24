'''
1. Skrifið forrit sem spyr notanda fyrst um fjölda hlutabréfa 
síðan um verðupplýsingar (verð sérhvers hlutar) sem einn streng sem inniheldur
heiltöluhluta ($) og brot (teljara og nefnara). T.d. stendur verðstrengurinn
“29 7 8”, fyrir verðið 29 7/8 eða 29,875. Innslegnar upplýsingar skal
villutékka, þ.e. tryggja skal að inntakið sé eingöngu tölustafir. Notið tryexcept
til að meðhöndla villur í inntakinu.

2. Markaðsvirði bréfanna er síðan skrifað út með tveimur aukastöfum. Notanda
er gefið kost á að endurtaka þetta eins oft og hann vill.
Við lausnina eigið þið eingöngu að nota aðferðir/efni sem fjallað er um í
fyrstu 6 köflunum í kennslubókinni.

3. Brjótið verkefnið upp í einstök hlutverkefni. Fyrir utan lykkjuna skal
aðalforritið aðeins vera runa af fallaköllum. Þið þurfið sjálf að finna út hvaða
föll eru nauðsynleg. Sjáið til þess að endurtekinn kóði sé ekki til staðar eða
a.m.k. í algjöru lágmarki.

'''



def bref():
    while True:
        try:
            fjoldi = int(input("Enter number of shares: "))
            return fjoldi
        except:
            print("Invalid number!")
        

def verdid():
    while True:
        verd = ""
        try:
            verd = str(input("Enter price (dollars, numerator, denominator): "))
            numbers = verd.split(" ")
            if numbers[0].isdigit() and numbers[1].isdigit() and numbers[2].isdigit():
                return numbers
            else:
                raise TypeError 
        except:
            print("Invalid price!")


def stock_price(fjoldi, tolur):
    deiling = float(tolur[1]) / float(tolur[2])
    saman = float(tolur[0]) + deiling
    heild = saman * fjoldi
    heild = round(heild, 2)
    return heild


svar = "y"
while svar is "y":
    fjoldi = bref()
    tolur = verdid()
    stock = stock_price(fjoldi, tolur)
    print(str(fjoldi) + " shares with market price " + str(tolur[0]) + " " + str(tolur[1]) + "/" + str(tolur[2]) + " have value ${:.2f}".format(float(stock)))
    svar= input("Continue: ")



