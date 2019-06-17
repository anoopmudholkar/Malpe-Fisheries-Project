import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fisherdf = pd.read_excel('survey - USSD among FIsher women - final.xlsx')

#types of phones used
phtype = fisherdf['Phone Type'].value_counts()
print(phtype)
smartphone = phtype[1]
featured = phtype[2]
no = phtype[3]
phones = [smartphone,featured,no]
labels = 'smartphone','featured','no'
plt.title('Types of phones used by the fishermen')
plt.pie(phones,labels=labels,shadow=True)
plt.axis('equal')
plt.show()


#1. education with heard about USSD
edu = fisherdf['Education'].value_counts()
zero1 = edu[0]
first1 = edu[1]
second1 = edu[2]
third1 = edu[3]
fourth1 = edu[4]
fifth1 = edu[5]
sixth1 = edu[6]
seventh1 = edu[7]
eighth1 = edu[8]
ninth1 = edu[9]
tenth1 = edu[10]
twelve1 = edu[12]
hauyes = fisherdf[fisherdf['Heard about USSD'] == 1]
hauedu = hauyes['Education'].value_counts()
zero = hauedu[0]
first = hauedu[1]
second = hauedu[2]
third = hauedu[3]
fourth = hauedu[4]
fifth = hauedu[5]
sixth = hauedu[6]
seventh = hauedu[7]
eighth = hauedu[8]
ninth = hauedu[9]
tenth = hauedu[10]
twelve = hauedu[12]
prob1 = zero/zero1
prob2 = first/first1
prob3 = second/second1
prob4 = third/third1
prob5 = fourth/fourth1
prob6 = fifth/fifth1
prob7 = sixth/sixth1
prob8 = seventh/seventh1
prob9 = eighth/eighth1
prob10 = ninth/ninth1
prob11 = tenth/tenth1
prob12 = twelve/twelve1
y = [prob1,prob2,prob3,prob4,prob5,prob6,prob7,prob8,prob9,prob10,prob11,prob12]
n = len(y)
x = range(n)
width = 0.5
plt.xticks(x, ('no education','class 2','class 3','class 4','class 5','class 6','class 7','class 8','class 9','class 10','class 12'))
plt.xlabel('Education')
plt.ylabel('Heard about ussd')
plt.title('Education with heard about ussd')
plt.bar(x,y,width)
plt.show()


#education with willingness to use mobile banking
edu = fisherdf['Education'].value_counts()
zero1 = edu[0]
first1 = edu[1]
second1 = edu[2]
third1 = edu[3]
fourth1 = edu[4]
fifth1 = edu[5]
sixth1 = edu[6]
seventh1 = edu[7]
eighth1 = edu[8]
ninth1 = edu[9]
tenth1 = edu[10]
twelve1 = edu[12]
willing = fisherdf[fisherdf['Willingness to use Mobile Banking'] == 1]
willingyes = willing['Education'].value_counts()
zero2 = willingyes[0]
second2 = willingyes[2]
third2 = willingyes[3]
fourth2 = willingyes[4]
fifth2 = willingyes[5]
sixth2 = willingyes[6]
seventh2 = willingyes[7]
eighth2 = willingyes[8]
ninth2 = willingyes[9]
tenth2 = willingyes[10]
twelve2 = willingyes[12]
prob11 = zero2/zero1
prob33 = second2/second1
prob44 = third2/third1
prob55 = fourth2/fourth1
prob66 = fifth2/fifth1
prob77 = sixth2/sixth1
prob88 = seventh2/seventh1
prob99 = eighth2/eighth1
prob100 = ninth2/ninth1
prob111 = tenth2/tenth1
prob122 = twelve2/twelve1
yax = [prob11,prob33,prob44,prob55,prob66,prob77,prob88,prob99,prob100,prob111,prob122]
num = len(yax)
xax = range(num)
width = 0.5
plt.xticks(xax, ('no education','class 2','class 3','class 4','class 5','class 6','class 7','class 8','class 9','class 10','class 12'))
plt.xlabel('Education')
plt.ylabel('Willingness to use mobile banking')
plt.title('Education with willingness to use mobile banking')
plt.bar(xax,yax,width)
plt.show()


#income with request for digital payment
total = fisherdf['Average Per day sales'].value_counts()
digpay = fisherdf[fisherdf['Customer request for digital payment'] == 1]
digincome = digpay['Average Per day sales']
countdiginc = digincome.value_counts()
prob = countdiginc/total
plt.xlabel('Income range')
plt.ylabel('Customer request for digital payment')
plt.title('Income with request for Digital payment')
prob.plot(kind='bar')
plt.show()

