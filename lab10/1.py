import psycopg2
import random

conn = psycopg2.connect(
    host = 'localhost',
    database = 'pp_db',
    user = 'pp_user',
)
running  = True
print('PhoneBook --------------------------------------------------')
while running:
    print('Commands: insert | update | query | delete | exit')
    command = input()

    if command == 'insert' or command == '/i':
        insert_type = input('Choose insert option: terminal | file\n')
        if insert_type == 'terminal' or insert_type == '/t':
            user = input('input text in format \'user, 7-777-777-77-77\'\n')
            user = user.split(', ')
            sql = f"insert into phoneBook (name, phone) values ('{user[0]}','{user[1]}');"
        elif insert_type == 'file' or insert_type == '/f':
            # with open('phoneBook.csv', 'w') as f:
            #     for i in range(10) :
            #         s = f'\'{random.randint(1, 10)}-{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(10, 99)}\''
            #         f.writelines(f'\'user{i + 1}\', {s}\n')

            with open('phoneBook.csv', 'r') as f :
                data = f.readlines()

            for i in range(len(data)) :
                data[i] = data[i].removesuffix('\n')
                data[i] = f"({data[i]})"

            sql = f"insert into phoneBook (name, phone) values {','.join(data)};"

    elif command == 'update' or command == '/u':
        update_type = input('Choose what to update: name | phone\n')
        if update_type == 'name' or update_type == 'n':
            phone = input('Enter phone of the user\n')
            new_name = input('Enter the new name you want to set\n')
            sql = f'''
                update phoneBook
                set name = \'{new_name}\'
                where phone = \'{phone}\'
            '''
        elif update_type == 'phone' or update_type == '/p':
            name = input('Enter name of the user\n')
            new_phone = input('Enter the new phone number you want to set\n')
            sql = f'''
                update phoneBook
                set phone = \'{new_phone}\'
                where name = \'{name}\'
            '''

    elif command == 'query' or command == '/q':
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
                delete from phoneBook
                where id > 0
            '''
        else :
            sql = f'''
                delete from phoneBook
                where name = \'{user}\' or phone = \'{user}\'
            '''
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