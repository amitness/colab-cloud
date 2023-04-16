# colab-cloud [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dIPSXtgOlXoWmiXSsukiLkpcqLAbZQ40?usp=sharing)

An experiment to have a resumable code editor on Google Colab that persists all your settings and files across sessions.

There are are numerous improvements over the original approach we had [proposed](https://amitness.com/vscode-on-colab/) before:
1. Use the RAM to store all the user settings and extensions for code-server. This reduces the startup time for the editor compared to disk.
2. Use Google Drive to persist the settings for VSCode across sessions
3. Use a dedicated folder on Google Drive to store all the code files. The editor will resume with the files you had last opened.
4. Use [localtunnel](https://github.com/localtunnel/localtunnel) instead of ngrok for unlimited bandwidth and removing requirement for an account

## Usage

You can make a copy of this [notebook](https://colab.research.google.com/drive/1dIPSXtgOlXoWmiXSsukiLkpcqLAbZQ40?usp=sharing) and run the code to get started.

On Colab, install the library
```bash
!pip install git+https://github.com/amitness/colab-cloud -qqq
```

Then, run the code with a unique subdomain of your choice.
```python
from colabcloud import colabcloud

colabcloud(subdomain='example')
```

The editor can be accessed on your chosen URL e.g. [https://example.loca.lt](#).