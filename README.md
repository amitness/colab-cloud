# colab-cloud [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1dIPSXtgOlXoWmiXSsukiLkpcqLAbZQ40?usp=sharing)

An experiment to have a resumable cloud workspace on Google Colab that persists all your settings and files across sessions.

![image](https://user-images.githubusercontent.com/8587189/232345088-c4542701-53ad-4c8b-9787-5e9f13491403.png)

There are are numerous improvements over the original approach we had [proposed](https://amitness.com/vscode-on-colab/) before:
1. Uses the RAM to store all the user settings and extensions for code-server. This makes the editor snappier compared to disk and reduces the startup time.
2. Uses Google Drive to persist the code editor settings across sessions
3. Uses a dedicated folder on Google Drive to store all the code files. The editor will resume with all your code files.
4. Uses [localtunnel](https://github.com/localtunnel/localtunnel) instead of ngrok for exposing the editor on web and allowing choice of custom subdomain.

## Usage

You can make a copy of this [notebook](https://colab.research.google.com/drive/1dIPSXtgOlXoWmiXSsukiLkpcqLAbZQ40?usp=sharing) and run it to get started.

Alternatively, on Colab, install the library
```bash
!pip install colabcloud -qqq
```

Then, run the code with a unique subdomain of your choice.
```python
from colabcloud import colabcloud

colabcloud(subdomain='example')
```

The editor can be accessed on your chosen URL e.g. [https://example.loca.lt](#).
