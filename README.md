# JupyterLab on Tanzu Platform for Cloud Foundry with uv

Deploy JupyterLab as a web application on Tanzu Platform for Cloud Foundry with this simple configuration.

## 📋 Prerequisites

- Cloud Foundry CLI installed
- Access to a Tanzu Platform for Cloud Foundry environment
- Git (for cloning this repository)
- (optional) GenAI tile

## 🚀 Quick Start

1. **Clone this repository**
   ```bash
   git clone https://github.com/yannicklevederpvtl/cf-jupyterlab-uv
   cd cf-jupyterlab-uv
   ```

2. **Deploy to Tanzu Platform for Cloud Foundry**
   ```bash
   cf push
   ```

3. **Access your JupyterLab**
   - Check the route in your terminal output after deployment
   - Open the URL in your browser
   - Start coding in JupyterLab!

4. **Notebook sample**
   - Bind your genai chat service named "chat-llm" to your Jupyterlab app (or edit the nobebook accordingly)
    ```bash
   cf bind-service cf-jupyterlab-uv chat-llm
   cf restage cf-jupyterlab-uv
    ```
    - Open and use the nbsample notebook in Jupyterlab

5. **more advanced Notebook samples**
   
   - Use Git within JupyterLab to git clone this samples repo
   ```bash
   git clone https://github.com/kirtiapte/cf-jupyterlab-samples
   ```
   Edit `pyproject.toml` with the dependencies prior `CF push` or add these dependencies within JupyterLab terminal using `uv pip install <package>`
   

## 📁 Project Structure

```
├── pyproject.toml                # Python dependencies
├── jupyter_notebook_config.py    # JupyterLab configuration
├── manifest.yml                  # Cloud Foundry deployment settings
├── nbsample.jpynb                # Notebook sample with GenAI for TPCF 
└── README.md                     # This file
```

## ⚙️ Configuration

### Resource Allocation
- **Memory**: 2GB (configurable in `manifest.yml`)
- **Disk**: 4GB (configurable in `manifest.yml`)
- **Instances**: 1 

### Python Packages
Default packages included:
- JupyterLab 4.2.5
- jupyterlab-git 0.51.2
- notebook
- ipykernel
- python-dotenv
- ipywidgets
- requests
- openai
- langchain
- langchain-openai
- langchain_experimental
- langchain_chroma
- langchain[docarray]
- datasets
- matplotlib
- unstructured
- modal
- ollama

Add more packages to `pyproject.toml` as needed.

### Security Settings
⚠️ **Important**: This configuration disables authentication for simplicity. For production use, enable security features.

## 🔧 Customization

### Adding Python Packages
Edit `pyproject.toml`:
```
jupyterlab==4.2.5
your-package==1.0.0
another-package
```

or use command in a JupyterLab Terminal
```
uv pip add <package>
```

### Changing Memory/Disk
Edit `manifest.yml`:
```yaml
applications:
- name: cf-jupyterlab-uv
  memory: 2G        # Increase memory
  disk_quota: 4G    # Increase disk space
```

### Custom Domain
Edit `manifest.yml` routes section:
```yaml
routes:
  - route: jupyterlab.yourdomain.com
```

### Enable Authentication
Edit `jupyter_notebook_config.py`:
```python
# Set a token
c.NotebookApp.token = 'your-secure-token'

# Or set a password hash
c.NotebookApp.password = 'sha1:your-hashed-password'
```

## 🔒 Security Considerations

**For Production Use:**
1. Enable authentication (token or password)
2. Restrict allowed origins
3. Use HTTPS routes
4. Consider network policies
5. Regular security updates

Example secure configuration:
```python
c.NotebookApp.token = os.environ.get('JUPYTER_TOKEN', 'default-token')
c.NotebookApp.allow_origin = 'https://yourdomain.com'
```

## 💾 Data Persistence

⚠️ **Important**: Cloud Foundry applications are ephemeral. Notebooks and data will be lost when the app restarts.

**Solutions for data persistence:**
1. **Version Control**: Commit notebooks to git regularly
2. **Volume Services**: Bind persistent storage services
3. **External Storage**: Use cloud storage APIs (S3, GCS, etc.)

### Example with Volume Service
```yaml
# In manifest.yml
services:
  - my-llm-service
```

## 🐛 Troubleshooting

### Common Issues


**Application won't start**
- Check memory allocation (increase if needed)
- Verify Python version in `pyproject.toml`
- Check application logs: `cf logs cf-jupyterlab --recent`

**Can't access JupyterLab**
- Verify the route is correct
- Check if app is running: `cf apps`
- Review health check settings

### Debugging Commands
```bash
# Check application status
cf apps

# View recent logs
cf logs cf-jupyterlab-uv --recent

# SSH into the container (if enabled)
cf ssh cf-jupyterlab-uv

# Check environment variables
cf env cf-jupyterlab-uv
```

## 🔄 Updates

To update your deployment:
1. Make changes to your files
2. Run `cf push` again
3. Cloud Foundry will handle the update with zero downtime

## 📚 Additional Resources

- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test deployment
5. Submit a pull request
