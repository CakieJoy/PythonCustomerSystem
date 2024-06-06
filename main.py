import csv

customers = [
    
]


while True:
    print("1.Müşteri ekle")
    print("2.Müşterileri yönet")
    menu = int(input("Lütfen seçin :"))

    if menu == 1:
        name = input("Please enter customer name : ")
        print("Saved : ",name)
        email = input("Please enter customer E-Mail : ")
        print("Saved : ",email)
        phone = int(input("Please enter customer Phone Number : "))

        with open('database/customer.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, phone])
            writer.writerows(customers)
    if menu == 2:
        with open('database/customer.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)