"""
Debug an ISBN Validator
The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits.

Tests:
1. You should comment out the call to the main function to allow for the rest of the tests to work properly.
2. You should have a validate_isbn function.
3. You should have a calculate_check_digit_10 function.
4. You should have a calculate_check_digit_13 function.
5. You should have a main function.
6. When the user inputs a value that is not a comma separated value, you should see the message Enter comma-separated values. in the console.
7. When the user inputs a non-numeric value for the length, you should see the message Length must be a number. in the console.
8. When the user enters an incorrect ISBN code with characters other than numbers, you should see the message Invalid character was found. in the console.
9. When the user enters 1530051126,10, you should see the message Valid ISBN Code. in the console.
10. When the user enters 9781530051120,13, you should see the message Valid ISBN Code.
11. When the user enters 1530051125,10, you should see the message Invalid ISBN Code..
12. When the user enters 9781530051120,10, you should see the message ISBN-10 code should be 10 digits long.
13. When the user enters 1530051126,13, you should see the message ISBN-13 code should be 13 digits long.
14. When the user enters 15-0051126,10, you should see the message Invalid character was found.
15. When the user enters 1530051126,9, you should see the message Length should be 10 or 13.
16. When the user enters 1530051125,A, you should see the message Length must be a number.
17. When the user enters 1530051125, you should see the message Enter comma-separated values.
18. When the user enters 9971502100,10, you should see the message Valid ISBN Code.
19. When the user enters 080442957X,10, you should see the message Valid ISBN Code.
20. When the user enters 9781947172104,13, you should see the message Valid ISBN Code.
"""




def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    try:
        main_digits = isbn[0:length-1]
        given_check_digit = isbn[length-1]
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return
    
    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 9 digits by its corresponding weight (10 to 2) and sum up the results
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    # Find the remainder of dividing the sum by 11, then subtract it from 11
    result = 11 - digits_sum % 11
    # The calculation result can range from 1 to 11.
    # If the result is 11, use 0.
    # If the result is 10, use upper case X.
    # Use the value as it is for other numbers.
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    # Note: You don't have to fully understand the logic in this function.
    digits_sum = 0
    # Multiply each of the first 12 digits by 1 and 3 alternately (starting with 1), and sum up the results
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    # Find the remainder of dividing the sum by 10, then subtract it from 10
    result = 10 - digits_sum % 10
    # The calculation result can range from 1 to 10.
    # If the result is 10, use 0.
    # Use the value as it is for other numbers.
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    try:
        user_input = input('Enter ISBN and length: ')
        values = user_input.split(',')
        
        if len(values) != 2:
            print('Enter comma-separated values.')
            return
        
        isbn = values[0]
        
        try:
            length = int(values[1])
        except ValueError:
            print('Length must be a number.')
            return
        
        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
            
    except IndexError:
        print('Enter comma-separated values.')

# Commenté l'appel à main() pour les tests
# main()