#average per day sales for each market
kodibengre = fisherdf[fisherdf['Market Place'] == 1]
sales1 = kodibengre['Average Per day sales'].sum()
#print(sales1)
malpe = fisherdf[fisherdf['Market Place'] == 2]
sales2 = malpe['Average Per day sales'].sum()
#print(sales2)
udupi = fisherdf[fisherdf['Market Place'] == 3]
sales3 = udupi['Average Per day sales'].sum()
#print(sales3)
shirva = fisherdf[fisherdf['Market Place'] == 4]
sales4 = shirva['Average Per day sales'].sum()
#print(sales4)
parkala = fisherdf[fisherdf['Market Place'] == 5]
sales5 = parkala['Average Per day sales'].sum()
#print(sales5)
kalyanpura = fisherdf[fisherdf['Market Place'] == 6]
sales6 = kalyanpura['Average Per day sales'].sum()
#print(sales6)
bramavara = fisherdf[fisherdf['Market Place'] == 7]
sales7 = bramavara['Average Per day sales'].sum()
#print(sales7)
uchila = fisherdf[fisherdf['Market Place'] == 8]
sales8 = uchila['Average Per day sales'].sum()
#print(sales8)
kaup = fisherdf[fisherdf['Market Place'] == 9]
sales9 = kaup['Average Per day sales'].sum()
#print(sales9)
indrali = fisherdf[fisherdf['Market Place'] == 10]
sales10 = indrali['Average Per day sales'].sum()
#print(sales10)
padubidri = fisherdf[fisherdf['Market Place'] == 11]
sales11 = padubidri['Average Per day sales'].sum()
#print(sales11)
mulki = fisherdf[fisherdf['Market Place'] == 12]
sales12 = mulki['Average Per day sales'].sum()
#print(sales12)
suratkal = fisherdf[fisherdf['Market Place'] == 13]
sales13 = suratkal['Average Per day sales'].sum()
#print(sales13)
statebankfishmarket = fisherdf[fisherdf['Market Place'] == 14]
sales14 = statebankfishmarket['Average Per day sales'].sum()
#print(sales14)
urwa = fisherdf[fisherdf['Market Place'] == 15]
sales15 = urwa['Average Per day sales'].sum()
#print(sales15)
bejai = fisherdf[fisherdf['Market Place'] == 16]
sales16 = bejai['Average Per day sales'].sum()
#print(sales16)
kavoor = fisherdf[fisherdf['Market Place'] == 17]
sales17 = kavoor['Average Per day sales'].sum()
#print(sales17)
kankanadi = fisherdf[fisherdf['Market Place'] == 18]
sales18 = kankanadi['Average Per day sales'].sum()
#print(sales18)
karwar = fisherdf[fisherdf['Market Place'] == 19]
sales19 = karwar['Average Per day sales'].sum()
#print(sales19)
honnavar = fisherdf[fisherdf['Market Place'] == 20]
sales20 = honnavar['Average Per day sales'].sum()
#print(sales20)
bhatkal = fisherdf[fisherdf['Market Place'] == 21]
sales21 = bhatkal['Average Per day sales'].sum()
#print(sales21)
murdeshwar = fisherdf[fisherdf['Market Place'] == 22]
sales22 = murdeshwar['Average Per day sales'].sum()
#print(sales22)
kumta = fisherdf[fisherdf['Market Place'] == 23]
sales23 = kumta['Average Per day sales'].sum()
#print(sales23)
ankola = fisherdf[fisherdf['Market Place'] == 24]
sales24 = ankola['Average Per day sales'].sum()
#print(sales24)
kundapura = fisherdf[fisherdf['Market Place'] == 25]
sales25 = kundapura['Average Per day sales'].sum()
#print(sales25)
sastan = fisherdf[fisherdf['Market Place'] == 26]
sales26 = sastan['Average Per day sales'].sum()
#print(sales26)
numberofmarkets = 26
xvalues = np.arange(numberofmarkets)
yvalues = (sales1,sales2,sales3,sales4,sales5,sales6,sales7,sales8,sales9,sales10,sales11,sales12,sales13,sales14,sales15,sales16,sales17,sales18,sales19,sales20,sales21,sales22,sales23,sales24,sales25,sales26)
fig, ax = plt.subplots()
width = 0.3
opacity = 0.8
plt.xticks(xvalues, ('kodibengre','malpe','udupi','shirva','parkala','kalyanpura','bramavara','uchila','kaup','indrali','padubidri','mulki','suratkal','statebank fish market','urwa','bejai','kavoor','kankanadi','karwar','honnavar','bhatkal','murdeshwar','kumta','ankola','kundapura','sastan'),rotation = 'vertical')
plt.xlabel('Market Places')
plt.ylabel('Average sales per day')
plt.title('total sales in each market')
barchart = plt.bar(xvalues, yvalues, width, alpha=opacity, align='center')
plt.tight_layout()
plt.show()

#popular bank among fisherman
banktype = fisherdf['Bank Name'].value_counts()
Noacc = banktype[0]
Canara = banktype[1]
cooperative = banktype[2]
corporation = banktype[3]
mahalaxmi = banktype[4]
syndicate = banktype[5]
vijaya = banktype[6]
na = banktype[7]
urban = banktype[8]
karnataka = banktype[9]
postoffice = banktype[10]
bom = banktype[11]
labels ='No account','Canara Bank','Cooperative Bank','Corporation Bank','Mahalaxmi Bank','Syndicate Bank','Vijaya Bank','n/a','Urban bank','Karnataka Bank','Post office','Bank of Mysore'
sizes = [Noacc,Canara,cooperative,corporation,mahalaxmi,syndicate,vijaya,na,urban,karnataka,postoffice,bom]
plt.title('Popular banks among fishermen')
plt.pie(sizes,labels=labels,shadow=True)
plt.axis('equal')
plt.show()


#does age matter for willingness
aboveforty = fisherdf[fisherdf['age'] > 40]
willingness = aboveforty['Willingness to use Mobile Banking'].value_counts()
willingnessyes = willingness[1]
totalabove40 = willingness[0] + willingness[1]
probabove40 = willingnessyes/totalabove40
belowforty = fisherdf[fisherdf['age'] < 40]
willingness1 = belowforty['Willingness to use Mobile Banking'].value_counts()
willingnessyes1 = willingness1[1]
totalbelow40 = willingness1[0] + willingness1[1]
probbelow40 = willingnessyes1/totalbelow40
print(probbelow40)
print(probabove40)
agefactor = [probbelow40,probabove40]
labels = 'below 40','above 40'
plt.title('Age with willingness to use mobile banking')
plt.pie(agefactor,labels=labels,shadow=True)
plt.axis('equal')
plt.show()
