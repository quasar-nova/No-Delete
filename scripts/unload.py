from subprocess import check_output as CO
import os
import psutil
import logging as logger
logger.basicConfig(format="[ejector] %(levelname)s %(message)s", level=logger.INFO)

logger.info("Needs Injector.exe from: https://github.com/nefarius/Injector to run")

def unload_file_from_process(pid, filename):
    cmd = ("Injector", "-e", "-p", f"{pid}", f"{filename}")
    try: 
        out = CO(cmd)
        if b'Could not find' in out:
            logger.info(f"{filename} is not present in explorer.exe:{pid}")
        else:
            logger.info(f"ejected {filename} from explorer.exe:{pid}")
    except Exception as e:
        logger.error(f"ejecting {filename} from {pid} failed with {e}")

files = (
    r".\builddir\NoDeleteH.dll",
    r".\builddir_release\NoDeleteH.dll",
)

def find_process_by_name(process_name):
    pids = []
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name in proc.info['name']:
            pids.append(proc.info['pid'])
    return pids

for p in find_process_by_name('explorer.exe'):
    for f in files:
        unload_file_from_process(p, f)
