from constants import CLIENT_USERNAME, CLIENT_PASSWORD, C_KEY, SS_ID
from kerberos import authentication_server, ticket_granting_server, service_server
from des import decrypt_des, encrypt_des
from output import yellow, dict_to_str


def client(client_data: dict) -> None:
    # sending package to AS
    print(yellow('Client: Sending to the Authentication Server with: '))
    print(dict_to_str(client_data) + '\n')

    package = authentication_server(client_data)

    # receiving package from AS
    tgt = package['TICKET'] = decrypt_des(package['TICKET'], C_KEY)
    c_tgs_key = package['KEY'] = decrypt_des(package['KEY'], C_KEY)

    print(yellow('Client: Receiving from the Authentication Server with: '))
    print(dict_to_str(package) + '\n')

    # forming package to TGS
    aut = {
        'c': client_data['username'] + ' ' + client_data['password'],
        't2': '0'
    }
    package = {
        'TICKET': tgt,
        'KEY': c_tgs_key,
        'AUT': encrypt_des(aut, c_tgs_key),
        'ID': SS_ID
    }

    # sending package to TGS
    print(yellow('Client: Sending to the Ticket Granting Server with: '))
    print(dict_to_str(package) + '\n')

    package = ticket_granting_server(package)

    # receiving package from TGS
    tgs = package['TICKET'] = decrypt_des(package['TICKET'],  c_tgs_key)
    c_ss_key = package['KEY'] = decrypt_des(package['KEY'], c_tgs_key)

    print(yellow('Client: Receiving from the Ticket Granting Server with: '))
    print(dict_to_str(package) + '\n')

    # forming package to SS
    aut = {
        'c': client_data['username'] + ' ' + client_data['password'],
        't4': '1'
    }
    package = {
        'TICKET': tgs,
        'KEY': c_ss_key,
        'AUT': encrypt_des(aut, c_ss_key)
    }

    # sending package to TGS
    print(yellow('Client: Sending to the Service Server with: '))
    print(dict_to_str(package) + '\n')

    package = service_server(package)

    # receiving package from SS
    t4 = package['t4'] = decrypt_des(package['t4'], c_ss_key)

    print(yellow('Client: Receiving from the Service Server with: '))
    print(dict_to_str(package) + '\n')

    # checking SS validation
    if int(aut['t4']) + 1 != int(t4):
        raise Exception(yellow('Client: Invalid Service Server!'))


if __name__ == '__main__':
    client_data = {
        'username': CLIENT_USERNAME,
        'password': CLIENT_PASSWORD
    }

    client(client_data)

    print('All actions have been successfully reproduced!\n')
