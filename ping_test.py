import subprocess

host = "8.8.8.8"
result = subprocess.run(["ping", "-c", "4", host]. capture_output=True, text=True)
print(result.stdout)

