# seeds an sqlite DB with a secrets table (instructor may edit flags before student release)
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, bio TEXT)')
c.execute("DELETE FROM users")
c.execute("INSERT INTO users (username, bio) VALUES (?, ?)", ("alice", "bio1"))
c.execute("INSERT INTO users (username, bio) VALUES (?, ?)", ("bob", "bio2"))
c.execute('CREATE TABLE IF NOT EXISTS secrets (id INTEGER PRIMARY KEY, secret TEXT)')
c.execute("DELETE FROM secrets")
# DEFAULT FLAG - instructor should change before publishing
c.execute("INSERT INTO secrets (secret) VALUES (?)", ("flag{sql_injection_mastery}",))
conn.commit()
conn.close()
