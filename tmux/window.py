import subprocess

def create_tmux_window(session_name, window_name):
    """
    Creates a new window in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_name (str): Name of the new window.
    """
    try:
        subprocess.run(['tmux', 'new-window', '-t', session_name, '-n', window_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error creating window '{window_name}' in session '{session_name}': {e}")

def kill_tmux_window(session_name, window_index):
    """
    Kills a window in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to kill.
    """
    try:
        subprocess.run(['tmux', 'kill-window', '-t', f'{session_name}:{window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error killing window {window_index} in session '{session_name}': {e}")

def list_tmux_windows(session_name):
    """
    Lists all windows in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.

    Returns:
        list: List of tmux window indexes, or an empty list if no windows are found or an error occurs.
    """
    try:
        result = subprocess.run(['tmux', 'list-windows', '-t', session_name, '-F', '#I'], capture_output=True, text=True, check=True)
        windows = result.stdout.strip().split('\n')
        return windows if windows != [''] else []
    except subprocess.CalledProcessError as e:
        print(f"Error listing windows in session '{session_name}': {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []

def rename_tmux_window(session_name, window_index, new_name):
    """
    Renames an existing window in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to rename.
        new_name (str): New name for the window.
    """
    try:
        subprocess.run(['tmux', 'rename-window', '-t', f'{session_name}:{window_index}', new_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error renaming window {window_index} in session '{session_name}' to '{new_name}': {e}")

def select_tmux_window(session_name, window_index):
    """
    Selects a window in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to select.
    """
    try:
        subprocess.run(['tmux', 'select-window', '-t', f'{session_name}:{window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error selecting window {window_index} in session '{session_name}': {e}")

def split_tmux_window(session_name, window_index, direction='h'):
    """
    Splits a window in the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to split.
        direction (str): Direction to split the window ('h' for horizontal, 'v' for vertical).
    """
    direction_flag = '-h' if direction == 'h' else '-v'
    try:
        subprocess.run(['tmux', 'split-window', direction_flag, '-t', f'{session_name}:{window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error splitting window {window_index} in session '{session_name}' in direction '{direction}': {e}")

def move_window(session_name, window_index, target_index):
    """
    Moves a window to a new position within the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to move.
        target_index (int): New position for the window.
    """
    try:
        subprocess.run(['tmux', 'move-window', '-s', f'{session_name}:{window_index}', '-t', f'{session_name}:{target_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error moving window {window_index} to position {target_index} in session '{session_name}': {e}")

def link_window(session_name, window_index, target_session):
    """
    Links a window to another session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to link.
        target_session (str): Name of the target session.
    """
    try:
        subprocess.run(['tmux', 'link-window', '-s', f'{session_name}:{window_index}', '-t', target_session], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error linking window {window_index} from session '{session_name}' to target session '{target_session}': {e}")

def unlink_window(session_name, window_index):
    """
    Unlinks a window from its current session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the window to unlink.
    """
    try:
        subprocess.run(['tmux', 'unlink-window', '-t', f'{session_name}:{window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error unlinking window {window_index} in session '{session_name}': {e}")
