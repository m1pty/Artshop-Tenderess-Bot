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

# изменение баланса
async def setBalance(user_id: int, balance: int) -> None:
    balance_db = constPaths.db_paths["balance"]
    connection = sqlite3.connect(balance_db)
    cursor = connection.cursor()
    parameters = f"UPDATE balanceTable SET balance = {balance} WHERE user_id = {user_id}"
    cursor.execute(parameters)
    connection.commit()
    cursor.close(); connection.close()

# уменьшение количества элементов дропа по id
async def setBannerDropQuantity(drop_id: int):
    drop_db = constPaths.db_paths["banner_prizes"]
    connection = sqlite3.connect(drop_db)
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT quantity FROM possible_prizes WHERE id = {drop_id}")
    quantity = (cursor.fetchall())[0][0]

    parameters = f"UPDATE possible_prizes SET quantity = {quantity - 1} WHERE id = {drop_id}"
    cursor.execute(parameters)
    connection.commit()
    cursor.close(); connection.close()