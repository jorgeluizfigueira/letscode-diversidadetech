import psycopg2
from configparser import ConfigParser

# carrega os dados de configuracao do BD
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

# Classe encarregada da conexao com o bd e execucao das instrucoes sql
class Conexao(object):
    
    _db=None
    def __init__(self, host,database,user,password):
        self._db = psycopg2.connect(host=host,database=database,user=user,password=password)
        
    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close();
            self._db.commit()
        except:
            return False;
        return True;
    
    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall();
        except:
            return None
        return rs

    def fechar(self):
        self._db.close()