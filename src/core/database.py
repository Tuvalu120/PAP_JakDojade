import oracledb

_HOST = "xxx"
_SERVICE_NAME = "xxx"
_PORT = 1521
_DSN = oracledb.makedsn(_HOST, _PORT, service_name=_SERVICE_NAME)


class Database:
    """
    Cursor access to the Z14 database
    """

    def __init__(self):
        self._connection = oracledb.connect(user='xxx', password="xxx", dsn=_DSN)

    @property
    def cursor(self):
        return self._connection.cursor()

    def simple_type_mapping(self, sql: str, map_to):
        """
        Converts the results of a sql select to a list of elements of 'map_to' type
        :param sql: sql select
        :param map_to: type to map to
        :return: list
        """
        out = []
        cur = self.cursor.execute(sql)
        for row in cur.fetchall():
            out.append(map_to(*row))
        return out
