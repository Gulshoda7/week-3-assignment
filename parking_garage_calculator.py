print(f'\n=== Parking Garage Calculator ===')
print(f'Enter day type: weekday, weekend, or holiday')
print(f'Type `done` when finished entering hours')

total = 0
discount = 0
price = 0
while True:
    day_type = input(f'\nEnter day type for 1 hour: ').lower()
    if day_type == 'done':
        break
    elif day_type == 'weekday':
        price = 8
    elif day_type == 'weekend':
        price = 6
    elif day_type == 'holiday':
        price = 5
    else:
        print(f'Invalid Day Type!')
        continue
    
    total += price
    print(f'Price: ${price:.2f}')
    print(f'Current total: ${total:.2f}')

print(f'=== Parking Summary ===')
print(f'Subtotal: ${total:.2f}')
if total >= 50:
    print(f'Frequent Parker Discount: -$7.00')
    final_total = total - 7
    print(f'Final Total: ${final_total:.2f}')
else:
    print(f'Frequent Parker Discount: $0.00')
    print(f'Final Total: ${total:.2f}')
print(f'Thank you for parking with us!😊')
