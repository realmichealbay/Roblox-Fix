import os
import subprocess

SteamVr_Location = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SteamVR"
SteamVr1_Location = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SteamVR1"

home_dir = os.path.expanduser("~")
Roblox_Versions_Location = os.path.join(home_dir, "AppData\\Local\\Roblox\\Versions")

if os.path.exists(SteamVr_Location):
    os.rename(SteamVr_Location, SteamVr1_Location)
else:
    print(f"{SteamVr_Location} does not exist.")

# Search for RobloxPlayerBeta.exe in the Versions directory and its subdirectories
Roblox_Player_Location = None
for root, dirs, files in os.walk(Roblox_Versions_Location):
    if "RobloxPlayerBeta.exe" in files:
        Roblox_Player_Location = os.path.join(root, "RobloxPlayerBeta.exe")
        break

# Check if Roblox Player exists before trying to run it
if Roblox_Player_Location and os.path.exists(Roblox_Player_Location):
    # Start Roblox Player and do not wait for it to finish
    print(Roblox_Player_Location)
    process = subprocess.Popen(Roblox_Player_Location)

else:
    print(f"{Roblox_Player_Location} does not exist.")

# Wait for the Roblox Player process to finish
while process:
    try:
        if process.poll() is not None:
            break
    except OSError as e:
        if e.winerror == 6:  # The handle is invalid
            print("winerror detected")
            break
        else:
            raise


def Stop():
    if os.path.exists(SteamVr1_Location):
        os.rename(SteamVr1_Location, SteamVr_Location)
        print("Complete")
    else:
        print(f"{SteamVr1_Location} does not exist.")


Stop()
