from . import CONN, CURSOR

class Recommendations:

    def __init__(self, title):
        self.title =title
        self.id =None

    @classmethod
    def create_table(self):
        sql = '''
        CREATE TABLE IF NOT EXISTS recommendations_table (
        id INTEGER PRIMARY KEY,
        title TEXT
        );
        '''

        CURSOR.execute(sql)
        CONN.commit()
    
    def create(self):
        sql = 'INSERT INTO recommendations_table (title) VALUES (?);'

        CURSOR.execute(sql, [self.title])
        CONN.commit()

        last_row_sql = '''
        SELECT * FROM recommendations_table
        ORDER BY id DESC
        LIMIT 1
        '''
        last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
        self.id = last_row_tuple[0]

    @classmethod
    def read_all(cls):
        sql = '''
        SELECT * FROM recommendations_table;
        '''

        all_animes_tuples = CURSOR.execute(sql).fetchall()

        return all_animes_tuples
    

class Animes:

    def __init__(self, anime):
        self.anime = anime
        self.id = None

@classmethod
def create_table(self):
    sql = '''
        CREATE TABLE IF NOT EXISTS animes_table (
        id INTEGER PRIMARY KEY,
        anime TEXT
        );
        '''
    CURSOR.execute(sql)
    CONN.commit()

def create(self):
    sql = 'INSERT INTO aanimes_table (anime) VALUES (?);'

    CURSOR.execute(sql, [self.anime])
    CONN.commit()

    last_row_sql = '''
    SELECT * FROM animes_table
    ORDER BY id DESC
    LIMIT 1
    '''
    last_row_tuple = CURSOR.execute(last_row_sql).fetchone()
    self.id = last_row_tuple[0]


class Questions:

    def __init__(self, question):
        self.question = question
        self.id = None

    @classmethod
    def create_table(self):
        sql = '''
            CREATE TABLE IF NOT EXISTS questions_table (
            id INTEGER PRIMARY KEY,
            question TEXT
            );
            '''
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def read_all(cls):
        sql = '''
        SELECT * FROM questions_table;
        '''

        all_questions_tuples = CURSOR.execute(sql).fetchall()

        return all_questions_tuples

