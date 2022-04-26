import psycopg2
conn = psycopg2.connect(
    host = 'localhost',
    database = 'pp_db',
    user = 'pp_user',
)

cursor = conn.cursor()

user = input('Enter your name\n')

def updateUserLevel() :
    sql = f'''
        select *
        from users
        where name = \'{user}\'
    '''
    cursor.execute(sql)
    global user_data
    user_data = cursor.fetchone()

updateUserLevel()
if user_data is None :
    sql = f'''
        insert into users (name)
        values (\'{user}\')
    '''
    cursor.execute(sql)
    conn.commit()
    print(f'New user \'{user}\' created')
    updateUserLevel()
else :
    print(f'Logged in as \'{user}\'')