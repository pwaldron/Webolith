import multiprocessing

bind = "127.0.0.1:8000"
#workers = multiprocessing.cpu_count() * 2 + 1
workers = 3
pidfile = "/home/ubuntu/webolith/gunicorn.pid"
logfile = "/home/ubuntu/webolith/gunicorn.log"
worker_class = "sync"
timeout = 30
#daemon = True
#loglevel = "debug"
