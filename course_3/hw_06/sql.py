import sqlite3
from contextlib import contextmanager


@contextmanager
def conn_context(db_path: str):
    """
    SQLite context manager for safe connections handling.
    :param db_path: path to database
    """
    conn = sqlite3.connect(db_path)
    yield conn
    conn.commit()
    conn.close()


if __name__ == '__main__':
    with conn_context('sql.sqlite') as conn:
        c = conn.cursor()

        c.executescript(
            """
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                `name` TEXT NOT NULL,
                description TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS units (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                `name` TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS positions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                `name` TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS goods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                `name` TEXT NOT NULL,
                unit_id INT NOT NULL,
                category_id INT NOT NULL,
                FOREIGN KEY(unit_id) REFERENCES units(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE, 
                FOREIGN KEY(category_id) REFERENCES categories(id)
                    ON UPDATE CASCADE
                    ON DELETE CASCADE 
            );
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT NOT NULL,
                position_id INT NOT NULL,
                FOREIGN KEY(position_id) REFERENCES positions(id)
                    ON UPDATE CASCADE
                    ON DELETE SET NULL 
            );
            CREATE TABLE IF NOT EXISTS vendors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                `name` TEXT NOT NULL,
                ownerchipform TEXT NOT NULL,
                address TEXT NOT NULL,
                phone TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """
        )

        c.executescript(
            """
            INSERT INTO units VALUES (1, 'pc.');
            INSERT INTO categories VALUES (1, 'fruits', 'good fruits');
            INSERT INTO goods VALUES (1, 'good#1', 1, 1);
            """
        )

        result = c.execute(
            """
            SELECT g.name, u.name, c.name FROM goods g
                LEFT JOIN units u ON u.id = g.unit_id
                LEFT JOIN categories c ON c.id = g.category_id;
            """
        )

        print(result.fetchone())

