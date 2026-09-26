import json
import subprocess
import os

# Check if gitdoc extension is installed and can be activated
ext_path = os.path.expanduser("~/.vscode/extensions/vsls-contrib.gitdoc-0.2.3")
if os.path.exists(ext_path):
    print(f"Extension found at: {ext_path}")
    package_json = os.path.join(ext_path, "package.json")
    if os.path.exists(package_json):
        with open(package_json) as f:
            pkg = json.load(f)
        print(f"Extension name: {pkg.get('name')}")
        print(f"Version: {pkg.get('version')}")
        print(f"Activation events: {pkg.get('activationEvents')}")
        print(f"Main: {pkg.get('main')}")
else:
    print("Extension not found in ~/.vscode/extensions")
    # Check other locations
    for base in ["/usr/share/code/extensions", "/opt/visual-studio-code/extensions", "/home/hardik-sankhla/.vscode-server/extensions"]:
        for root, dirs, files in os.walk(base):
            for d in dirs:
                if "gitdoc" in d.lower():
                    print(f"Found at: {os.path.join(root, d)}")

