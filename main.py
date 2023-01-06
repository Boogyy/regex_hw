import re
import csv

with open("regex.csv", encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=",")
    info_list = list(reader)

result = []
headers = info_list.pop(0)
quantity = len(info_list)
for iterator in range(quantity):
    item = info_list[iterator]
    organization = []
    position = []
    phone = []
    email = []
    lastname = item[0].split()
    firstname = item[1].split()
    surname = item[2].split()
    organization_item = item[3]
    organization.append(organization_item)
    position_item = item[4]
    position.append(position_item)
    num = item[5]
    phone.append(num)
    mail = item[6]
    email.append(mail)
    if len(lastname) != 1:
        firstname.append(lastname.pop(1))
        if len(lastname) != 1:
            surname.append(lastname.pop(1))
        elif len(firstname) != 1:
            surname.append(firstname.pop(1))
        else:
            surname.append('')
    else:
        if len(firstname) != 1:
            surname.append(firstname.pop(1))
    li = lastname + firstname + surname + organization + position + phone + email
    result.append(li)

pattern = r"(\+7|8)\s*\(*(\d{1,3})[)-]*\s*(\d{1,3})\-*(\d{1,2})\-*(\d+)(\s*)\(*([доб.]*)\.?\s*(\d+)*\)*"
substitution = r'+7(\2)\3-\4-\5\6\7\8'
for i in result:
    i[5] = re.sub(pattern, substitution, i[5])

count = 1
users_list = result
for user in result:
    for item_compare in users_list[count:]:
        if user[0] == item_compare[0] and user[1] == item_compare[1]:
            if user[2] == '':
                user[2] = item_compare[2]
            if user[3] == '':
                user[3] = item_compare[3]
            if user[4] == '':
                user[4] = item_compare[4]
            if user[5] == '':
                user[5] = item_compare[5]
            if user[6] == '':
                user[6] = item_compare[6]
            result.remove(item_compare)
    count += 1

with open("users.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerow(headers)
    datawriter.writerows(result)
