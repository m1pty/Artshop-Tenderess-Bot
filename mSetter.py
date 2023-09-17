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

# инициализация пустой таблицы для призов пользователя
async def setNewUserDrop(user_id: int) -> None:
    user_drop_db = constPaths.db_paths["user_drops"]
    connection = sqlite3.connect(user_drop_db)
    cursor = connection.cursor()

    parameters = f"""CREATE TABLE IF NOT EXISTS '{user_id}'(
        id INT PRIMARY KEY UNIQUE, 
        name TEXT, 
        quantity INT);
    """
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
async def setBannerDropQuantity(drop_id: int) -> None:
    drop_db = constPaths.db_paths["banner_prizes"]
    connection = sqlite3.connect(drop_db)
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT quantity FROM possible_prizes WHERE id = {drop_id}")
    quantity = (cursor.fetchall())[0][0]

    parameters = f"UPDATE possible_prizes SET quantity = {quantity - 1} WHERE id = {drop_id}"
    cursor.execute(parameters)
    connection.commit()
    cursor.close(); connection.close()

# внесение дропа в БД пользователя (любой баннер)
async def setUserArtistDropById(user_id: int, drop_id: int):
    drop_db = constPaths.db_paths["user_drops"]
    connection = sqlite3.connect(drop_db)
    cursor = connection.cursor()
    
    # получаем имя приза из другой таблицы
    possible_drop_db = constPaths.db_paths["banner_prizes"]
    connection2 = sqlite3.connect(possible_drop_db)
    cursor2 = connection2.cursor()
    cursor2.execute(f"SELECT name FROM possible_prizes WHERE id = {drop_id}")
    name = str(cursor2.fetchall()[0][0])
    cursor2.close()
    connection2.close()

    # получаем кол-во призов такого типа у пользователя
    get_parameters = "SELECT * FROM \'" + str(user_id) + "\'"
    cursor.execute(get_parameters)
    fetchall_try = list(cursor.fetchall())

    quantity = -1
    for element in fetchall_try:
        if (element[0] == drop_id):
            quantity = element[2]
            break

    # такого приза ещё не было, добавляем новый
    if (quantity == -1):
        cursor.execute(f"INSERT INTO '{user_id}' (id, name, quantity) VALUES ({drop_id}, '{name}', 1)")
        connection.commit()
    # увеличиваем кол-во призов данного типа у пользователя
    else:
        cursor.execute(f"UPDATE '{user_id}' SET quantity = {quantity + 1} WHERE id = {drop_id}")
        connection.commit()
    cursor.close(); connection.close()