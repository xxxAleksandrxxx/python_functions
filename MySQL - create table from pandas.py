
import re

def sql_table_from_pandas(text_dtypes : str = '', table_name : str = '') -> str:
    ''' 
    Function: sql_table_from_pandas
    
    Description: Converts pandas dtypes table data information into an SQL query for creating a table.

    Parameters:
    - text_dtypes (str): Text containing converted to string pandas dtypes table data information.
    - table_name (str): Name of the SQL table to be created.

    Returns:
    - sql_query (str): SQL query for creating the table.
    '''

    # check if anything is in functiona parameters
    if not text_dtypes or not table_name:
        print('You probably forgot to pass attributes to function\ndouble-check and try again ^_^')
        return 'NONE'
    
    # dict for autoreplacement type from pandas to SQL format
    type_d = {
        'object' : 'VARCHAR(50)',
        'int64' : 'INT',
        'float64' : 'FLOAT'
    }

    # preparing SQL statment
    sql_stmnt_start = f'CREATE TABLE {table_name} (\nid INT PRIMARY KEY, \n'
    sql_stmnt_end = ')'
    sql_stmnt_middle = ''

    # convert text to list. one line - one element
    text_l = [elem for elem in text_dtypes.split('\n')]
    
    # pattern to extract data from pd.dtypes line
    # it extract into two groups: 
    # 1st should be the voulumn name
    # 2nd should be the data type
    pattern = r'(.+[\)\w])\s+(\w+)'
    
    # extract data and add it to sql_stmnt_middle
    for elem in text_l:
        match = re.search(pattern, elem)
        k = match.group(1).replace(' ', '_').replace('%', 'percent').replace('(', '').replace(')', '')
        v = type_d[match.group(2)]
        sql_stmnt_middle += f'{k} {v}, \n'
    
    # delete the last ',' and space from SQL code to repare it
    sql_stmnt_middle = sql_stmnt_middle[:-3]

    return sql_stmnt_start + sql_stmnt_middle + sql_stmnt_end






text = '''Category                          object
Item                              object
Serving Size                      object
Calories                           int64
Calories from Fat                  int64
Total Fat                        float64
Total Fat (% Daily Value)          int64
Saturated Fat                    float64
Saturated Fat (% Daily Value)      int64
Trans Fat                        float64
Cholesterol                        int64
Cholesterol (% Daily Value)        int64
Sodium                             int64
Sodium (% Daily Value)             int64
Carbohydrates                      int64
Carbohydrates (% Daily Value)      int64
Dietary Fiber                      int64
Dietary Fiber (% Daily Value)      int64
Sugars                             int64
Protein                            int64
Vitamin A (% Daily Value)          int64
Vitamin C (% Daily Value)          int64
Calcium (% Daily Value)            int64
Iron (% Daily Value)               int64'''





table_name = 'MC_NUTRITION'

sql_query = sql_table_from_pandas(text, table_name);
print(sql_query)