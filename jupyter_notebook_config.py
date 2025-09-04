import os

c = get_config()

# Basic JupyterLab settings
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = int(os.environ.get('PORT', 8888))
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.allow_origin = '*'

# Basic collaboration settings - Let the extension handle these automatically
c.ServerApp.disable_check_xsrf = True
c.ServerApp.allow_remote_access = True

# JupyterLab specific collaboration settings
c.ServerApp.jpserver_extensions = {
    'jupyter_server_ydoc': True,
}