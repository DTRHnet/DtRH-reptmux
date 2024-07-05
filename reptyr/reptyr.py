#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: reptyr/reptyr.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >


import subprocess
from hooks import hook_manager
from utils import get_current_state

def reattach_process_to_tmux_pane(pid, session_name=None, window_index=None, pane_index=None):
    """
    Reattaches a process to a specific tmux pane using reptyr.

    Args:
        pid (int): Process ID to reattach.
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the tmux pane.
    """
    session_name, window_index, pane_index = get_current_state(session_name, window_index, pane_index)
    tmux_pane = f'{session_name}:{window_index}.{pane_index}'
    hook_manager.run_hooks('before_function', 'reattach_process_to_tmux_pane', pid, session_name, window_index, pane_index)
    try:
        subprocess.run(['reptyr', '-T', tmux_pane, str(pid)], check=True)
        hook_manager.run_hooks('after_function', 'reattach_process_to_tmux_pane', pid, session_name, window_index, pane_index)
    except subprocess.CalledProcessError as e:
        print(f"Error reattaching process {pid} to tmux pane {pane_index} in window {window_index} of session '{session_name}': {e}")

def reattach_process_to_terminal(pid, terminal):
    """
    Reattaches a process to a specific terminal using reptyr.

    Args:
        pid (int): Process ID to reattach.
        terminal (str): Terminal to reattach the process to (e.g., '/dev/pts/1').
    """
    hook_manager.run_hooks('before_function', 'reattach_process_to_terminal', pid, terminal)
    try:
        subprocess.run(['reptyr', '-T', terminal, str(pid)], check=True)
        hook_manager.run_hooks('after_function', 'reattach_process_to_terminal', pid, terminal)
    except subprocess.CalledProcessError as e:
        print(f"Error reattaching process {pid} to terminal '{terminal}': {e}")

def list_reptyr_pids():
    """
    Lists all process IDs that are managed by reptyr.

    Returns:
        list: List of process IDs, or an empty list if no processes are found or an error occurs.
    """
    hook_manager.run_hooks('before_function', 'list_reptyr_pids')
    try:
        result = subprocess.run(['ps', '-e', '-o', 'pid,command'], capture_output=True, text=True, check=True)
        pids = []
        for line in result.stdout.splitlines()[1:]:  # Skip header line
            pid, command = line.strip().split(' ', 1)
            if 'reptyr' in command:
                pids.append(int(pid))
        hook_manager.run_hooks('after_function', 'list_reptyr_pids', pids)
        return pids
    except subprocess.CalledProcessError as e:
        print(f"Error listing reptyr-managed process IDs: {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []

def is_process_attached(pid):
    """
    Checks if a process is attached using reptyr.

    Args:
        pid (int): Process ID to check.

    Returns:
        bool: True if the process is attached, False otherwise.
    """
    hook_manager.run_hooks('before_function', 'is_process_attached', pid)
    try:
        result = subprocess.run(['ps', '-p', str(pid), '-o', 'comm='], capture_output=True, text=True, check=True)
        attached = 'reptyr' in result.stdout.strip()
        hook_manager.run_hooks('after_function', 'is_process_attached', pid, attached)
        return attached
    except subprocess.CalledProcessError as e:
        print(f"Error checking if process {pid} is attached: {e}")
        return False

def detach_process(pid):
    """
    Detaches a process from its current terminal or tmux pane.

    Args:
        pid (int): Process ID to detach.
    """
    hook_manager.run_hooks('before_function', 'detach_process', pid)
    try:
        # Note: reptyr doesn't provide a direct detach command, so this function might just kill the reptyr process
        subprocess.run(['kill', str(pid)], check=True)
        hook_manager.run_hooks('after_function', 'detach_process', pid)
    except subprocess.CalledProcessError as e:
        print(f"Error detaching process {pid}: {e}")

def move_process_to_tmux_pane(pid, session_name=None, window_index=None, pane_index=None):
    """
    Moves a process to a different tmux pane.

    Args:
        pid (int): Process ID to move.
        session_name (str): Name of the target tmux session.
        window_index (int): Index of the target tmux window.
        pane_index (int): Index of the target tmux pane.
    """
    session_name, window_index, pane_index = get_current_state(session_name, window_index, pane_index)
    hook_manager.run_hooks('before_function', 'move_process_to_tmux_pane', pid, session_name, window_index, pane_index)
    try:
        detach_process(pid)
        reattach_process_to_tmux_pane(pid, session_name, window_index, pane_index)
        hook_manager.run_hooks('after_function', 'move_process_to_tmux_pane', pid, session_name, window_index, pane_index)
    except Exception as e:
        print(f"Error moving process {pid} to tmux pane {pane_index} in window {window_index} of session '{session_name}': {e}")

def reattach_process_with_env(pid, terminal, env_vars):
    """
    Reattaches a process to a terminal with specific environment variables.

    Args:
        pid (int): Process ID to reattach.
        terminal (str): Terminal to reattach the process to (e.g., '/dev/pts/1').
        env_vars (dict): Dictionary of environment variables to set.
    """
    hook_manager.run_hooks('before_function', 'reattach_process_with_env', pid, terminal, env_vars)
    try:
        env_command = ' '.join([f'{key}={value}' for key, value in env_vars.items()])
        subprocess.run(['reptyr', '-T', terminal, '-E', env_command, str(pid)], check=True)
        hook_manager.run_hooks('after_function', 'reattach_process_with_env', pid, terminal, env_vars)
    except subprocess.CalledProcessError as e:
        print(f"Error reattaching process {pid} to terminal '{terminal}' with environment variables {env_vars}: {e}")

def list_process_ids_and_names():
    """
    Lists all process IDs and their corresponding process names.

    Returns:
        list: List of tuples containing process IDs and process names, or an empty list if an error occurs.
    """
    hook_manager.run_hooks('before_function', 'list_process_ids_and_names')
    try:
        result = subprocess.run(['ps', '-e', '-o', 'pid,comm'], capture_output=True, text=True, check=True)
        processes = []
        for line in result.stdout.splitlines()[1:]:
            pid, command = line.strip().split(None, 1)
            processes.append((int(pid), command))
        hook_manager.run_hooks('after_function', 'list_process_ids_and_names', processes)
        return processes
    except subprocess.CalledProcessError as e:
        print(f"Error listing process IDs and names: {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []
