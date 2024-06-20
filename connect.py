import faker
import psycopg2


def connect_to_db():

    connection = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="xbnflhbnf0509",
        host="localhost",
        port="5432",
    )

    cursor = connection.cursor()


if __name__ == "__main__":

    connect_to_db()
