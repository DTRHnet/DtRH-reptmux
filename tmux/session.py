#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: tmux/session.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

import subprocess
from hooks import hook_manager
from utils import get_current_state
import global_state

def create_tmux_session(session_name):
    hook_manager.run_hooks('before_function', 'create_tmux_session', session_name)
    try:
        subprocess.run(['tmux', 'new-session', '-d', '-s', session_name], check=True)
        global_state.current_session = session_name  # Update current session
        hook_manager.run_hooks('after_function', 'create_tmux_session', session_name)
    except subprocess.CalledProcessError as e:
        print(f"Error creating session '{session_name}': {e}")

def kill_tmux_session(session_name=None):
    session_name, _, _ = get_current_state(session_name)
    hook_manager.run_hooks('before_function', 'kill_tmux_session', session_name)
    try:
        subprocess.run(['tmux', 'kill-session', '-t', session_name], check=True)
        if global_state.current_session == session_name:
            global_state.current_session = None  # Reset current session if it was the one killed
        hook_manager.run_hooks('after_function', 'kill_tmux_session', session_name)
    except subprocess.CalledProcessError as e:
        print(f"Error killing session '{session_name}': {e}")


def list_tmux_sessions():
    """
    Lists all tmux sessions.

    Returns:
        list: List of tmux session names, or an empty list if no sessions are found or an error occurs.
    """
    try:
        result = subprocess.run(['tmux', 'list-sessions', '-F', '#S'], capture_output=True, text=True, check=True)
        sessions = result.stdout.strip().split('\n')
        return sessions if sessions != [''] else []
    except subprocess.CalledProcessError as e:
        print(f"Error listing sessions: {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []

def attach_tmux_session(session_name):
    """
    Attaches to an existing tmux session.

    Args:
        session_name (str): Name of the tmux session to attach to.
    """
    try:
        subprocess.run(['tmux', 'attach-session', '-t', session_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error attaching to session '{session_name}': {e}")

def rename_tmux_session(old_name, new_name):
    """
    Renames an existing tmux session.

    Args:
        old_name (str): Current name of the tmux session.
        new_name (str): New name for the tmux session.
    """
    try:
        subprocess.run(['tmux', 'rename-session', '-t', old_name, new_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error renaming session from '{old_name}' to '{new_name}': {e}")

def switch_tmux_session(session_name):
    """
    Switches to another tmux session.

    Args:
        session_name (str): Name of the tmux session to switch to.
    """
    try:
        subprocess.run(['tmux', 'switch-client', '-t', session_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error switching to session '{session_name}': {e}")

def has_session(session_name):
    """
    Checks if a tmux session exists.

    Args:
        session_name (str): Name of the tmux session to check.

    Returns:
        bool: True if the session exists, False otherwise.
    """
    try:
        result = subprocess.run(['tmux', 'has-session', '-t', session_name], capture_output=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False

def save_tmux_session_layout(session_name, layout_file):
    """
    Saves the layout of a tmux session to a file.

    Args:
        session_name (str): Name of the tmux session.
        layout_file (str): File to save the layout.
    """
    try:
        result = subprocess.run(['tmux', 'list-windows', '-t', session_name, '-F', '#{window_layout}'], capture_output=True, text=True, check=True)
        with open(layout_file, 'w') as f:
            f.write(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error saving layout for session '{session_name}': {e}")
    except IOError as e:
        print(f"File I/O error: {e}")

def restore_tmux_session_layout(session_name, layout_file):
    """
    Restores the layout of a tmux session from a file.

    Args:
        session_name (str): Name of the tmux session.
        layout_file (str): File to read the layout from.
    """
    try:
        with open(layout_file, 'r') as f:
            layout = f.read().strip()
        windows = layout.split("\n")
        for i, win_layout in enumerate(windows):
            subprocess.run(['tmux', 'select-layout', '-t', f'{session_name}:{i}', win_layout], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error restoring layout for session '{session_name}': {e}")
    except IOError as e:
        print(f"File I/O error: {e}")
    except IndexError as e:
        print(f"Index error: {e}")
