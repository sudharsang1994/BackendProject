from configuration.properties import environments
import mysql.connector as sql
import logging

duplicate_error = "Could not execute query"


class DBEngine:

    def __init__(self, threaded=False):
        self.threaded = threaded
        self._pool = self.__init_pool(threaded)

    def __init_pool(self, threaded=False):
        connection = sql.connect(host=environments['dev']['o_host'], user=environments['dev']['o_user'],
                                 password=environments['dev']['o_password'], database=environments['dev']['o_database']
                                 )
        logging.info(connection)
        return connection

    def execute_query(self, query, get_columns=False):
        return self.__execute_query(query=query, fetchmany=False, fetchone=False, get_columns=get_columns)

    def __execute_query(self, query, params={}, fetch_size=1, fetchmany=False, fetchone=False, get_columns=False):
        try:
            with self._pool as conn:
                cursor = conn.cursor()
                cursor.execute(query, params)

                if fetchmany is True and fetchone is False:
                    query_result = cursor.fetchmany(fetch_size)

                elif fetchmany is False and fetchone is True:
                    query_result = cursor.fetchone()

                elif fetchmany is False and fetchone is False:
                    query_result = cursor.fetchall()

                if get_columns:
                    columns = [d[0] for d in cursor.description]
                    return query_result, columns
                else:
                    return query_result

        except Exception as e:
            logging.error(duplicate_error + query + "\n" + str(e))
