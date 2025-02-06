import sqlite3

class scoreDB:
    def __init__(self):
        self.conn   = sqlite3.connect('src/data/point.db')
        self.cursor = self.conn.cursor()

    def get_score(self):
        self.cursor.execute('''
            SELECT * FROM score
            ORDER BY score DESC
            LIMIT 10
        ''')

        self.conn.commit()

        return self.cursor.fetchall()
        
    def update_score(self, score):
        from src.auth_server.service.store_reader import email_reader

        self.cursor.execute('''
            UPDATE score
            SET score = CASE 
                            WHEN ? > score THEN ?  
                            ELSE score  
                        END
            WHERE username = ?;
        ''', (score, score, email_reader().split("@")[0]))

        self.conn.commit()

    def init_score(self):
        from src.auth_server.service.store_reader import email_reader

        self.cursor.execute('''
            INSERT INTO score (username, score)
            VALUES (?, ?)
        ''', (email_reader().split("@")[0], 0))

        self.conn.commit()

    def clear(self):
        self.cursor.execute('''
            DELETE FROM score
        ''')

        self.conn.commit()

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    try:
        score_db = scoreDB()
        score_db.clear()
    except Exception as e:
        print(str(e))

    pass