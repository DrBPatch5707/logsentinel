# logsentinel

Tiny, opt-in runtime/debug logger with simple wrapper functions:
`info`, `warn`, `error`, `d_info`, `d_warn`, `d_error`, plus toggles.

---

## Install

You can install directly from GitHub. This will build from source on your machine (no wheels to download).

### Latest tagged release (recommended)
```bash
pip install "git+https://github.com/DrBPatch5707/logsentinel.git@v0.1.0"
```

### Development version (main branch)
```bash
pip install "git+https://github.com/DrBPatch5707/logsentinel.git@main"
```

Pinning a specific tag is recommended for reproducibility.

---

## Usage

```python
from logsentinel import *
```

### Runtime Logs (default: enabled)
Runtime logs (`info`, `warn`, `error`) are meant for **normal application messages**.

```python
info("informational message")   # [INFO] informational message
warn("watch out")               # [WARNING] watch out
error("something failed")       # [ERROR] something failed (stderr)
```

Disable runtime logs globally:

```python
toggle_RUNTIME_LOGS()           # flips RUNTIME_LOGS to False
info("hidden")                  # no output
```

Bypass the toggle to always log:

```python
info("always shown", bypass_log_vars=True)
```

---

### Debug Logs (default: disabled)
Debug logs (`d_info`, `d_warn`, `d_error`) are designed for **development or troubleshooting**.

```python
d_info("debug details")         # no output (disabled by default)

toggle_DEBUG_LOGS()             # enable debug logging
d_info("debug details")         # [INFO] debug details
d_warn("be careful")            # [WARNING] be careful
d_error("debug failure")        # [ERROR] debug failure (stderr)
```

Bypass the toggle to always log:

```python
d_info("force log", bypass_log_vars=True)
```

---

### Mixing Runtime and Debug
You can toggle runtime and debug logs independently:

- **Only runtime logs** (default state).
- **Runtime + debug logs** (enable debug).
- **Silent mode** (disable runtime, leave debug off).
- **Selective overrides** (use `bypass_log_vars=True` per call).

---

### Quick Reference

| Function   | Default Enabled? | Output Stream | Controlled by Toggle | Example                          |
|------------|------------------|---------------|----------------------|----------------------------------|
| `info`     | ✅ Yes           | `stdout`      | `RUNTIME_LOGS`       | `info("msg")` → `[INFO] msg`     |
| `warn`     | ✅ Yes           | `stdout`      | `RUNTIME_LOGS`       | `warn("msg")` → `[WARNING] msg`  |
| `error`    | ✅ Yes           | `stderr`      | `RUNTIME_LOGS`       | `error("msg")` → `[ERROR] msg`   |
| `d_info`   | ❌ No            | `stdout`      | `DEBUG_LOGS`         | `d_info("msg")`                  |
| `d_warn`   | ❌ No            | `stdout`      | `DEBUG_LOGS`         | `d_warn("msg")`                  |
| `d_error`  | ❌ No            | `stderr`      | `DEBUG_LOGS`         | `d_error("msg")`                 |

All functions accept:
```python
bypass_log_vars=True   # forces the message to print, ignoring toggles
```

---

### Example Session

```python
from logsentinel import *

info("program started")            # [INFO] program started

toggle_RUNTIME_LOGS()              # disable runtime logs
info("hidden")                     # no output

d_error("forced error", bypass_log_vars=True)
# always prints: [ERROR] forced error

toggle_DEBUG_LOGS()                # enable debug logs
d_info("debugging...")             # [INFO] debugging...
```

---

## Development

- Clone the repo:
  ```bash
  git clone https://github.com/DrBPatch5707/logsentinel.git
  cd logsentinel
  ```
- Install in editable mode:
  ```bash
  pip install -e .
  ```
- Bump the version in `pyproject.toml` before tagging a new release.
