import time
from zk import ZK, const
from pymitter import EventEmitter
from models import Attendance_Logs
from config import DEVICE_IP, DEVICE_PORT, DEVICE_TIMEOUT
import redis
import json

ee = EventEmitter()
conn = None
zk = ZK(DEVICE_IP, DEVICE_PORT, DEVICE_TIMEOUT)
# conn = zk.connect()

# make listener from event attendace_log_available
@ee.on("attendace_log_available")
# handle function of event attendace_log_available
def handle_attendace_log_available(data):
    # loop list data
    for user in data:
        # storing to the database
        user_id = user.user_id
        timestamp = user.timestamp

        store = Attendance_Logs( user_id=user_id, time=timestamp )
        store.save()
        print "  ---> {} - {}".format(user_id, timestamp)

def check():
    try:
        conn = zk.connect()
        attendaces = conn.get_attendance()

        # if have no data
        if not attendaces:
            print "no data"
        
        # if have data
        else:
            print "{} data found".format(len(attendaces))
            #emit event to attendace_log_available
            ee.emit("attendace_log_available", attendaces)
            
            #always clear when success inserting to database
            conn.clear_attendance()

        #disconnect device
        # conn.disconnect()
    except Exception, e:
        print "Process terminate : {}".format(e)


def handler(msg):
    if msg['data'] != 1:
        data = json.loads(msg['data'])

        try:
            ZK2 = ZK(data['ip'], data['port'], DEVICE_TIMEOUT)
            conn2 = ZK2.connect()
            conn2.test_voice()
            print "machine ip = {}, test voice ->> success".format(data['ip'])
        except Exception, e:
            print e

def main():

    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    p = r.pubsub()
    p.subscribe('@machine/test_voice')

    while True:
        msg = p.get_message()
        if msg:
            handler(msg)

    # infinite loop
    # while True:
    #     check()

    #     # sleeptime : 1s
    #     time.sleep(1)

if __name__ == "__main__":
    main()
