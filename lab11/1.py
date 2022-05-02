import psycopg2
import random
import re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'pp_db',
    user = 'pp_user',
)
running  = True
print('PhoneBook --------------------------------------------------')
while running:
    print('Commands: insert | query | delete | exit')
    command = input()

    if command == 'insert' or command == '/i':
        insert_type = input('Choose insert option: terminal | file\n')
        if insert_type == 'terminal' or insert_type == '/t':
            n = input('How many users you want to insert?\n')
            print('input text in format \'user, 7-777-777-77-77\'')
            for i in range(int(n)) :
                user = input()
                user = user.split(', ')
                if re.match("[0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]", user[1]) :
                    sql = f"call insertUser('{user[0]}', '{user[1]}');"
                    cursor = conn.cursor()
                    cursor.execute(sql)
                else :
                    print('Your phone is in incorrect format')
        elif insert_type == 'file' or insert_type == '/f':
            # with open('phoneBook.csv', 'w') as f:
            #     for i in range(100) :
            #         s = f'\'{random.randint(1, 10)}-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}\''
            #         f.writelines(f'\'user{i + 1}\', {s}\n')

            with open('phoneBook.csv', 'r') as f :
                data = f.readlines()

            for i in range(len(data)) :
                data[i] = data[i].removesuffix('\n')
                data[i] = f"({data[i]})"

            sql = f"insert into phoneBook (name, phone) values {','.join(data)};"

    elif command == 'query' or command == '/q':
        query_type = input('Do you want to find users by pattern? y | n\n')
        if query_type == 'y' or query_type == 'yes' :
            pattern = input('Enter the pattern\n')
            sql = f'''
                select *
                from getUserFromPattern('%{pattern}%');
            '''
        else :
            pagination = input('Dou you want to get pages? y | n\n')
            if pagination == 'yes' or pagination == 'y' :
                page = input('Enter which page you want to see?\n')
                sql = f"select * from getUsersWithPagination({int(page)}, 10);"
            else :
                user = input('Enter name or phone of the user you want to find\n')
                if user == '/all' :
                    sql = '''
                        select *
                        from phoneBook
                    '''
                else :
                    sql = f'''
                        select *
                        from phoneBook
                        where name = \'{user}\' or phone = \'{user}\'
                '''

    elif command == 'delete' or command == '/d':
        user = input('Enter name or phone of the user you want to delete\n')
        if user == '/all' :
            sql = '''
                alter sequence phonebook_id_seq restart with 1;
                delete from phoneBook
                where id > 0;
            '''
        else :
            sql = f"call deleteUser('{user}');"
    elif command == 'exit' or command == '/e' :
        running = False

    if command != 'exit' and command != '/e' :
        cursor = conn.cursor()
        cursor.execute(sql)
        if command == 'query' or command == '/q':
            result = cursor.fetchall()
            if len(result) > 0 :
                for i in result :
                    print(f'{i[1]}, {i[2]}')
            else :
                print('There is no such user')
        else :
            conn.commit()

        cursor.close()

conn.close()