import subprocess
def openApp(q):
    if('spotify' in q):
        application_name = 'spotify.exe'
    elif('notepad' in q):
        application_name = "notepad.exe"
    elif('chrome' in q):
        application_name = "chrome.exe"
    elif('command' in q or 'cmd' in q):
        application_name = "cmd.exe"

    try:
        subprocess.Popen(application_name)
        print(f"Opened {application_name} successfully.")
    except FileNotFoundError:
        print(f"Error: {application_name} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
