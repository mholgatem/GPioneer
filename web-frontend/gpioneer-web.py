[program:gpioneer-web]
command=sudo python app.py
autostart=true
autorestart=unexpected
stderr_logfile=/var/log/long.err.log
stdout_logfile=/var/log/long.out.log