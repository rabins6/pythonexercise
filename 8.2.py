import mysql.connector


def getAirportsByAreaCode(area_code):
    sql = "SELECT * FROM airport"
    sql += " WHERE iso_country='" + area_code + "'"
    sql += " ORDER BY type ASC"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return


# Main program
connection = mysql.connector.connect(
          host='127.0.0.1',
          port=3306,
          database='flight_game',
          user='root',
          password='Cricketer1',
          autocommit=True
          )

area_code = input("Write area code of a country (for e.g. - FI) : ")
getAirportsByAreaCode(area_code.upper())