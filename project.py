contacts = {
    "Ashutosh Purushotam": 9381520954, "Ishan Garg": 9568623576, "Mohammad Suhaib Wani": 7006703701,
    "Riyajeet Singh": 9103182131, "Jayesh Kumar": 7654507963, "Shubam Kumar": 6299410557, "Kundan Kumar": 9634217890,
    "Abhay": 892380890, "Sahil Kumar": 7488187309, "Ayushman Joshi": 7535025802, "Ashirbad": 7077656922,
    "Yogesh": 8440842169, "Himansu Kumar Panda": 7326869234, "Pratikshya Rout": 6239370615, "Anmol Chauhan": 8630502611,
    "Ujjwal": 8569804781, "Bhavishya Yadav": 7073927307, "Gaurav Rajput": 7500125655, "Vivek Vardhan Reddy": 761954876,
    "Yagna Madhav ": 9392212260, "Aryus Kumar": 9115883308, "Harsh Jaiswal": 8889303719, "Tarun Garg": 7247818133,
    "Harsh Gupta": 9149045570, "kshitij Singh": 9876023290, "Ashish CHauhan": 63070556091, "Durgesh Kumar": 9696754672,
    "Utsav": 7061221822, "Sudharsan": 9342771181, "Kashyap Yadav": 9381444789, "Tanbir Ahmed": 9749420008,
    "Saurav": 8307209328, "Rushikesh": 9676079128, "Neelesh": 8897123757, "Kabir": 8847453863, "Rohit": 9356774688,
    "Nikhil": 9381520954, "Aditya": 7658864572, "Naman Pratap": 8210246045, "Sadique Mobarak Azmi": 7488863584,
    "Adiya Raj": 6207937383, "Debasis Sahu": 7855032278, "Arhiant Jain": 9509776730, "Tushar Karn": 8797001407,
    "Aashtuosh Kumar": 8340348272, "Bhuvan Chandu": 9032405135, "Yash Kumar": 9693344052, "Umang Singh": 8127239465,
    "Harsh Vardhan Singh": 9555489012, "Sardhar": 7044464449, "Ankita": 8091334631, "Rishi Raj": 8210021610,
    "Hemant Sharma": 9835857838, "Vedang Jangam": 8010959168, "Rishab Raj": 9122114280, "Pratap Singh": 8777786370,
    "Shobhit Pathak": 8736848222, "Rajan Patel": 9316524007, "Bhavan Sadhu": 8919334866

}


# Searches the dictionary and prints the key value pair incase the key isn't present, it prints "no such contact found"

def single_search():
    name = input(">>>Enter the name of the student whose contact is needed: ").title()
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        print("\nNo such contact found")



# Searches the dictionary and prints multiple key value pair and incase any key isn't present,it shows error

def multiple_search():
    result = {}
    s1 = []
    a = 0
    name1 = input(">>>Enter the names of the contacts separated by commas: ").split(",")
    for i in name1:
        i = i.title()
        if i in contacts:
            result[i] = contacts[i]
        else:
            s1.append(i)
            a += 1
    if a > 0:
        print(f"\nCouldn't find contacts {s1}  ")


    else:

        print(result)


choice = int(input(
    "Would you like to: \n\n1. Search for a single contact👤 \n2. List all the contacts📜 \n3. Search for multiple contacts👥 \n\n \n>>>Enter your choice: "))

if choice == 1:
    single_search()

elif choice == 2:

    print(contacts)

elif choice == 3:
    multiple_search()

else:
    print("Choose from the given options!")
