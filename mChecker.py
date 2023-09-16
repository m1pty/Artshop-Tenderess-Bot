import os, sqlite3, asyncio
import constPaths # пути до основных файлов

# проверка на наличие аккаунта в списке пользователей бота
async def checkAccountExistance(user_id: int) -> bool:
    balance_db = constPaths.db_paths["balance"]
    connection = sqlite3.connect(balance_db)
    cursor = connection.cursor()
    parameters = f"SELECT balance FROM balanceTable WHERE user_id = {user_id}"
    
    balance = cursor.execute(parameters)
    balance = balance.fetchone()
    cursor.close(); connection.close()
    return False if (balance is None) else True

async def checkPrize(text) -> None:
    conn = sqlite3.connect(constPaths.db_paths["banner_prizes"], check_same_thread = False)
    cursor = conn.cursor()
    cursor.execute(f"SELECT quantity FROM possible_prizes WHERE name = {text}")
    number = int(cursor.fetchall())
    if number == 1:
        cursor.execute(f"DELETE FROM possible_prizes WHERE name = {text}")
        conn.commit
    else:
        cursor.execute(f"UPDATE possible_prizes SET quantity = {number - 1} WHERE name = {text}")
        conn.commit
    cursor.close()
    conn.close()