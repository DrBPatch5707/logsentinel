
# logsentinel

Tiny, opt-in runtime/debug logger with simple wrapper functions:
`info`, `warn`, `error`, `d_info`, `d_warn`, `d_error`, plus toggles.

### Install (local)
```bash
python -m pip install -U build
python -m build
python -m pip install --user dist/logsentinel-*.whl
```

## Usage

```python
from logsentinel import *
```

#### Runtime Logs (default: enabled)
Runtime logs (`info`, `warn`, `error`) are meant for **normal application messages**.

```python
info("informational message")   # [INFO] informational message
warn("watch out")               # [WARNING] watch out
error("something failed")       # [ERROR] something failed (stderr)
```

You can **disable runtime logs globally**:

```python
toggle_RUNTIME_LOGS()           # flips RUNTIME_LOGS to False
info("hidden")                  # no output
```

Force a runtime message to appear even if runtime logs are disabled:

```python
info("always shown", bypass_log_vars=True)   # prints regardless of RUNTIME_LOGS
```

---

#### Debug Logs (default: disabled)
Debug logs (`d_info`, `d_warn`, `d_error`) are designed for **development or troubleshooting**.

```python
d_info("debug details")         # no output (disabled by default)

toggle_DEBUG_LOGS()             # enable debug logging
d_info("debug details")         # [INFO] debug details
d_warn("be careful")            # [WARNING] be careful
d_error("debug failure")        # [ERROR] debug failure (stderr)
```

Force a debug message to print even if debug logs are disabled:

```python
d_info("force log", bypass_log_vars=True)   # [INFO] force log
```

---

#### Mixing Runtime and Debug
You can toggle runtime and debug logs independently:

- **Only runtime logs** (default state).
- **Runtime + debug logs** (enable debug).
- **Silent mode** (disable runtime, leave debug off).
- **Selective overrides** (use `bypass_log_vars=True` for individual messages).

---

#### Quick Reference

| Function   | Default Enabled? | Output Stream | Affected by Toggle | Example                          |
|------------|------------------|---------------|--------------------|----------------------------------|
| `info`     | ✅ Yes           | `stdout`      | `RUNTIME_LOGS`     | `info("msg")` → `[INFO] msg`     |
| `warn`     | ✅ Yes           | `stdout`      | `RUNTIME_LOGS`     | `warn("msg")` → `[WARNING] msg`  |
| `error`    | ✅ Yes           | `stderr`      | `RUNTIME_LOGS`     | `error("msg")` → `[ERROR] msg`   |
| `d_info`   | ❌ No            | `stdout`      | `DEBUG_LOGS`       | `d_info("msg")`                  |
| `d_warn`   | ❌ No            | `stdout`      | `DEBUG_LOGS`       | `d_warn("msg")`                  |
| `d_error`  | ❌ No            | `stderr`      | `DEBUG_LOGS`       | `d_error("msg")`                 |

All functions accept:
```python
bypass_log_vars=True   # Forces the message to print, ignoring toggles
```

---

#### Example Session

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

