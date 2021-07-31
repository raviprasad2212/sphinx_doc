from flask import Blueprint
import psycopg2
from werkzeug import exceptions

bikes = Blueprint('bike', __name__)

@bikes.route('/bikes/allinfo')
def showbikeinfo():
    """This method is used for to get bike information from avaliable database.\n

    Get http request.\n
    Connect database server.\n
    Write a query select query to get data from bikeinfo table.\n
    And store in the get_data variable.\n
    Return data as get_data in the dictionary format.\n

    Returns:
        json: {'data': data}
    """
    try:
        conn = psycopg2.connect(database='somedatabae', user='postgres', password='somepassword', port='5321')
        cur = conn.cursor()
        data = 'select * from bikeinfo'
        cur.execute(data)
        get_data = cur.fetchall()
        return {'data': get_data}

    except (Exception, psycopg2.DatabaseError) as error:
        return {'error': error}