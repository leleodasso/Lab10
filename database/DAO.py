from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import County


class DAO():

    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []
        query = """select *  
                    from country """
        cursor.execute(query, ())

        for row in cursor:
            result.append(County(*row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []
        query = """select distinct ca.StateAbb, ca.CCode, ca.StateNme
                   from countries.contiguity c, countries.country ca
                   where c.`year` <= %s
                    and c.state1no = ca.CCode"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(County(*row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []
        query = """select *
                    from countries.contiguity c
                    where c.`year` <= %s
                    and conttype = 1"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Contiguity(*row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getWeightNodes(anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor()

        result = []
        query = """SELECT c.state1no, c.state1ab, ca.StateNme,COUNT(state1no) AS peso
                       from countries.contiguity c, countries.country ca
                       where c.`year` <= %s
                       and conttype = 1
                       and c.state1no = ca.CCode
                    group by c.state1no
                    order by ca.StateNme"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append((row[2], row[3], row[0]))

        cursor.close()
        conn.close()
        return result



