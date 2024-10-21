from config import aws_config, database_config
from utils.aws.s3 import upload_to_s3

import psycopg2
import psycopg2.extras
import pandas as pd
import io
import csv



def get_data(branch_id, between, object_name):
    branch_id = branch_id
    start_date = between["start_date"]
    end_date = between["end_date"]

    conn = psycopg2.connect(
        host=database_config.host,
        port=database_config.port,
        dbname=database_config.database,
        user=database_config.user,
        password=database_config.password,
    )
    cur = conn.cursor()

    query = """
        SELECT
            p.id,
            p.camera_id,
            p.detection_time,
            p.label,
            p.confidence,
            ee.event_time,
            ee.event_type,
            g.gender,
            g.confidence AS gender_confidence,
            a.age_range,
            a.confidence AS age_confidence
        FROM
            "Person" p
        LEFT JOIN "EnterExit" ee ON p.id = ee.person_id
        LEFT JOIN "Gender" g ON p.id = g.person_id
        LEFT JOIN "Age" a ON p.id = a.person_id
        LEFT JOIN "Camera" c ON p.camera_id = c.id
        WHERE
            (%s is NULL OR c.branch_id = %s) AND
            (%s is NULL OR p.detection_time >= %s) AND
            (%s is NULL OR p.detection_time <= %s);
    """

    params = (branch_id, branch_id, start_date, start_date, end_date, end_date)
    cur.execute(query, params)
    rows = cur.fetchall()

    csv_buffer = io.StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow([i[0] for i in cur.description])
    csv_writer.writerows(rows)

    csv_buffer.seek(0)

    file_size = len(csv_buffer.getvalue())

    data_for_s3 = csv_buffer.getvalue()

    response = upload_to_s3(object_name, data_for_s3)

    cur.close()
    conn.close()

    return file_size, len(rows), response


def get_data_as_dataframe(branch_id, between):
    start_date = between["start_date"]
    end_date = between["end_date"]

    conn = psycopg2.connect(
        host=database_config.host,
        port=database_config.port,
        dbname=database_config.database,
        user=database_config.user,
        password=database_config.password,
    )

    query = """
        SELECT
            p.id,
            p.camera_id,
            p.detection_time,
            p.label,
            p.confidence,
            ee.event_time,
            ee.event_type,
            g.gender,
            g.confidence AS gender_confidence,
            a.age_range,
            a.confidence AS age_confidence
        FROM
            "Person" p
        LEFT JOIN "EnterExit" ee ON p.id = ee.person_id
        LEFT JOIN "Gender" g ON p.id = g.person_id
        LEFT JOIN "Age" a ON p.id = a.person_id
        LEFT JOIN "Camera" c ON p.camera_id = c.id
        WHERE
            (%s is NULL OR c.branch_id = %s) AND
            (%s is NULL OR p.detection_time >= %s) AND
            (%s is NULL OR p.detection_time <= %s);
    """

    params = (branch_id, branch_id, start_date, start_date, end_date, end_date)

    # Pandas read_sql_query method is used here
    df = pd.read_sql_query(query, conn, params=params)

    conn.close()

    return df

def get_data_as_dataframe_from_camera(branch_id, between, camera_id):
    start_date = between["start_date"]
    end_date = between["end_date"]

    conn = psycopg2.connect(
        host=database_config.host,
        port=database_config.port,
        dbname=database_config.database,
        user=database_config.user,
        password=database_config.password,
    )

    query = """
        SELECT
            p.id,
            p.camera_id,
            p.detection_time,
            p.label,
            p.confidence,
            ee.event_time,
            ee.event_type,
            g.gender,
            g.confidence AS gender_confidence,
            a.age_range,
            a.confidence AS age_confidence
        FROM
            "Person" p
        LEFT JOIN "EnterExit" ee ON p.id = ee.person_id
        LEFT JOIN "Gender" g ON p.id = g.person_id
        LEFT JOIN "Age" a ON p.id = a.person_id
        LEFT JOIN "Camera" c ON p.camera_id = c.id
        WHERE
            (%s is NULL OR p.camera_id = %s) AND
            (%s is NULL OR c.branch_id = %s) AND
            (%s is NULL OR p.detection_time >= %s) AND
            (%s is NULL OR p.detection_time <= %s);
    """

    params = (camera_id,camera_id, branch_id, branch_id, start_date, start_date, end_date, end_date)

    # Pandas read_sql_query method is used here
    df = pd.read_sql_query(query, conn, params=params)

    conn.close()

    return df

def get_camera_as_dataframe(branch_id):

    conn = psycopg2.connect(
        host=database_config.host,
        port=database_config.port,
        dbname=database_config.database,
        user=database_config.user,
        password=database_config.password,
    )

    query = f'SELECT * FROM "Camera" WHERE branch_id = {branch_id}';

    # Pandas read_sql_query method is used here
    df = pd.read_sql_query(query, conn)

    conn.close()

    return df







def get_branch_by_id(branch_id):
    try:
        conn = psycopg2.connect(
            host=database_config.host,
            port=database_config.port,
            dbname=database_config.database,
            user=database_config.user,
            password=database_config.password,
        )

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        query = """SELECT * FROM "Branch" WHERE id = %s;"""

        cur.execute(query, (branch_id,))

        row = cur.fetchone()

        if row is None:
            return {}
        result = dict(row)

        cur.close()
        conn.close()

        return result

    except Exception as e:
        print("Veritabanından veri çekme sırasında bir hata oluştu:", e)
        if conn:
            conn.close()
        return None





