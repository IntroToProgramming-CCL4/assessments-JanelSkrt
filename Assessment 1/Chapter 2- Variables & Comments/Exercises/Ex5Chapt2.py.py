budget = 50
usb_stick_price = 6
num_usb_sticks = budget // usb_stick_price
leftover_pounds = budget % usb_stick_price
print(f"She can buy {num_usb_sticks} USB sticks.")
print(f"She will have {leftover_pounds} pounds left.")