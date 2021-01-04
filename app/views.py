from flask import Flask , render_template , redirect , url_for ,request
import sqlite3
from flask.helpers import send_file
from app.helper_func import *
from app.forms import DBAction
import logging

logger = logging.getLogger('Hits_Count')

logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('log/app.log')
fh.setLevel(logging.INFO)

formatter = logging.Formatter("Time: %(asctime)s | Level:%(levelname)s | MSG:%(message)s","%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)
logger.addHandler(fh)

app = Flask(__name__)

@app.route('/', methods=["GET" , "POST"])
def hello():
    database = ('database.db')
    conn = create_connection(database)
    reset_hits = DBAction()
    if request.method == "POST":
        if reset_hits.reset_hit_count.data:
            hits_counter = select_hits_count(conn)[0]
            reset_hit_count(conn)
            logger.info('The reset button was pressed from IP:' + request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
                        + ' After it was hit ' + str(hits_counter) + ' times' )
            return redirect(url_for('hello'))
    update_value(conn, '1')
    hits_counter = select_hits_count(conn)[0]
    return render_template('index.html', hits_counter=hits_counter,form=reset_hits)

