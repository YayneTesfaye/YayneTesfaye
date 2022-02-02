
employee = 1

while employee < 11:
    overtime = 0
    Employee_name = input("***************************" f"\nEnter Employee {employee}'s Name: ")
    Pay_Rate = float(input("Enter Pay Rate: $"))
    Hours_worked = float(input("Enter Hours: "))

    regular_pay = Hours_worked * Pay_Rate

    if Hours_worked > 40:
        overtime = (Hours_worked - 40) * (1.5 * Pay_Rate)
        gross_pay = regular_pay + overtime
    else:
        gross_pay = regular_pay


    fed_tax = gross_pay * 0.1
    state_tax = gross_pay * 0.06
    fica = gross_pay * 0.03


    net_pay = gross_pay - (fed_tax + state_tax + fica)


    print(
        f"\nEmployee_name ${Employee_name} Hours_worked: {Hours_worked} Pay_Rate: ${Pay_Rate} Regular Pay: ${regular_pay} Overtime Pay: ${overtime}, Gross Pay: ${gross_pay}, Federal Tax: ${fed_tax}, State Tax: ${state_tax}, FICA: ${fica}, Net Pay: ${net_pay} ")

    # next employee turn
    employee += 1