first_name = '   liane'
last_name = 'Levy    '
message = ' is adorable  '
full_name = f'{first_name.strip()} {last_name.strip()}'
full_name = full_name.title()

final_message = f"{full_name} {message.strip()}"

print(final_message)