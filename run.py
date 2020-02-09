from login_gmail import main
import psycopg2


def dbConnect():
    '''this function checking the connectvity between the sql,
    this function need a db which is same as below'''
    try:
        dbconnection = psycopg2.connect(
            dbname='gmail_data', user='gmail_data', password='gmail', host='localhost')
    except TypeError as e:
        print(e)
        pass
    if dbconnection:
        return dbconnection


def createTable():
    '''after connection, it will check the table if not it will create a table on db'''
    dbSession = dbConnect()
    if dbSession:
        dbCursor = dbSession.cursor()
        sqlCreateTable = "CREATE TABLE Inbox(id bigint, subject varchar(255));"
        try:
            dbCursor.execute(sqlCreateTable)
        except TypeError as e:
            print(e)
            pass


def importData():
    '''after connection and create table, it will save data on the db, by defult it will take 
    3 value , so change it acording to need (in list), here main function also calling where the mail connection happning'''
    dbSession = dbConnect()
    if dbSession:
        dbCursor = dbSession.cursor()
        messages = main()
        # email_list=[]
        # for message in messages[0:3]:
        #     msg = service.users().messages().get(
        #         userId='me', id=message['id']).execute()
        #     email_list.append(msg['snippet'])
        i = 0
        for email_data in messages[:3]:
            sqlInsert = "INSERT INTO Inbox values('%d','%s');" % (
                i, email_data)
            i += 1
            dbCursor.execute(sqlInsert)


def index():
    '''it will call all the above function '''
    createTable()
    importData()


if __name__ == "__main__":
    index()
