import asyncio, sqlite3, os
import constPaths

# получение баланса по id пользователя
async def getBalance(user_id: int):
    balance_db = constPaths.db_paths["balance"]
    connection = sqlite3.connect(balance_db, check_same_thread = False)
    cursor = connection.cursor()

    cursor.execute(f"SELECT balance FROM balanceTable WHERE user_id = {user_id}")
    user_balance = (cursor.fetchall())
    cursor.close(); connection.close()

    return user_balance[0][0]

# получение доступных призов баннера
async def getTable():
    conn = sqlite3.connect(constPaths.db_paths["banner_prizes"], check_same_thread = False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM possible_prizes")
    exists = cursor.fetchall()
    cursor.close()
    conn.close()
    if exists:
        return exists

# возвращает список для выбора в рулетке
async def getBannerDrop() -> list:
    """ Returns list of possible prizes to random_get_from"""
    firstly = await getTable()
    possible_list = list()
    for string in firstly:
        sum = string[3] * string[2]
        for i in range(sum):
            possible_list.append(string[0])
    return possible_list
