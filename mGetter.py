import asyncio, sqlite3, os, random
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
async def getTable() -> list:
    conn = sqlite3.connect(constPaths.db_paths["banner_prizes"], check_same_thread = False)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM possible_prizes WHERE quantity > 0")
    exists = cursor.fetchall()
    cursor.close(); conn.close()
    return exists

# возвращает список для выбора в рулетке
async def getBannerResult() -> list:
    firstly = await getTable()
    possible_list = list()
    for string in firstly:
        sum = string[3] * string[2]
        for i in range(sum):
            possible_list.append(string[0])
    
    if (len(possible_list) == 0):
        return 0
    return random.choice(possible_list)

# возвращает инвентарь пользователя
async def getUserInventory(user_id: int) -> list:
    connection = sqlite3.connect(
        constPaths.db_paths["user_drops"],
        check_same_thread = False
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM '{user_id}' WHERE quantity > 0 AND id > 0")
    item_list = cursor.fetchall()
    cursor.close(); connection.close()
    return item_list

# вывод доступных предметов баннера художников
async def getArtBannerDrop() -> list:
    connection = sqlite3.connect(
        constPaths.db_paths["banner_prizes"],
        check_same_thread = False
    )
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM possible_prizes WHERE quantity > 0 AND weight != 0")
    item_list = cursor.fetchall()
    cursor.close(); connection.close()
    return item_list