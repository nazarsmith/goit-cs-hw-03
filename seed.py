import faker
import psycopg2

from random import randint, choice

NUMBER_TASKS = 100
NUMBER_DESCRIPTIONS = 100
NUMBER_USERS = 30
NUMBER_STATUSES = 3


def generate_fake_data(number_tasks, number_descriptions, number_users) -> tuple():
    fake_tasks = []
    fake_descriptions = []
    fake_users = []
    fake_emails = []
    fake_data = faker.Faker()

    for _ in range(number_tasks):
        fake_tasks.append(fake_data.text(max_nb_chars=20))

    for _ in range(number_descriptions):
        fake_descriptions.append(fake_data.paragraph(nb_sentences=3))

    for _ in range(number_users):
        fake_users.append(fake_data.name())

    for _ in range(number_users):
        while True:
            email = fake_data.email()
            if email not in fake_emails:
                fake_emails.append(email)
                if len(fake_emails) >= number_users:
                    break

    print(fake_tasks[:2], fake_descriptions[:2], fake_users[:2], fake_emails[:2])

    return fake_tasks, fake_descriptions, fake_users, fake_emails


def prepare_data(tasks, descriptions, users, emails) -> tuple():

    for_tasks = []
    for_users = []

    for task in tasks:
        for_tasks.append(
            (
                task,
                choice(descriptions),
                randint(1, NUMBER_STATUSES),
                randint(1, NUMBER_USERS),
            )
        )

    for user in users:
        email = emails.pop(-1)
        print(email)
        for_users.append((user, email))
    print(for_users)

    return for_tasks, for_users


def insert_data_to_db(for_tasks, for_users) -> None:
    with psycopg2.connect(
        dbname="dbname", user="user", password="password", host="localhost", port="5432"
    ) as connection:
        cursor = connection.cursor()
        print(len(for_users))

        sql_to_users = """INSERT INTO users (fullname, email)
                          VALUES (%s, %s)"""
        cursor.executemany(sql_to_users, for_users)
        connection.commit()

        sql_to_tasks = """INSERT INTO tasks (title, description, status_id, user_id)
                          VALUES (%s, %s, %s, %s)"""
        cursor.executemany(sql_to_tasks, for_tasks)
        connection.commit()


if __name__ == "__main__":
    for_tasks, for_users = prepare_data(
        *generate_fake_data(NUMBER_TASKS, NUMBER_DESCRIPTIONS, NUMBER_USERS)
    )
    insert_data_to_db(for_tasks, for_users)
