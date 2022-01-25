import psycopg2


def get_data_from_DB(strhostname, strDatabase, strUser, strPassword, strQuery):
    conn = psycopg2.connect(host=strhostname, database=strDatabase, user=strUser, password=strPassword)
# conn = psycopg2.connect(host="localhost", database="LMS_DB", user="postgres", password="postgres")
    cursor = conn.cursor()
    # strQuery='select skill_id,skill_name from tbl_lms_skill_master '
    cursor.execute(strQuery)
    headers = [i[0] for i in cursor.description]
    resultSet = cursor.fetchall()
    res=[]
    for result in resultSet:
        result = list(result)
        dictionary = dict(zip(headers, result))
        res.append(dictionary)

    print(res)
    return res
