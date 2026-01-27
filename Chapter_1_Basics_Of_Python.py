#String & Multiplication#
print("="*90)
print("\U0001F680 Welcome To Python Chapter 1st:\U0001F680  Basics Of Python \U0001F680 ")
print("Author:Syed Ahmad Ali")
print('''In this cahpter we learn  Python Basics & after Completing this, you will be able to build:
-Simple Calculator
-Marks & Percentage Calculator
-Age Calculator
-Temperature Converter
-Table Generator ''')
print("="*90)
#Comments#
print('''\U0001F31FComments(#)\U0001F31F
Comments are used in a program to explain code. If We put a #before a line, Python will ignore everything after it on that line and will not act it.''')
#String Concentration#
First_Name=input("\nEnter your first name:")
Last_Name=input("\nEnter your last name:")
Full_Name=First_Name +" "+Last_Name
#Unicode & Emojis#
print(f"\n\n\U0001F917Welcome,{Full_Name}!\U0001F917")
#Input & Type Cating(Integer & Float)#
Age=int(input("\n\nEnter Your Age"))
#Basic Math Operation & Our Age Caluculator Is Ready#
Months=Age*12
Days=Months*30
Hours=Days*24
Minutes=Hours*60
Seconds=Minutes*60
print(Age, "\t\tYears")
print(Months,"\t\tMonths")
print(Days,"\t\tDays")
print(Hours,"\t\tHours")
print(Minutes,"\tMinutes")
print(Seconds,"\tSeconds")
print("\n\n\U0001F389Congratulations\U0001F389, You Build Age Calculator Successfully!\U0001F44F")
#Boolean Logic#
Is_Adult=Age>=18
print("\nAdult Status:",bool(Is_Adult))
#Type Checking#
print("\nAge Type:",type(Age))
print("\nName Type:",type(Full_Name))
#Escape Sequence#
print("\nName\tAge\tClass\nAhmad\t15\t12th\nAkram\t15\t11th\nAlia\t17\t14th\nAisha\t16\t10th")
#String Methods & Slicing#
msg="python is powerfull"
print("\nOrginal Message:",msg)
print("\nStripped:",msg.strip())
print("\nUpper:",msg.upper())
print("\nSliced:",msg[0:10])
#Currency Exchange#
#Currency<USD#
PKR=float(input("Enter Your Amount:"))
USD_RATE=float(input("Enter USD RATE:"))
USD=PKR/USD_RATE
print(f"\n{PKR}PKR={USD}USD")
#Currency>USD put this currency rate in usa like kuwaiti dinar rate is 3.26usd #
Kuwaiti_Dinar=float(input("Enter Your Amount:"))
Dollar_rate=float(input("Enter Dollar Rate:"))
USD_Rate=Kuwaiti_Dinar*Dollar_rate
print(f"{Kuwaiti_Dinar}Kuwaiti_Dinar={USD_Rate}USD")
print(f"\U0001F973Congratulations{Full_Name}\U0001F973,You successfully build Currency Converter\U0001F4B2")
#Even Odd Check#
number=int(input("\nEnter a number to check even or odd:"))
print("\nIs Even Number?",number%2==0)
num=int(input("\nEnter a number to check even or odd:"))
print("\nIs Odd Number?",num%2!=0)
#For Loop#
for i in range(10):
    print(i+1,Full_Name)
for i in range(1,20,2):
    print(i,Full_Name)
