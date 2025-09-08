import enum
import sys

# Public API of this module: only these functions and names will be imported
# when someone does `from module import *`.
__all__ = [
    "info", "warn", "error",           # Runtime logging wrappers
    "d_info", "d_warn", "d_error",     # Debug logging wrappers
    "toggle_DEBUG_LOGS", "toggle_RUNTIME_LOGS"
] 

class Status(enum.Enum):
    """
    Enumeration of possible log statuses.
    
    Members:
        ERROR   - Used for error messages (printed to stderr).
        INFO    - Used for informational messages.
        WARNING - Used for warning messages.
    """
    ERROR = "ERROR"
    INFO = "INFO"
    WARNING = "WARNING"

class Sentinel:
    """
    Core logging system that controls runtime and debug logs.
    
    Attributes:
        DEBUG_LOGS (bool): Whether debug logs are enabled.
        RUNTIME_LOGS (bool): Whether runtime logs are enabled.
    """
    
    DEBUG_LOGS: bool = False
    RUNTIME_LOGS: bool = True
    
    @staticmethod
    def __log(status, message):
        """
        Print a message with the given status.
        
        Args:
            status (Status): The status level for the log.
            message (str): The log message.
        
        Notes:
            - ERROR messages are printed to stderr.
            - INFO and WARNING messages are printed to stdout.
        """
        if status == Status.ERROR:
            print(f"[{status.value}] {message}", file=sys.stderr)
        else:
            print(f"[{status.value}] {message}")
    
    @staticmethod
    def __set_proper_status(status: Status, message: str):
        """
        Validate the status and log the message.
        
        Args:
            status (Status): The desired log status.
            message (str): The log message.
        
        Behavior:
            - If the provided status is not a `Status` enum member, 
              logs a warning about the invalid status and then logs the 
              message as INFO.
            - Otherwise, logs the message with the given status.
        """
        if not isinstance(status, Status):
            Sentinel.__log(Status.WARNING, f"Unrecognized status \"{status}\"! setting default status \"INFO\"")
            Sentinel.__log(Status.INFO, message)
        else:
            Sentinel.__log(status, message)

    @staticmethod
    def DLOG(status: Status, message: str, *, bypass_log_vars: bool = False):
        """
        Debug-level logging function.
        
        Args:
            status (Status): The log level to use (INFO, WARNING, ERROR).
            message (str): The message to log.
            bypass_log_vars (bool, optional): If True, log regardless of 
                DEBUG_LOGS being enabled. Defaults to False.
        
        Notes:
            - Does nothing if the message is empty.
            - Respects the DEBUG_LOGS toggle unless bypassed.
        """
        if message == "":
            return
        if not bypass_log_vars and not Sentinel.DEBUG_LOGS:
            return
        Sentinel.__set_proper_status(status, message)

    @staticmethod
    def LOG(status: Status, message: str, *, bypass_log_vars: bool = False):
        """
        Runtime-level logging function.
        
        Args:
            status (Status): The log level to use (INFO, WARNING, ERROR).
            message (str): The message to log.
            bypass_log_vars (bool, optional): If True, log regardless of 
                RUNTIME_LOGS being enabled. Defaults to False.
        
        Notes:
            - Does nothing if the message is empty.
            - Respects the RUNTIME_LOGS toggle unless bypassed.
        """
        if message == "":
            return
        if not bypass_log_vars and not Sentinel.RUNTIME_LOGS:
            return
        Sentinel.__set_proper_status(status, message)


# -------------------------
# User-facing wrapper functions
# -------------------------

def info(message: str, *, bypass_log_vars: bool = False):
    """Log an INFO message at runtime level."""
    Sentinel.LOG(Status.INFO, message, bypass_log_vars=bypass_log_vars)

def warn(message: str, *, bypass_log_vars: bool = False):
    """Log a WARNING message at runtime level."""
    Sentinel.LOG(Status.WARNING, message, bypass_log_vars=bypass_log_vars)

def error(message: str, *, bypass_log_vars: bool = False):
    """Log an ERROR message at runtime level (stderr)."""
    Sentinel.LOG(Status.ERROR, message, bypass_log_vars=bypass_log_vars)

def d_info(message: str, *, bypass_log_vars: bool = False):
    """Log an INFO message at debug level."""
    Sentinel.DLOG(Status.INFO, message, bypass_log_vars=bypass_log_vars)

def d_warn(message: str, *, bypass_log_vars: bool = False):
    """Log a WARNING message at debug level."""
    Sentinel.DLOG(Status.WARNING, message, bypass_log_vars=bypass_log_vars)

def d_error(message: str, *, bypass_log_vars: bool = False):
    """Log an ERROR message at debug level (stderr)."""
    Sentinel.DLOG(Status.ERROR, message, bypass_log_vars=bypass_log_vars)


# -------------------------
# Toggle functions
# -------------------------

def toggle_DEBUG_LOGS():
    """
    Toggle the DEBUG_LOGS setting.
    
    If DEBUG_LOGS was False, enables debug logging. 
    If True, disables it.
    """
    Sentinel.DEBUG_LOGS = not Sentinel.DEBUG_LOGS

def toggle_RUNTIME_LOGS():
    """
    Toggle the RUNTIME_LOGS setting.
    
    If RUNTIME_LOGS was False, enables runtime logging. 
    If True, disables it.
    """
    Sentinel.RUNTIME_LOGS = not Sentinel.RUNTIME_LOGS
