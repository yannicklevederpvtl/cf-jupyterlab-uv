c = get_config()
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = int(os.environ.get('PORT', 8888))
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.allow_origin = '*'