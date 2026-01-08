
import psycopg2

def connect_to_postgres():
    """Connect to the PostgreSQL database server"""
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host="localhost",
            database="app_db",
            user="yadnesh.deore",
            password="postgres123"  # IMPORTANT: REPLACE WITH YOUR ACTUAL PASSWORD
        )

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        # For example, create a table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            )
        """)
        conn.commit()
        print("Table 'users' ensured to exist.")

        # Insert some data
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING", ('John Doe', 'john.doe@example.com'))
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING", ('Jane Smith', 'jane.smith@example.com'))
        conn.commit()
        print("Sample data inserted (if not already present).")

        # Query data
        cur.execute("SELECT id, name, email FROM users")
        users = cur.fetchall()
        print("\nUsers in the database:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect_to_postgres()
