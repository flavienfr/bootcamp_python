import getpass
import time

global start

def log(func):
	def log_write(*args, **kwargs):
		ret = func(*args, **kwargs)
		global start
		if func.__name__ == 'start_machine':
			start = time.time()
		f = open("machine.log","a+")
		msg = '(' + getpass.getuser() + ')'
		f.write(msg)
		f.write('Running: ')
		f.write(func.__name__)
		f.write('        ')
		msg = '[ exec-time = '
		if (time.time() - start) < 1:
			ms = round((time.time() - start) * 1000, 3)
			msg += str(ms) + ' ms ]'
		else:
			ms = round((time.time() - start), 3)
			msg += str(ms) + ' s ]'
		f.write(msg)
		f.write('\n')
		f.close()
		return ret
	return log_write