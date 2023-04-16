import json
import subprocess
from importlib import import_module
from pathlib import Path
import uuid

default_settings = {
    "jupyter.useDefaultConfigForJupyter": False,
    "jupyter.askForKernelRestart": False,
    "jupyter.debugJustMyCode": False
}


def run_foreground(cmd: str) -> None:
    """
    Run a bash command in foreground.

    Reference: http://blog.kagesenshi.org/2008/02/teeing-python-subprocesspopen-output.html

    Args:
        cmd: Bash command

    Returns:
        None
    """
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    while True:
        line = p.stdout.readline()
        print(line.strip())
        if line == "" and p.poll() is not None:
            break
    return None


def run(command: str) -> None:
    process = subprocess.run(command.split())
    if process.returncode == 0:
        print(f"Ran: {command}")
        
def colabcloud(
    subdomain: str = str(uuid.uuid4()),
    port: int = 9000
) -> None:
    """
    Start code-server with persistence of settings and code.

    Args:
        subdomain: Subdomain for localtunnel.
        port: Port for running code-server

    Returns:
        None
    """
    print("Mounting Google Drive...")
    drive = import_module("google.colab.drive")
    drive.mount("/content/drive")
    
    print("Installing python libraries...")
    run("pip3 install --user flake8 black ipywidgets")
    run("pip3 install -U ipykernel")
    run("sudo apt install htop -y")
    
    
    print("Installing code-server...")
    run("curl -fsSL https://code-server.dev/install.sh -O")
    run("bash install.sh --version 4.9.1")

    # Remap code-server config path to use RAM for storing settings and extensions
    user_data_dir: str = "/dev/shm/.vscode"
    Path(user_data_dir).mkdir(exist_ok=True)
    

    # Install python and jupyter extensions for code-server
    extensions = ["ms-python.python"]
    for extension in extensions:
        run(f"code-server --install-extension {extension} --user-data-dir {user_data_dir}")
    
    # Symlink settings in drive to code-server
    drive_path = '/content/drive/MyDrive/colab'
    Path(f'{drive_path}/.vscode-settings/').mkdir(parents=True, exist_ok=True)
    if not Path(f'{drive_path}/.vscode-settings/settings.json').exists():
        with open(f'{drive_path}/.vscode-settings/settings.json', 'w') as f:
            json.dump(default_settings, f)
    Path('/dev/shm/.vscode/User/settings.json').unlink(missing_ok=True)
    run(f'ln -s {drive_path}/.vscode-settings/settings.json {user_data_dir}/User/settings.json')

    # Start code-server pointing to the colab folder in drive
    print("\n\nAccess the code editor at the following URL:")
    print(f"https://{subdomain}.loca.lt/?folder={drive_path}\n\n")
    run_foreground(
        f"code-server --port {port} --host localhost --auth none --disable-telemetry --force --user-data-dir {user_data_dir} & npx localtunnel -p {port} -s {subdomain} --allow-invalid-cert"
    )