#Q03
#party list number
print('****WElCOME****')
partyList = []
# maxlenlist = 3
number_of_inviters = int(input('Add number of inviters you want to invite: '))
if number_of_inviters <10:
    for n in range(number_of_inviters):
        invitedList = input('Please enter the names you want to invite them to party^^: ')
        partyList.append(invitedList)
        print('name has been added {}'.format(invitedList))
    print('Your inviters List is', partyList)
    choice = input('Do you want to enter more! yes/no: ')
    if choice == 'yes':
        for n in range(number_of_inviters):
            invitedList = input('Please enter the names you want to invite them to party^^: ')
            partyList.append(invitedList)
            print('name has been added {}'.format(invitedList))
        print('Your inviters List is', partyList)
        choice = input('Do you want to enter more! yes/no: ')
    elif choice == 'no':
        print('here is your number of names in invited list',len(partyList),'and they are',partyList)
else :
    print('too many people')