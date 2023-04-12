def value(enter):
    while True:
        try:
            value = float(input(enter))
            if value <= 0:
                print("Invalid!!, Please Enter again")
            else:
                return value
        except ValueError:
            print("Invalid!!, Please Enter again")
def data():
    start_number = value("Starting number of organisms: ")
    increment_daily = value("Average daily percentage increase: ")
    days = int(value("Enter the number of days to display the final data: "))
    print('Day Approximate'+' '*10+'Population')
    print('-----------------------------------')
    print("1",' '*22, start_number)
    for day in range(2, days+1):
        start_number += start_number * (increment_daily/100)
        print("{}".format(day),' '*22, start_number)
data()





