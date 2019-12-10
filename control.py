import switch
import data
import datetime

HOME_DIR = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
LOG_FILE = HOME_DIR + "log.log"

print(LOG_FILE)

while True:
	t, h = data.get_temperature_humidity()
	print(t, h)