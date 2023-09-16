import os, asyncio, sqlite3
import constPaths

# инициализация нулевого баланса для пользователя
async def setNewUserBalance(user_id: int) -> None:
    balance_db = constPaths.db_paths["balance"]
    connection = sqlite3.connect(balance_db)
    cursor = connection.cursor()
    parameters = f"INSERT INTO balanceTable (user_id, balance) VALUES ({user_id}, 0)"
    cursor.execute(parameters)
    connection.commit()
    cursor.close(); connection.close()