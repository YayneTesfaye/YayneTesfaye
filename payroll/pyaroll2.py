print("Payroll Report")
user = input("Enter Employee Name: ")
end = "0"

employees = []
while len(employees) <= 10:
    Hours_worked = float(input("Enter Numbers of Hours worked: "))
    Pay_Rate = float(input("Enter pay Rate: $"))
    if Hours_worked < 40:
        GrossPay = round(Pay_Rate * Hours_worked, 2)
        FedTax = round(0.1 * GrossPay, 2)
        StateTax = round(0.06 * GrossPay, 2)
        Fica = round(0.03 * GrossPay,2)
        print("Employee Name: ", user)
        print("Gross Pay: $", GrossPay)
        print("Federal Tax: $", FedTax)
        print("State Tax: $", StateTax)
        print("Fica:",Fica)
    else:
        RegularPay = Pay_Rate * 40
        OverTime = Hours_worked - 40
        OverTimeRate = Pay_Rate * 1.5
        OverTimePay = round(OverTimeRate * OverTime, 2)
        GrossPay = round(RegularPay + OverTimePay, 2)
        FedTax = round(0.1 * GrossPay, 2)
        StateTax = round(0.06 * GrossPay, 2)
        Fica = round(0.03 * GrossPay, 2)
        print("Employee Name: ", employees)
        print("Gross Pay: $", GrossPay)
        print("(Overtime pay: $", OverTimePay, ")")
        print("Federal Tax: $", FedTax)
        print("State Tax: $", StateTax)
        print("Fica:", Fica)
    user = input(">>>>>>>>>>>>>>>>>>" "Enter Next Employee or type '0' to Exit: ")
else:
    print("Exiting program....")