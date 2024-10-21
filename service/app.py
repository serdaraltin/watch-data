
from app import app


if __name__ == '__main__':
     # app.run(debug=True, host="0.0.0.0", port=3002)
    
# from config import aws_config, database_config

# import psycopg2
# import psycopg2.extras

# def get_branch_by_id(branch_id):
#     try:
#         conn = psycopg2.connect(
#             host=database_config.host,
#             port=database_config.port,
#             dbname=database_config.database,
#             user=database_config.user,
#             password=database_config.password,
#         )

#         cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

#         query = """SELECT * FROM "Branch" WHERE id = %s;"""

#         cur.execute(query, (branch_id,))

#         row = cur.fetchone()

#         if row is None:
#             return {}
#         result = dict(row)

#         cur.close()
#         conn.close()

#         return result

#     except Exception as e:
#         print("Veritabanından veri çekme sırasında bir hata oluştu:", e)
#         if conn:
#             conn.close()
#         return None

# data = get_branch_by_id(1)
# print(data["name"])
