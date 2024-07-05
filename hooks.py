#  ______ _  ______ _   _                       _              
#  |  _  \ | | ___ \ | | |                     | |             
#  | | | | |_| |_/ / |_| |______ _ __ ___ _ __ | |_ _   _ _ __ 
#  | | | | __|    /|  _  |______| '__/ _ \ '_ \| __| | | | '__|
#  | |/ /| |_| |\ \| | | |      | | |  __/ |_) | |_| |_| | |   
#  |___/  \__\_| \_\_| |_/      |_|  \___| .__/ \__|\__, |_|   
#                                        | |         __/ |     
#                                        |_|        |___/      
#  Version: 0.0.2
#  File: hooks.py
#  Date: Friday 5th, July 2024
#                                              https://dtrh.net
#                                 < admin [at] dtrh [dot] net >

class HookManager:
    def __init__(self):
        self.hooks = {
            'before_function': [],
            'after_function': []
        }
        self.enabled = True

    def register_hook(self, event, func):
        """
        Register a function to be called when a specific event occurs.

        Args:
            event (str): The name of the event to hook into.
            func (callable): The function to call when the event occurs.
        """
        if event in self.hooks:
            self.hooks[event].append(func)
        else:
            raise ValueError(f"No such hook point: {event}")

    def run_hooks(self, event, function_name, *args, **kwargs):
        """
        Run all functions registered for a specific event.

        Args:
            event (str): The name of the event to trigger.
            function_name (str): The name of the function where the hook is being run.
            *args: Positional arguments to pass to the hook functions.
            **kwargs: Keyword arguments to pass to the hook functions.
        """
        if self.enabled and event in self.hooks:
            for func in self.hooks[event]:
                func(function_name, *args, **kwargs)

    def enable_hooks(self):
        """Enable all hooks."""
        self.enabled = True

    def disable_hooks(self):
        """Disable all hooks."""
        self.enabled = False


hook_manager = HookManager()
