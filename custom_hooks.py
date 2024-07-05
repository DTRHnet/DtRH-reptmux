#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: custom_hooks.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

from hooks import hook_manager

def pre_hook(function_name, *args, **kwargs):
    print(f"Before function '{function_name}' with args: {args} and kwargs: {kwargs}")

def post_hook(function_name, *args, **kwargs):
    print(f"After function '{function_name}' with args: {args} and kwargs: {kwargs}")

# Register generic hooks
hook_manager.register_hook('before_function', pre_hook)
hook_manager.register_hook('after_function', post_hook)

# Enable or disable hooks as needed
hook_manager.enable_hooks()
# hook_manager.disable_hooks()
