from .db_connection import DBConnection


class DBOperations:
    def __init__(self):
        self.db = DBConnection()

    def add_name(self, name: str):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            query = "INSERT INTO convidados (name) VALUES (%s)"
            cursor.execute(query, (name,))
            conn.commit()
            return {"message": "Guest added successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    def remove_name(self, name: str):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            query = "DELETE FROM convidados WHERE name = %s"
            cursor.execute(query, (name,))
            conn.commit()
            return {"message": "Guest removed successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    def show_guests(self):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            query = "SELECT name FROM convidados"
            cursor.execute(query)
            result = cursor.fetchall()
            return {"guests": [row[0] for row in result]}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()

    def search_name(self, name: str):
        try:
            conn = self.db.connect()
            cursor = conn.cursor()
            query = "SELECT name FROM convidados WHERE name = %s"
            cursor.execute(query, (name,))
            result = cursor.fetchone()
            if result:
                return {"guest": result[0]}
            else:
                return {"message": "Guest not found"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            conn.close()
