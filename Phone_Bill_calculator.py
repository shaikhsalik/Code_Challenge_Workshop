import csv
from datetime import datetime
CSV_FILEPATH =r"C:\Users\135982\01_Repositories\Code_Challenge\generated_sample.csv"
STD_RATE=1
BONUS_RATE=0.2
RATE_OUTSIDE_INTERVAL=0.5 #From 1600 hrs to 800

def Calculate(CSV_FILEPATH):
    Total_bill_list=[]
    BillingData=read_csv_file(CSV_FILEPATH)
    Billtime_list=get_billing_time(BillingData)
    for i in range(len(Billtime_list)):
        if Billtime_list[i].seconds <= 600:
            Bill= (Billtime_list[i].seconds/60) * STD_RATE
        elif Billtime_list[i].seconds >600:
            additional_time=Billtime_list[i].seconds-600
            Bill= 5 +(additional_time/60) * BONUS_RATE
        Total_bill_list.append(Bill)
    Overall_Bill=sum(Total_bill_list)
    return print(Overall_Bill)


def get_billing_time(BillingData):
    Billtime=[]
    time_format="%m/%d/%Y %H:%M"
    for i in range(len(BillingData)):
        Start_time= datetime.strptime(BillingData[i][1],time_format)
        End_time= datetime.strptime(BillingData[i][2], time_format)
        timetobill=End_time-Start_time
        # print(Start_time.hour)
        if Start_time.hour >16 or Start_time.hour <8:
            Billtime.append(timetobill/2)
        else:
            Billtime.append(timetobill)
    return(Billtime)

# def 
def read_csv_file(CSV_FILEPATH):
    # opening the CSV file
    with open(CSV_FILEPATH, mode ='r')as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        allCsvData=list(csvFile)
    return allCsvData

Calculate(CSV_FILEPATH)