# DtRH-reptmux: Simplifying Tmux and Process Management

## Overview

DtRH-reptmux is a robust toolset and wrapper for managing tmux sessions, windows, and panes, along with reptyr functionality to attach and manage processes within tmux panes or terminals. This project is designed to streamline terminal multiplexing and process management, making it easier to handle complex terminal workflows.

## Features

Reptmux is designed to address several key challenges:

- **Focused Function Wrapping:** Rather than wrapping every tmux function, Reptmux simplifies the most common tmux operations without relying on the libtmux library.
- **Unified Property State Management:** Reptmux manages tmux properties to make intelligent assumptions when parameters are missing. For example, if you create a window without specifying a session ID/name, it defaults to the current session gracefully.
- **Flexible Hooking:** Built-in function hooking allows for code injection before, after, or at any point during the execution of wrapped functions, providing great flexibility.
- **Process Management with Reptyr:** Integrating reptyr makes it easy to move existing processes and terminals into and out of tmux sessions.
- **Terminal Communication:** Simplify sending and recieving data amongst regular terminals as well as tmux panes and windows 
- **Enhanced Error Handling:** Gracefully handle errors and provide informative messages.
- **Modular Design:** Reptmux is designed for easy integration, whether you need part or all of its functionality. Simply import the required modules and get started.
- **Future Scripting Language:** A simple scripting language is planned to work with Reptmux, further simplifying interactions and making tmux management more accessible than ever.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/DTRHnet/DtRH-reptmux.git
    cd DtRH-reptmux
    ```

2. Ensure you have tmux and reptyr installed:
    ```bash
    sudo apt-get install tmux reptyr
    ```

3. (Optional) Create a virtual environment and activate it:
    ```bash
    python3 -m venv .env
    source .env/bin/activate
    ```

## Project Structure

```
DtRH-reptmux/
├── tmux/
│   ├── cmds.py
│   ├── session.py
│   ├── window.py
│   ├── pane.py
│   ├── server.py
├── reptyr/
│   └── reptyr.py
├── hooks.py
├── custom_hooks.py
├── global_state.py
├── utils.py
├── main.py
├── README.md
├── CHANGELOG.md
```

## Usage

### Initialize the Server and Perform Operations

Ensure the tmux server is running and perform various operations using the provided scripts.

```python
# main.py

# Imports will be packaged in the future to reduce unnecessary typing
#
from tmux.session import create_tmux_session, kill_tmux_session
from tmux.window import create_tmux_window, kill_tmux_window
from tmux.pane import split_tmux_pane, kill_tmux_pane
from tmux.server import start_tmux_server, stop_tmux_server
from cmd import send_keys_to_pane, execute_tmux_command
from reptyr.reptyr import reattach_process_to_tmux_pane, reattach_process_to_terminal, list_reptyr_pids, is_process_attached, detach_process, move_process_to_tmux_pane, reattach_process_with_env, list_process_ids_and_names
import custom_hooks  # This registers the hooks
import global_state

# Enable hooks
custom_hooks.hook_manager.enable_hooks()

# Start tmux server if not already running
start_tmux_server()

# Example function calls to demonstrate hooks and global state usage
create_tmux_session("REPTMUX")
create_tmux_window("REPTMUX-WINDOW")  # No session name provided, uses current session
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
```

### Custom Hooks

Add custom hooks to monitor function calls and execution times.

```python
# custom_hooks.py

from hooks import hook_manager

def log_before_function(function_name, *args, **kwargs):
    print(f"Before function '{function_name}' with arguments: {args} and keyword arguments: {kwargs}")

def log_after_function(function_name, *args, **kwargs):
    print(f"After function '{function_name}' with arguments: {args} and keyword arguments: {kwargs}")

# Register hooks
hook_manager.register_hook('before_function', log_before_function)
hook_manager.register_hook('after_function', log_after_function)
```

## Contributing

Contributions are welcome! Please create a pull request with your changes or open an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [tmux](https://github.com/tmux/tmux) - Terminal multiplexer
- [reptyr](https://github.com/nelhage/reptyr) - Reattach processes to a new terminal

---


# ChangeLog

## Version 0.0.2

**Date: 2024-07-05**

### Added
- **Global State Management:**
  - Introduced `global_state.py` to store the current session, window, and pane information.
  - Added `tmux_server_info` to keep track of the tmux server's state, socket file, and creation time.

- **Server Initialization and Management:**
  - Created `server.py` to handle tmux server initialization, checking if the server is running, and starting/stopping the server.
  - Updated `main.py` to ensure the tmux server is initialized before performing any operations.

- **Unified State Retrieval:**
  - Created `utils.py` to define a function `get_current_state` to retrieve the current session, window, and pane based on provided arguments or the global state.

- **Hook Management:**
  - Introduced `hooks.py` to manage hooks before and after function calls.
  - Registered hooks in `custom_hooks.py` for logging function calls and monitoring execution times.
  - Updated all relevant functions in `session.py`, `window.py`, `pane.py`, `cmds.py`, and `reptyr.py` to include before and after hooks.

- **Enhanced `reptyr.py`:**
  - Updated functions to utilize global state and hooks.
  - Added error handling for subprocess calls.

- **Example Usage:**
  - Provided an example `main.py` script to demonstrate the usage of tmux and reptyr functions with hooks and global state. Currently a work in progress, so left commented out.

### Changed
- **Function Signatures:**
  - Updated functions in `session.py`, `window.py`, `pane.py`, and `cmds.py` to use the unified state retrieval function.

### Fixed
- **Error Handling:**
  - Improved error handling for subprocess calls across all relevant functions to ensure graceful failures and informative error messages.

---

## Version 0.0.1

**Date: 2024-07-04**

### Initial Release
- Basic tmux session, window, and pane management.
- Basic reptyr functionality for attaching processes to tmux panes and terminals.

---
