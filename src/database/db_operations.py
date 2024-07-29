from .db_connection import DBConnection

class DBOperations:
    def __init__(self):
        self.db_connection = DBConnection()

    def add_name(self, name: str) -> dict:
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "INSERT INTO guests (name) VALUES (%s)"
            cursor.execute(query, (name,))
            connection.commit()
            return {"message": "Name added successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

    def remove_name(self, name: str) -> dict:
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "DELETE FROM guests WHERE name = %s"
            cursor.execute(query, (name,))
            connection.commit()
            return {"message": "Name removed successfully"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

    def show_guests(self) -> dict:
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "SELECT id, name FROM guests"
            cursor.execute(query)
            guests = cursor.fetchall()
            guest_dict = {guest[0]: guest[1] for guest in guests}
            return {"guests": guest_dict}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()

    def search_name(self, name: str) -> dict:
        try:
            connection = self.db_connection.connect()
            cursor = connection.cursor()
            query = "SELECT * FROM guests WHERE name = %s"
            cursor.execute(query, (name,))
            guest = cursor.fetchone()
            if guest:
                return {"guest": guest}
            return {"message": "Guest not found"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            cursor.close()
            connection.close()
