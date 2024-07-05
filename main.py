#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: main.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >


#### THIS SIMPLY DEMONSTRATES LIMITED FUNCTIONALITY ####


from tmux.session import create_tmux_session, kill_tmux_session
from tmux.window import create_tmux_window, kill_tmux_window
from tmux.pane import split_tmux_pane, kill_tmux_pane
from tmux.server import start_tmux_server
from tmux.cmds import send_keys_to_pane
from reptyr.reptyr import *
import custom_hooks  # This registers the hooks

# Enable hooks
custom_hooks.hook_manager.enable_hooks()

# Start tmux server if not already running
start_tmux_server()

# Example function calls to demonstrate hooks and global state usage
create_tmux_session("example_session")
create_tmux_window("example_window")  # No session name provided, uses current session
split_tmux_pane('h')  # No session or window provided, uses current session and window
send_keys_to_pane("echo 'Hello, tmux!'")  # No session, window, or pane provided
kill_tmux_pane()  # No session, window, or pane provided
kill_tmux_window()  # No session or window provided
kill_tmux_session()  # No session provided

# Reptyr example usage
# pid = 1234  # Example PID
# reattach_process_to_tmux_pane(pid)
# reattach_process_to_terminal(pid, '/dev/pts/1')
# print(list_reptyr_pids())
# print(is_process_attached(pid))
# detach_process(pid)
# move_process_to_tmux_pane(pid)
# reattach_process_with_env(pid, '/dev/pts/1', {"EXAMPLE_VAR": "value"})
# print(list_process_ids_and_names())

# Optionally stop the server
# stop_tmux_server()
