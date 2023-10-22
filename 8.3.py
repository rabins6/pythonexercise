import mysql.connector
import geopy.distance


def getAirportsByICAO(icao_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao_code + "'"

    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount > 0:
        for row in result:
            return row
    return


def calculateDistanceInKilometer(coordinate_1, coordinate_2):
    return geopy.distance.distance(coordinate_1, coordinate_2).km


# Main program
connection = mysql.connector.connect(
          host='127.0.0.1',
          port=3306,
          database='flight_game',
          user='root',
          password='Cricketer1',
          autocommit=True
          )

icao_code_1 = input("Write ICAO code of a 1st airport : ")
coordinate_1 = getAirportsByICAO(icao_code_1)

icao_code_2 = input("Write ICAO code of a 2nd airport : ")
coordinate_2 = getAirportsByICAO(icao_code_2)

distanceInKilometer = calculateDistanceInKilometer(coordinate_1, coordinate_2)

print(f"The distance between two airports is: {distanceInKilometer : .2f} kilometer")