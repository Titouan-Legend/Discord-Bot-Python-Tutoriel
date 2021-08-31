import os
import sqlite3
import datetime

class DatabaseHandler():
	def __init__(self, database_name : str):
		self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
		self.con.row_factory = sqlite3.Row

	def add_tempmute(self, user_id : int, guild_id : int, expiration_date : datetime.datetime):
		cursor = self.con.cursor()
		query = "INSERT INTO Tempmute (user_id, guild_id, expiration_date) VALUES (?, ?, ?);"
		cursor.execute(query, (user_id, guild_id, expiration_date))
		cursor.close()
		self.con.commit()

	def active_tempmute_to_revoke(self, guild_id : int) -> [dict]:
		cursor = self.con.cursor()
		query = f"SELECT * FROM Tempmute WHERE guild_id = ? AND active = 1 AND expiration_date < ?;"
		cursor.execute(query, (guild_id, datetime.datetime.utcnow()))
		result = list(map(dict, cursor.fetchall()))
		cursor.close()
		return result

	def revoke_tempmute(self, tempmute_id : int):
		cursor = self.con.cursor()
		query = f"UPDATE Tempmute SET active = 0 WHERE id = ?;"
		cursor.execute(query, (tempmute_id,))
		cursor.close()
		self.con.commit()
