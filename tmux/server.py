#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: tmux/server.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

import subprocess
import time
import global_state
from hooks import hook_manager

def check_tmux_server():
    """
    Checks if the tmux server is running.

    Returns:
        bool: True if the server is running, False otherwise.
    """
    try:
        result = subprocess.run(['tmux', 'info'], capture_output=True, text=True, check=True)
        return True if "tmux server is running" in result.stdout else False
    except subprocess.CalledProcessError:
        return False

def start_tmux_server():
    """
    Starts the tmux server if it is not already running and saves server information.
    """
    if global_state.tmux_server_info['is_running'] or check_tmux_server():
        global_state.tmux_server_info['is_running'] = True
        # The socket file path might need to be updated based on the actual environment
        global_state.tmux_server_info['socket_file'] = '/tmp/tmux-1000/default'
        global_state.tmux_server_info['time_created'] = time.strftime('%Y-%m-%d %H:%M:%S')
        print("Tmux server is already running.")
    else:
        hook_manager.run_hooks('before_function', 'start_tmux_server')
        try:
            # Starting a new tmux session to initialize the server
            subprocess.run(['tmux', 'start-server'], check=True)
            subprocess.run(['tmux', 'new-session', '-d', '-s', 'init_session'], check=True)
            
            # Save server information
            global_state.tmux_server_info['is_running'] = True
            global_state.tmux_server_info['socket_file'] = '/tmp/tmux-1000/default'
            global_state.tmux_server_info['time_created'] = time.strftime('%Y-%m-%d %H:%M:%S')
            hook_manager.run_hooks('after_function', 'start_tmux_server')
        except subprocess.CalledProcessError as e:
            print(f"Error starting tmux server: {e}")

def stop_tmux_server():
    """
    Stops the tmux server.
    """
    if check_tmux_server():
        hook_manager.run_hooks('before_function', 'stop_tmux_server')
        try:
            subprocess.run(['tmux', 'kill-server'], check=True)
            global_state.tmux_server_info['is_running'] = False
            global_state.tmux_server_info['socket_file'] = None
            global_state.tmux_server_info['time_created'] = None
            hook_manager.run_hooks('after_function', 'stop_tmux_server')
        except subprocess.CalledProcessError as e:
            print(f"Error stopping tmux server: {e}")
