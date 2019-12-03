#Regex validate PIN code
#Level: 7 kyu
'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
'''
def validate_pin(pin):
    return True if (len(pin) == 4 or len(pin) == 6)and pin.isdigit() else False
