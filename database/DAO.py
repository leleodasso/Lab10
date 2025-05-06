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
                    and conttype = 1
                    and c.state1no < c.state2no """
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
        query = """SELECT state1no, state1ab, COUNT(state1no) AS peso
                       from countries.contiguity c
                       where c.`year` <= %s
                       and conttype = 1
                       and c.state1no < c.state2no
                    group by c.state1no"""
        cursor.execute(query, (anno,))

        for row in cursor:
            result.append((row[1], row[2]))

        cursor.close()
        conn.close()
        return result