#Power Operator#
print(2**5)
print(3**7)
#Log Factor#
import math
result_ln=math.log(10)
print(result_ln)
result_log10=math.log10(199)
print(result_log10)
result_log2=math.log(32,2)
print(result_log2)
#Variable re assignment"
#Simple Method#
score=10
score=score+8
print("Updated Score",score)
#Profeshional Style#
Score=int(input("Enter Score:"))
Score=Score+5
print("Updated Score",Score)
#Modern Style & Shortcut#
scoree=int(input("Enter Score:"))
scoree+=9
print("Updated Score",scoree)
#Temperature Converter#
#Celcius#
Celcius=float(input("Enter Temperature In Degree Celcius:"))
Kelvin=round(Celcius+273.15,2)
print(Kelvin,"Kelvin")
Fahrnheit=round((Celcius*9/5)+32,2)
print(Fahrnheit,"Fahrnheit")
#Fahrnheit#
F=float(input("\nEnter Temperature In Fahrnheit:"))
C=round((F-32)*5/9,2)
print(C,"Celcius")
K=round((F-32)*5/9+273.15,2)
print(K,"Kelvin")
#Kelvin#
kelvin=float(input("\nEnter Temperature In Kelvin:"))
celcius=round(kelvin-273.15,2)
print(celcius,"Celcius")
fahrenheit=round((kelvin-273.15)*9/5+32,2)
print(fahrenheit,"Fahrenheit")
print("\n\U0001F321Congratulations\U0001F321, You Build Temperature Converter successfully\U0001F973")
#Bussiness Calculator#
#Profit#
print("\n\nProfit Calculator")
CP=float(input("Enter Cost Price:"))
SP=float(input("Enter Selling Price:"))
Profit=SP-CP
print("\nCost Price:",round(CP,2))
print("Selling Price:",round(SP,2))
print("\nProfit:",round(Profit,2))
#Loss#
print("\n\nLoss Calculator")
cp=float(input("Enter Cost Price:"))
sp=float(input("Enter Selling Price:"))
Loss=cp-sp
print("\nCost Price:",round(cp,2))
print("Selling Price:",round(sp,2))
print("\nLoss:",Loss)
#Discount#
print("\n\nDiscount")
Original_Price=float(input("Enter Original Price:"))
Discount_Rate=float(input("Enter Discount Percentage:"))
Discount_Amount=(Original_Price*Discount_Rate)/100
Result=round(Discount_Amount,2)
print("\nOriginal Price:",round(Original_Price,2))
print("Discount Percentage:",round(Discount_Rate,2))
print("\nDiscount Amount:", Result)
#Zakat#
print("\n\nZakat")
Wealth=float(input("\nEnter Amount:"))
Zakat=Wealth/40
result=round(Zakat,2)
print(result)
#Tax#
print("\n\nTax")
Item_Price=float(input("Enter Itom Price:"))
Tax_Percentage=float(input("Enter Tax Percentage:"))
Tax_Amount=(Item_Price*Tax_Percentage)/100
Total=Item_Price+Tax_Amount
print("\nItem Price:",round(Item_Price,2))
print("Tax Percentage:",round(Tax_Percentage))
print("Tax Amount:",round(Tax_Amount))
print("\nTotal Bill:",round(Total))
print("\n\U0001F973Congratulations\U0001F973, You Build Successfully Bussiness Calculator")
#Percentage Calculator#
Marks=float(input("Enter Marks:"))
Total_Marks=float(input("Enter Total Marks:"))
percentage=(Marks/Total_Marks)*100
print(round(percentage,2),"%")
#Basic Caculation#
#Addition#
print(23+73)
Apple=765
Banana=876
print(Apple+Banana)
print(Apple)
print(Banana)
#Substriction#
print(7725-865)
Patato=782
Tamato=726
print(Patato-Tamato)
print(Patato)
print(Tamato)
#Multiplication#
print(8268*7272)
Grapes=67273
Grass=8737
print(Grapes*Grass)
print(Grass)
print(Grapes)
#Square Factor#
print(3**2)
#Division#
#With point#
print(60/10)
#Without Point#
print(60//10)
#Modulus#
print(61%10)
#Log#
import math
print(math.log(25,5))
#Boolean & Logics#
A=828
print(A<7654)
print(A>78446)
print(A==933)
print(A==828)
print("#"*50)
#Take Marks Of Many Subjectb At Same Time#
print("Enter Marks Of Math English Physics Biology ")
Math,English,Physics,Biology= map(int, input().split()) 
total = Math + English + Physics + Biology
print(f"Total Marks: {total}")
#Professional Table Forming By Using F'String#
print(f"{'Fruit':^10} | {'Price':^10}")
print("-"*23)
print(f"{'Apple':<10} | {'1000':>10}")
print(f"{'Banana':<10} | {'900':>10}")
print(f"{'Grapes':<10} | {'698':>10}")
print(f"{'Orange':<10} | {'654':>10}")
print(f"{'Mango':<10} | {'456':>10}")
#Professional Decimal Formating#
#Shortcut Of Round(value,2)#
PRICE=1000
print(f"Total Bill:{PRICE:.2f}Rupees")
print("\U0001F973Hurrah\U0001F973,CHAPTER 1 ENDED SUSSESSFULLY")
