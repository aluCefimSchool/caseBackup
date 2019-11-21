import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import mysql.connector
from mysql.connector import errorcode

from datetime import datetime

try:
    cnx = mysql.connector.connect(
        user='Case_CDA',
        port=3306,
        password='6wJwKUA7XZ8d&Wb!',
        host='da.cefim-formation.org',
        database='Case_CDA',
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

# connection à l'api google gspread
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('Satisfaktion-b5ad91466942.json', scope)
client = gspread.authorize(creds)

# ouverture de la sheet1
sheet = client.open('satisfaktion').sheet1

# récupération des données de la sheet1
students = sheet.get_all_values()

# Création du fichier csv
with open('satisfaktion.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(students)
csvFile.close()

# vider le formulaire
# cursor = cnx.cursor()
# check_empty_form_Table = "SELECT EXISTS (SELECT 1 FROM form)"
# cursor.execute(check_empty_form_Table)
# empty_form_Table = cursor.fetchone()
# print(empty_form_Table[0])
# response_empty_form_Table = empty_form_Table[0]
# print(response_empty_form_Table)
# if response_empty_form_Table == 1:
#   delete_form = "DELETE FROM form"
#   cursor.execute(delete_form)
#   print("the table is emptied.")
# cursor.close()


# Lecture du fichier csv
with open('satisfaktion.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    id_counter = 1
    for row in csv_reader:

        if line_count == 0:
            cursor = cnx.cursor()
            # print(f'Column names are {", ".join(row)}')
            # print(f'\t{row[0]}')
            try:

                # check_question_alphabetic_Table = "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'mydb') AND (TABLE_NAME = 'question_alphabetic')"
                # check_question_numeric_Table = "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'mydb') AND (TABLE_NAME = 'question_numeric')"
                # check_user_Table = "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'mydb') AND (TABLE_NAME = 'form')"
                # cursor.execute(check_user_Table)
                # resultExist = cursor.fetchone()
                # print(resultExist)

                # if len(resultExist) != 1:
                #   print("The table does not exist")
                # else:
                #   print("The table exists")
                # exit()

                # check_exist = "SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = 'mydb') AND (TABLE_NAME = %s)"
                # check_empty = "SELECT EXISTS (SELECT 1 FROM %s)"
                # empty_table = "DELETE FROM %s"

                # question alphabétiques
                check_empty_question_alphabetic_Table = "SELECT EXISTS (SELECT 1 FROM question_alphabetic)"
                add_alphabetic_question = "INSERT IGNORE INTO `question_alphabetic` (`question`) VALUES (%s)"
                cursor.execute(check_empty_question_alphabetic_Table)
                empty_question_alphabetic_Table = cursor.fetchone()
                print(empty_question_alphabetic_Table)

                if empty_question_alphabetic_Table == (0,):
                    # print("The table is not empty")
                    # delete_form_question_numeric = "DELETE FROM question_alphabetic"
                    # cursor.execute(delete_form_question_numeric)
                    # print("the table is emptied.")

                    cursor.execute(add_alphabetic_question, (row[9],))
                    cursor.execute(add_alphabetic_question, (row[10],))
                    cursor.execute(add_alphabetic_question, (row[15],))
                    cursor.execute(add_alphabetic_question, (row[16],))
                    cursor.execute(add_alphabetic_question, (row[17],))
                    cnx.commit()

                # questions numériques
                check_empty_question_numeric_Table = "SELECT EXISTS (SELECT 1 FROM question_numeric)"
                add_numeric_question = "INSERT IGNORE INTO `question_numeric` (`question`) VALUES (%s)"
                cursor.execute(check_empty_question_numeric_Table)
                empty_question_numeric_Table = cursor.fetchone()
                if empty_question_numeric_Table == (0,):
                    # print("The table is not empty")
                    # delete_form_question_numeric = "DELETE FROM question_numeric"
                    # cursor.execute(delete_form_question_numeric)
                    # print("the table is emptied.")

                    cursor.execute(add_numeric_question, (row[3],))
                    cursor.execute(add_numeric_question, (row[4],))
                    cursor.execute(add_numeric_question, (row[5],))
                    cursor.execute(add_numeric_question, (row[6],))
                    cursor.execute(add_numeric_question, (row[7],))
                    cursor.execute(add_numeric_question, (row[8],))
                    cursor.execute(add_numeric_question, (row[11],))
                    cursor.execute(add_numeric_question, (row[12],))
                    cursor.execute(add_numeric_question, (row[13],))
                    cursor.execute(add_numeric_question, (row[14],))
                    cnx.commit()
            finally:
                # cursor.close()
                print("stop")
            line_count += 1
        else:

            cursor = cnx.cursor()
            # select id_question_alpha
            select_id_question_alpha = "SELECT id_question FROM question_alphabetic"
            cursor.execute(select_id_question_alpha)
            result = cursor.fetchall()
            id_question_alpha = []
            for rowalpha in result:
                id_question_alpha.append(rowalpha[0])

            # select id_question_num
            select_id_question_num = "SELECT id_question FROM question_numeric"
            cursor.execute(select_id_question_num)
            result = cursor.fetchall()
            id_question_num = []
            for rownum in result:
                id_question_num.append(rownum[0])
            cursor.close()

            cursor = cnx.cursor(dictionary=True)
            # select id_promotion
            select_id_promotion = "SELECT id_promotion FROM promotion WHERE promotion = %s "
            cursor.execute(select_id_promotion, (row[17],))
            result = cursor.fetchone()
            print(result['id_promotion'])
            cnx.commit()

            # formulaire
            count_form = "SELECT COUNT(*) FROM form"
            cursor.execute(count_form)
            count_row_form = cursor.fetchone()
            count_reponse_row_form = count_row_form['COUNT(*)']

            datetime_object = datetime.strptime(row[0], '%m/%d/%Y %H:%M:%S')
            add_form_info = "INSERT IGNORE INTO form (firstname, lastname, id_promotion, release_date) VALUES (%s, %s, %s, %s)"

            print(line_count)
            print(id_counter)

            if count_reponse_row_form < line_count:
                print("Le nombre de lignes est plus petit que count_row_form")
                cursor.execute(add_form_info, (row[2], row[1], result["id_promotion"], datetime_object))
                cnx.commit()

            else:
                print("Le nombre de ligne est plus grand que le form")

            cursor.execute(add_form_info, (row[2], row[1], result["id_promotion"], datetime_object))
            cnx.commit()

            # select form_id
            select_form_id = "SELECT id_form FROM form"
            cursor.execute(select_form_id)
            form_id = cursor.fetchall()

            id_form = []
            for rownum in form_id:
                id_form.append(rownum['id_form'])
            id_form = id_form[id_counter]
            cnx.commit()

            id_counter += 1

            # insert in link table
            check_empty_form_qestionnumeric_Table = "SELECT EXISTS (SELECT 1 FROM form_qestionnumeric)"
            insert_form_numericq = "INSERT IGNORE INTO `form_qestionnumeric` (id_form, id_question) VALUES (%s,%s)"

            cursor.execute(check_empty_form_qestionnumeric_Table)
            empty_form_qestionnumeric_Table = cursor.fetchone()

            for id_q_n in id_question_num:
                val = (id_form, id_q_n)
                cursor.execute(insert_form_numericq, val)
                cnx.commit()

            cnx.commit()
            reponse_empty_form_qestionnumeric_Table = empty_form_qestionnumeric_Table[
                'EXISTS (SELECT 1 FROM form_qestionnumeric)']

            check_empty_form_questionalphabetic_Table = "SELECT EXISTS (SELECT 1 FROM form_questionalphabetic)"
            insert_form_alphaq = "INSERT IGNORE INTO `form_questionalphabetic` (id_form, id_question) VALUES (%s,%s)"

            cursor.execute(check_empty_form_questionalphabetic_Table)
            empty_form_questionalphabetic_Table = cursor.fetchone()

            for id_q_a in id_question_alpha:
                val = (id_form, id_q_a)
                cursor.execute(insert_form_alphaq, val)
                cnx.commit()

            cnx.commit()
            reponse_empty_form_questionalphabetic_Table = empty_form_questionalphabetic_Table[
                'EXISTS (SELECT 1 FROM form_questionalphabetic)']

            for id_q_a in id_question_alpha:
                cursor.execute(insert_form_alphaq, id_form, id_q_a)
                cnx.commit()

            # réponses alphabétiques
            count_reponse_alphabetic_Table = "SELECT COUNT(*) FROM response_alphabetic"
            add_alphabetic_response = "INSERT IGNORE INTO `response_alphabetic` (response, id_question) VALUES (%s,%s)"
            cursor.execute(count_reponse_alphabetic_Table)
            count_reponse_alphabetic_Table = cursor.fetchall()
            count_reponse_alphabetic_Table = count_reponse_alphabetic_Table[0]['COUNT(*)']
            cnx.commit()

            # if empty_reponse_alphabetic_Table ==0:
            #   delete_response_alphabetic = "DELETE FROM response_alphabetic"
            #   cursor.execute(delete_response_alphabetic)
            #   print("the table is emptied.")
            if count_reponse_alphabetic_Table <= 84:
                cursor.execute(add_alphabetic_response, (row[9], id_question_alpha[0]))
                cursor.execute(add_alphabetic_response, (row[10], id_question_alpha[1]))
                cursor.execute(add_alphabetic_response, (row[11], id_question_alpha[2]))
                cursor.execute(add_alphabetic_response, (row[15], id_question_alpha[3]))
                cursor.execute(add_alphabetic_response, (row[16], id_question_alpha[4]))

                cnx.commit()

            # réponses numériques
            count_reponse_numeric_Table = "SELECT COUNT(*) FROM response_numeric"
            add_numeric_response = "INSERT IGNORE INTO `response_numeric` (response, id_question) VALUES (%s,%s)"
            cursor.execute(count_reponse_numeric_Table)
            count_reponse_numeric_Table = cursor.fetchall()
            cnx.commit()

            count_reponse_numeric_Table = count_reponse_numeric_Table[0]['COUNT(*)']

            # if empty_reponse_numeric_Table == 0:
            #   delete_response_alphabetic = "DELETE FROM response_numeric"
            #   cursor.execute(delete_response_alphabetic)
            #   print("the table is emptied.")

            if count_reponse_numeric_Table <= 126:
                cursor.execute(add_numeric_response, (row[3], id_question_num[0]))
                cursor.execute(add_numeric_response, (row[4], id_question_num[1]))
                cursor.execute(add_numeric_response, (row[5], id_question_num[2]))
                cursor.execute(add_numeric_response, (row[6], id_question_num[3]))
                cursor.execute(add_numeric_response, (row[7], id_question_num[4]))
                cursor.execute(add_numeric_response, (row[8], id_question_num[5]))
                cursor.execute(add_numeric_response, (row[11], id_question_num[6]))
                cursor.execute(add_numeric_response, (row[12], id_question_num[7]))
                cursor.execute(add_numeric_response, (row[13], id_question_num[8]))
                cursor.execute(add_numeric_response, (row[14], id_question_num[9]))

                cnx.commit()
            line_count += 1
    print(f'Processed {line_count} lines.')

