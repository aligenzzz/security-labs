from constants import DATABASE, C_KEY, AS_TGS_KEY, C_TGS_KEY, TGS_ID, C_SS_KEY, \
                      TGS_SS_KEY, CURRENT, PERIOD
from des import encrypt_des, decrypt_des
from output import red, blue, green, dict_to_str


def authentication_server(client_data: dict) -> dict:
    # checking the presence of a user in the database
    if client_data['username'] not in DATABASE:
        raise Exception(red('AS: There is no user with that name!'))
    elif client_data['password'] != DATABASE[client_data['username']]:
        raise Exception(red('AS: Invalid password!'))
    
    # forming package to Client
    ticket_granting_ticket = {
        'c': client_data['username'] + ' ' + client_data['password'],
        'tgs': TGS_ID,
        't1': '0',
        'p1': PERIOD
    }
    package = {
        'TICKET': encrypt_des(encrypt_des(ticket_granting_ticket, AS_TGS_KEY), C_KEY), 
        'KEY': encrypt_des(C_TGS_KEY, C_KEY)
    }
    
    print(red('AS: Sending to the Client with: '))
    print(dict_to_str(package) + '\n')
    
    return package
    

def ticket_granting_server(package: dict) -> dict:
    # receiving package from Client
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], AS_TGS_KEY)
    aut = package['AUT'] = decrypt_des(package['AUT'], package['KEY'])

    print(blue('TGS: Receiving from the Client with: '))
    print(dict_to_str(package) + '\n')

    # checking for the labels
    if aut['c'] != tgt['c'] or aut['t2'] != tgt['t1']:
        raise Exception(blue('TGS: Invalid AUT block!'))
    # checking for time expiration
    if int(tgt['t1']) + int(tgt['p1']) < int(CURRENT):
        raise Exception(blue('TGS: Session time is up!'))

    # forming package to Client
    ticket_granting_service = {
        'c': tgt['c'],
        'ss': package['ID'],
        't3': '1',
        'p2': PERIOD
    }
    package = {
        'TICKET': encrypt_des(encrypt_des(ticket_granting_service, TGS_SS_KEY), C_TGS_KEY), 
        'KEY': encrypt_des(C_SS_KEY, C_TGS_KEY)
    }

    print(blue('TGS: Sending to the Client with: '))
    print(dict_to_str(package) + '\n')
    
    return package


def service_server(package: dict) -> dict:
    # receiving package from Client
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], TGS_SS_KEY)
    aut = package['AUT'] = decrypt_des(package['AUT'], package['KEY'])

    print(green('SS: Receiving from the Client with: '))
    print(dict_to_str(package) + '\n')

    # checking for the labels
    if aut['c'] != tgt['c'] or aut['t4'] != tgt['t3']:
        raise Exception(green('SS: Invalid AUT block!'))
    # checking for time expiration
    if int(tgt['t3']) + int(tgt['p2']) < int(CURRENT):
        raise Exception(green('SS: Session time is up!'))

    # forming package to Client
    modified_aut = {
        't4': encrypt_des(str(int(aut['t4']) + 1), package['KEY'])
    }

    print(green('SS: Sending to the Client with: '))
    print(dict_to_str(modified_aut) + '\n')
    
    return modified_aut