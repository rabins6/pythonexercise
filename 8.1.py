import mysql.connector


def getAirportDetailByIdent(icao_code):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao_code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport name = {row[0]}")
            print(f"Airport location = {row[1]}")
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

icao_code = input("Write ICAO code of an airport : ")
getAirportDetailByIdent(icao_code.upper())