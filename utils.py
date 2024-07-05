#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: utils.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

import global_state

def get_current_state(session_name=None, window_index=None, pane_index=None):
    """
    Returns the current state for session, window, and pane based on provided arguments.

    Args:
        session_name (str, optional): Name of the tmux session.
        window_index (int, optional): Index of the tmux window.
        pane_index (int, optional): Index of the tmux pane.

    Returns:
        tuple: Current session, window, and pane.
    """
    current_session = session_name or global_state.current_session
    current_window = window_index or global_state.current_window
    current_pane = pane_index or global_state.current_pane

    return current_session, current_window, current_pane
