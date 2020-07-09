# This project converts kilometers into miles
# 07-08-2020
# CTI-110 P5T1_KilometerConverter
# Sinclair Robinson



# The main function gets a distance in kilometers and calls
# The show_miles function to  convert it.
def main():
    #Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    #Display the distance converted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the result.
def show_miles (km):
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    #Display the miles.
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function.
main()
