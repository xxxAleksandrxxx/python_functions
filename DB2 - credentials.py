def db2_creds(cred : dict = dict()) -> dict:
    '''
    Function: db2_creds
    
    Description: Extracts IBM DB2 credentials from a provided dictionary.
    
    Parameters:
    - cred (dict): Dictionary containing credential information.
    
    Returns:
    - cred_dict (dict): Dictionary containing extracted DB2 credentials.
    '''

    cred_dict = dict()
    if not cred:
        print('\nERROR: No data provided.\n')
        return cred_dict
    if type(cred) != dict:
        print('\nERROR: Wrong data format. Please provide dictionary.\n')
        return cred_dict

    db2_user = cred['connection']['db2']['authentication']['username']
    db2_pass = cred['connection']['db2']['authentication']['password']
    db2_hostname = cred['connection']['db2']['hosts'][0]['hostname']
    db2_port = cred['connection']['db2']['hosts'][0]['port']
    db2_database = cred['connection']['db2']['database']
    cred_dict = {
        'db2_user' : db2_user,
        'db2_pass' : db2_pass,
        'db2_hostname' : db2_hostname,
        'db2_port' : db2_port,
        'db2_database' : db2_database
    }
    return cred_dict


cred_test = {'connection': {'cli': {'arguments': [['-u', 'user_name', '-p', 'user_password', '--ssl', '--sslCAFile', '1dd14d0c-1b52-4f63-a606-53ecba28771d', '--authenticationDatabase', 'admin', '--host', 'user_hostname:user_port']], 'bin': 'db2', 'certificate': {'certificate_base64': 'sertificate_long_number', 'name': 'sertifiacte_name'}, 'composed': ['db2 -u user_name -p user_password --ssl --sslCAFile 1dd14d0c-1b52-4f63-a606-53ecba28771d --authenticationDatabase admin --host user_hostname:user_port'], 'environment': {}, 'type': 'cli'}, 'db2': {'authentication': {'method': 'direct', 'password': 'user_password', 'username': 'user_name'}, 'certificate': {'certificate_base64': 'sertificate_long_number', 'name': '1dd14d0c-1b52-4f63-a606-53ecba28771d'}, 'composed': ['db2://user_name:user_password@user_hostname:user_port/user_database?authSource=admin&replicaSet=replset'], 'database': 'user_database', 'host_ros': [], 'hosts': [{'hostname': 'user_hostname', 'port': 'user_port'}], 'jdbc_url': ['jdbc:db2://user_hostname:user_port/user_database:user=<userid>;password=<your_password>;sslConnection=true;'], 'path': '/user_database', 'query_options': {'authSource': 'admin', 'replicaSet': 'replset'}, 'replica_set': 'replset', 'scheme': 'db2', 'type': 'uri'}}, 'instance_administration_api': {'deployment_id': 'long_deployment_id', 'instance_id': 'long_instance_id', 'root': 'https://apieugb.db2.cloud.ibm.com/v5/ibm'}}

print()
for k, v in db2_creds(cred_test).items():
    print(f'{k} \t {v}')
print()