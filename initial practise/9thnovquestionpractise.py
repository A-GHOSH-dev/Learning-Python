






return_date=int(input('Enter date of return given by librarian: '))
number_of_month_return_late=int(input('Enter number of months after the return date month when the student returns the book:'))
while number_of_month_return_late==0:
    number_of_days_late=int(input('Enter number of days af days after the return date when the student returns book: '))
    if number_of_days_late==0:
        print('No fine charged. Fine is 0')
        break
    else:
        month=int(input('Enter number of days in that month in which boy needed to return book: '))
        if (number_of_days_late+return_date)<=month:
            Fine=15*number_of_days_late
            print('Fine= ',Fine)
            break
while number_of_month_return_late>0: 
        number_of_months_left_in_that_year=int(input('Enter number of months left in that year excluding the month in which the return date of the book is: '))
        if number_of_month_return_late<=number_of_months_left_in_that_year:
            Fine=500*number_of_month_return_late
            print('Fine= ',Fine)
            break
        elif number_of_month_return_late>number_of_months_left_in_that_year:
            Fine=10000
            print('Fine= ',Fine)
            break









'''return_date_given=int(input('Enter date of return given by librarian: '))
return_month_given=str(input('Enter month of return given by librarian: '))
month=int(input('Enter number of days in that month in which boy needed to return book: '))
return_date_actually=int(input('Enter date of submission: '))
return_month_actually=str(input('Enter month of submission: '))
if return_date_actually==return_date_given and return_month_actually==return_month_given:
    print('No fine charged. Fine is 0')
elif return_date_given<return_date_actually<=month and return_month_actually==return_month_given:
    Fine=15*(return_date_actually-return_date_given)
    print('Fine= ',Fine)
elif return_month_actually!=return_month_given:
    number_of_month_return_late=int(input('Enter number of months after the return date month when the student returns the book:'))
    number_of_months_left_in_that_year=int(input('Enter number of months left in that year excluding the month in which the return date of the book is: '))
    if number_of_month_return_late<=number_of_months_left_in_that_year:
        Fine=500*number_of_month_return_late
        print('Fine= ',Fine)
    elif number_of_month_return_late>number_of_months_left_in_that_year:
        Fine=10000
        print('Fine= ',Fine)'''
    
        
        
    





