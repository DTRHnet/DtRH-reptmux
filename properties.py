#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: properties.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >


import subprocess
from tmux.session import list_tmux_sessions
from tmux.window import list_tmux_windows
from tmux.pane import list_tmux_panes

properties = {
    "sessions": {},
    "windows": {},
    "panes": {}
}

def update_sessions():
    """
    Updates the sessions property with current tmux sessions.
    """
    try:
        sessions = list_tmux_sessions()
        if sessions:
            properties["sessions"] = {i: session for i, session in enumerate(sessions)}
        else:
            properties["sessions"] = {}
    except Exception as e:
        print(f"Error updating sessions: {e}")
        properties["sessions"] = {}

def update_windows():
    """
    Updates the windows property with current tmux windows for each session.
    """
    try:
        for session_id, session_name in properties["sessions"].items():
            windows = list_tmux_windows(session_name)
            properties["windows"][session_name] = {i: window for i, window in enumerate(windows)}
    except Exception as e:
        print(f"Error updating windows for session '{session_name}': {e}")
        properties["windows"][session_name] = {}

def update_panes():
    """
    Updates the panes property with current tmux panes for each window in each session.
    """
    try:
        for session_id, session_name in properties["sessions"].items():
            for window_id, window_index in properties["windows"][session_name].items():
                panes = list_tmux_panes(session_name, window_index)
                properties["panes"][f"{session_name}:{window_index}"] = {i: pane for i, pane in enumerate(panes)}
    except Exception as e:
        print(f"Error updating panes for window '{window_index}' in session '{session_name}': {e}")
        properties["panes"][f"{session_name}:{window_index}"] = {}

def update_all_properties():
    """
    Updates all properties (sessions, windows, panes) with current tmux information.
    """
    try:
        update_sessions()
        update_windows()
        update_panes()
    except Exception as e:
        print(f"Error updating all properties: {e}")
