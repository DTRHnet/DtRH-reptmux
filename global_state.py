#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: global_state.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

current_session = None
current_window = None
current_pane = None
tmux_server_info = {
    'is_running': False,
    'socket_file': None,
    'time_created': None
}
