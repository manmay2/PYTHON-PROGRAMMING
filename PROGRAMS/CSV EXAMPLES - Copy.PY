#wap that will accept records of 5 students from the user and write that records in the stu.csv file
import csv
with open("stu.csv","w") as f1:
    f=csv.writer(f1)
    f.writerow(["Roll_No","Name","Marks"])
    for i in range(1,6):
        print("Enter record no.",i)
        r=int(input("Enter the Roll No. of the student: "))
        n=input("Enter the Name of the student: ")
        m=float(input("Enter the marks of the student: "))
        f.writerow([r,n,m])
    
#Using the function of writerows()
with open("result.csv","w") as f:
    wr=csv.writer(f)
    wr.writerows(
        [
            ["Name","Points","Rank"],
            ["Shradha","4500","23"],
            ["Nischay","4800","31"],
            ["Ali","4500","25"],
            ["Adi","5100","14"]
        ]
    )


#trying the delimiter .
with open("delimiter.csv","w") as f3:
    deli=csv.writer(f3,delimeter="||")
    deli.writerow(["Name","Points","Rank"])


#display the file result.csv with brackets.
with open("result.csv","r") as f4:
    t=csv.reader(f4)
    for i in t:
        print(i)

#display the file result.csv without printing brackets.
with open("result.csv","r", newline="\r\n") as f4:
    t=csv.reader(f4)
    for i in t:
        print(i)


