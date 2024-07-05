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
