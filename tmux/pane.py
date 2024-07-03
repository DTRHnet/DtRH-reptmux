import subprocess

def split_tmux_pane(session_name, window_index, direction='h'):
    """
    Splits a pane in the specified tmux window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        direction (str): Direction to split the pane ('h' for horizontal, 'v' for vertical).
    """
    direction_flag = '-h' if direction == 'h' else '-v'
    try:
        subprocess.run(['tmux', 'split-window', direction_flag, '-t', f'{session_name}:{window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error splitting pane in window {window_index} of session '{session_name}' in direction '{direction}': {e}")

def kill_tmux_pane(session_name, window_index, pane_index):
    """
    Kills a pane in the specified tmux window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the pane to kill.
    """
    try:
        subprocess.run(['tmux', 'kill-pane', '-t', f'{session_name}:{window_index}.{pane_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error killing pane {pane_index} in window {window_index} of session '{session_name}': {e}")

def list_tmux_panes(session_name, window_index):
    """
    Lists all panes in the specified tmux window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.

    Returns:
        list: List of tmux pane indexes, or an empty list if no panes are found or an error occurs.
    """
    try:
        result = subprocess.run(['tmux', 'list-panes', '-t', f'{session_name}:{window_index}', '-F', '#P'], capture_output=True, text=True, check=True)
        panes = result.stdout.strip().split('\n')
        return panes if panes != [''] else []
    except subprocess.CalledProcessError as e:
        print(f"Error listing panes in window {window_index} of session '{session_name}': {e}")
        return []
    except TypeError as e:
        print(f"Type error: {e}")
        return []

def select_tmux_pane(session_name, window_index, pane_index):
    """
    Selects a pane in the specified tmux window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the pane to select.
    """
    try:
        subprocess.run(['tmux', 'select-pane', '-t', f'{session_name}:{window_index}.{pane_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error selecting pane {pane_index} in window {window_index} of session '{session_name}': {e}")

def resize_tmux_pane(session_name, window_index, pane_index, size, direction='h'):
    """
    Resizes a pane in the specified tmux window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the pane to resize.
        size (int): New size of the pane.
        direction (str): Direction to resize the pane ('h' for horizontal, 'v' for vertical).
    """
    direction_flag = '-L' if direction == 'h' else '-U'
    try:
        subprocess.run(['tmux', 'resize-pane', direction_flag, '-t', f'{session_name}:{window_index}.{pane_index}', '-x', str(size)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error resizing pane {pane_index} in window {window_index} of session '{session_name}' to size {size} in direction '{direction}': {e}")

def move_pane(session_name, window_index, pane_index, target_window_index):
    """
    Moves a pane to a new window within the specified tmux session.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window containing the pane.
        pane_index (int): Index of the pane to move.
        target_window_index (int): Index of the target window.
    """
    try:
        subprocess.run(['tmux', 'move-pane', '-s', f'{session_name}:{window_index}.{pane_index}', '-t', f'{session_name}:{target_window_index}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error moving pane {pane_index} from window {window_index} to window {target_window_index} in session '{session_name}': {e}")

def swap_panes(session_name, window_index1, pane_index1, window_index2, pane_index2):
    """
    Swaps two panes between tmux windows.

    Args:
        session_name (str): Name of the tmux session.
        window_index1 (int): Index of the first tmux window.
        pane_index1 (int): Index of the first pane.
        window_index2 (int): Index of the second tmux window.
        pane_index2 (int): Index of the second pane.
    """
    try:
        subprocess.run(['tmux', 'swap-pane', '-s', f'{session_name}:{window_index1}.{pane_index1}', '-t', f'{session_name}:{window_index2}.{pane_index2}'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error swapping pane {pane_index1} in window {window_index1} with pane {pane_index2} in window {window_index2} in session '{session_name}': {e}")

def capture_pane_output(session_name, window_index, pane_index):
    """
    Captures the output of a specific tmux pane.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the tmux pane.

    Returns:
        str: Output captured from the tmux pane, or an empty string if an error occurs.
    """
    try:
        result = subprocess.run(['tmux', 'capture-pane', '-p', '-t', f'{session_name}:{window_index}.{pane_index}'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error capturing output from pane {pane_index} in window {window_index} of session '{session_name}': {e}")
        return ""
    except TypeError as e:
        print(f"Type error: {e}")
        return ""
