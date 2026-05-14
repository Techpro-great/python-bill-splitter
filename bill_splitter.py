import time as t
print("Welcome to Bill Splitter.")
menu = '''1. Calculate
2. Exit'''
t.sleep(1)
while True:
    print(menu)
    cmd = input("Please enter the co-responding number >>> ")
    if cmd == '1':
        total_bill = float(input("Please enter the total bill >>> "))
        tip_percentage = input("Please enter the tip percentage >>> ")
        clean_tip = float(tip_percentage.replace("%", ""))
        number_of_people = int(input("How many people are you? >>> "))
        tip_ammount = clean_tip/100 * total_bill
        final_bill = total_bill + tip_ammount
        bill_per_person = round(final_bill / number_of_people, 2)
        print(f"Each person has to pay Rs {bill_per_person:.2f}")
        t.sleep(1)
    elif cmd == '2':
        print("Thanks for using.")
        break
    else:
        print("Invalid.")
