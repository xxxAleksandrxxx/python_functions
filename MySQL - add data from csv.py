# gerate SQL code to import data from .csv files to current MySQL database
import getpass

def sql_data_from_csv(
        sql_tables : str,
        csv_filenames : str,
        csv_path : str = 'DEFAUALT',
        header_exist : bool = False,
        sep_col : str = ',',
        sep_line : str = '\\n',
        sep_encl : str = '"'
        ) -> list:
    '''
    Function: sql_data_from_csv
    
    Description: Generates SQL import code for loading data from CSV files into SQL tables.

    Parameters:
    - sql_tables (str): Names of SQL tables to import the data into (separated by new lines).
    - csv_filenames (str): Filenames of the CSV files to import (separated by new lines).
    - csv_path (str, optional): Path where the CSV files are located (default: 'DEFAUALT'). That means that it's '~/Downloads'.
    - header_exist (bool, optional): Flag indicating if the CSV files have a header row (default: False).
    - sep_col (str, optional): Column separator used in the CSV files (default: ',').
    - sep_line (str, optional): Line separator used in the CSV files (default: '\n').

    Returns:
    - code_for_sql (list): List of generated SQL import code for each SQL table and CSV file pair.
    '''
    if not csv_filenames:
        return 'ERROR: There is no code as you forgot to provide any file for import...'
    if not sql_tables:
        return 'ERORR: There is no code as you forgot to provide any table name to import to... '
    
    # convert .csv filenames to list
    csv_filenames = [elem.strip() for elem in csv_filenames.split('\n') if elem != '']
    
    # fonvert sql table names to list
    sql_tables = [elem.strip() for elem in sql_tables.split('\n') if elem != '']
    
    # check that at least number of .csv files match number of tables
    len_csv = len(csv_filenames)
    len_sql = len(sql_tables)
    if len_csv != len_sql:
        return 'ERROR: There is something wrong as number of sql tables have to be the same as number of .csv files with data'
    
    # if path of .csv location wasn't provide we assume that all .csv are in Downloars folder
    if csv_path == 'DEFAUALT':
        user_name = getpass.getuser()
        csv_path = f'/Users/{user_name}/Downloads'

    # the list with final result
    code_for_sql = list()
    
    # create sql code and add it to code_for_sql list
    # hope that sequence of sql table names corelated to sequence of .csv filenames
    # probably I'll try to mange it later...
    for i in range(len_sql):
        sql_table_name = sql_tables[i]
        csv_name = csv_filenames[i]
        # ATTENTION! we assume that path name is connecter fo macos so the script would work wrong on Windows system
        # ATTENTION! following script will not work with date columns as they have to be converted to SQL date type format with:
        #   SET B_DATE = STR_TO_DATE(@B_DATE, '%m/%d/%Y');
        #
        # for example to import data from frile Employees.csv with lines like:
        #   E1001,John,Thomas,123456,01/09/1976,M,"5631 Rice, OakPark,IL",100,100000,30001,2
        #   E1002,Alice,James,123457,07/31/1972,F,"980 Berry ln, Elgin,IL",200,80000,30002,5
        # to table EMPLOYEES which has following columns:
        #   EMP_ID, F_NAME, L_NAME, SSN, B_DATE, SEX, ADDRESS, JOB_ID, SALARY, MANAGER_ID, DEP_ID
        # we have to use a code like this:
        #   LOAD DATA LOCAL INFILE 'Employees.csv'
        #   INTO TABLE EMPLOYEES
        #   FIELDS TERMINATED BY ','
        #   ENCLOSED BY '"'
        #   LINES TERMINATED BY '\n'
        #   (EMP_ID, F_NAME, L_NAME, SSN, @B_DATE, SEX, ADDRESS, JOB_ID, SALARY, MANAGER_ID, DEP_ID)
        #   SET B_DATE = STR_TO_DATE(@B_DATE, '%m/%d/%Y');
        #
        #
        # TO DO:
        # - add list with messages like this:
        #       Data from file table_name.csv to table table_name copied.......SUCCESS
        #       Data from file table_name.csv to table table_name copied.......SKIP (date column)
        #       Data from file table_name.csv to table table_name copied.......FAIL (no data)
        
        code = (
            f"LOAD DATA LOCAL INFILE '{csv_path}/{csv_name}' "
            f"INTO TABLE {sql_table_name} "
            f"FIELDS TERMINATED BY '{sep_col}' "
            f"ENCLOSED BY '{sep_encl}' "
            f"LINES TERMINATED BY '{sep_line}' "
            f"{['', 'IGNORE 1 ROWS'][header_exist]};"
        )
        code_for_sql.append(code)
    return code_for_sql


# csv_names = '''
# Departments.csv
# Employees.csv
# JobsHistory.csv
# Jobs.csv
# Locations.csv'''

# table_names = '''
# DEPARTMENTS
# EMPLOYEES
# JOB_HISTORY
# JOBS
# LOCATIONS'''

csv_names = 'Jobs.csv'
table_names = 'JOBS'

result = sql_data_from_csv(sql_tables=table_names, csv_filenames=csv_names, header_exist=True)

# to print all generated codes
print('\n'*3)
for elem in result:
    print(elem)
print('\n'*3)


# # print only one specific line
# number_of_line = 1
# print('\n'*3)
# print(result[number_of_line - 1])
# print('\n'*3)