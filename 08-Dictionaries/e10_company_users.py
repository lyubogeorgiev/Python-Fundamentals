companies = {}

while True:
    user_input = input()
    if user_input == 'End':
        break

    entry = user_input.split(' -> ')

    company_name = entry[0]
    employee_id = entry[1]

    if company_name not in companies.keys():
        companies[company_name] = []

    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company in companies.keys():
    print(company)
    [print(f'-- {current_id}') for (current_id) in companies[company]]
