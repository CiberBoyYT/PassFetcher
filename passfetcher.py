import subprocess
import re

def get_wifi_passwords():
    try:
        #get saved wifi profile
        result = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
        profiles = re.findall(r"All User Profile\s*: (.+)", result.stdout)
        if not profiles:
            print("no saved wifi profile found.")
            return

        print("\nretrieving wifi passwords, please wait......\n")
        for profile in profiles:
            #get wifi password for each profile
            result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True)
            password = re.search(r"Key Content\s*: (.+)", result.stdout)
            print(f"network connection: {profile.strip()}")
            print(f"passowrd: {password.group(1) if password else 'Not found'}\n{'-'*40}")

    except Exception as e:
        print(f"error has ocurred: {e}")
if __name__ == "__main__":
    get_wifi_passwords()
