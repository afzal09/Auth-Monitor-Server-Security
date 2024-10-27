from Monitor import Monitor

log = "/var/log/auth.log"
email = 'email.txt' #os.path.join(os.path.abspath(''),'email.txt')
app = Monitor(log_file=log,mail=email)
app.main()