import subprocess
from session import list_tmux_sessions
from window import list_tmux_windows
from pane import list_tmux_panes

def send_keys_to_pane(session_name, window_index, pane_index, keys):
    """
    Sends keystrokes to a specific tmux pane.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
        pane_index (int): Index of the tmux pane.
        keys (str): Keystrokes to send to the tmux pane.
    """
    try:
        subprocess.run(['tmux', 'send-keys', '-t', f'{session_name}:{window_index}.{pane_index}', keys, 'C-m'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error sending keys to pane {pane_index} in window {window_index} of session '{session_name}': {e}")

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

def list_all_sessions_windows_panes():
    """
    Lists all sessions, windows, and panes in tmux.
    """
    print("Sessions:")
    sessions = get_all_sessions()
    for session in sessions:
        print(session)
        print(f"\nWindows in session {session}:")
        windows = get_all_windows(session)
        for window in windows:
            print(window)
            print(f"\nPanes in window {window} of session {session}:")
            panes = get_all_panes(session, window)
            for pane in panes:
                print(pane)

def get_all_sessions():
    """
    Retrieves the list of all tmux sessions.

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

def get_all_windows(session_name):
    """
    Retrieves the list of all tmux windows in a session.

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

def get_all_panes(session_name, window_index):
    """
    Retrieves the list of all tmux panes in a window.

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

def find_pane(session_name, search_string):
    """
    Searches for a pane that contains the specified string in its output.

    Args:
        session_name (str): Name of the tmux session.
        search_string (str): String to search for in pane output.

    Returns:
        tuple: Session, window, and pane indexes of the found pane, or None if not found.
    """
    try:
        for window in get_all_windows(session_name):
            for pane in get_all_panes(session_name, window):
                output = capture_pane_output(session_name, window, pane)
                if search_string in output:
                    return session_name, window, pane
    except Exception as e:
        print(f"Error finding pane containing '{search_string}' in session '{session_name}': {e}")
    return None

def sync_panes(session_name, window_index):
    """
    Synchronizes input across all panes in a window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
    """
    try:
        subprocess.run(['tmux', 'setw', '-t', f'{session_name}:{window_index}', 'synchronize-panes', 'on'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error synchronizing panes in window {window_index} of session '{session_name}': {e}")

def unsync_panes(session_name, window_index):
    """
    Unsynchronizes input across all panes in a window.

    Args:
        session_name (str): Name of the tmux session.
        window_index (int): Index of the tmux window.
    """
    try:
        subprocess.run(['tmux', 'setw', '-t', f'{session_name}:{window_index}', 'synchronize-panes', 'off'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error unsynchronizing panes in window {window_index} of session '{session_name}': {e}")
