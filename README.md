# Stop-Printing Start Logging in Python

## Files
- `main.py`
- `other_module.py`
- `my_logs.log` 

## Problem with `print()`

Using `print()` for debugging and tracking our application's behavior has major drawbacks

## The Solution: Python's `logging` Module

The Python standard library includes a robust `logging` module that solves all these problems.

### 1. Basic Logging Setup (`samplelog.py`)

The file `samplelog.py` demonstrates the five standard log levels.

**Key Concepts:**
*   **Levels:** `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`. We set a threshold, and only messages of that level or higher are recorded.
*   **Persistence:** Messages are written to a file, so we can review them long after our program has finished running.

### 2. Informative Logs (`main.py`)

The `main.py` file, logging  with a custom format. 

**The magic is in the `format` string:**
*   `%(levelname)s`: The severity level (e.g., INFO, WARNING).
*   `%(asctime)s`: The timestamp, formatted by `datefmt`.
*   `%(message)s`: The log message we write.
*   `%(lineno)d`: The **line number** where the log call was made. Useful for debugging!
*   `%(filename)s`: The **source file** where the log call was made.

This format creates the rich, informative log entries you see in `my_logs.log`:
```bash
INFO (09/09/2025 02:09:43 PM): Hello, my name is Slim Shady! (Line: 12 [main.py])
WARNING (09/09/2025 02:09:43 PM): Oh no! You caught me! (Line: 13 [main.py])
```

### 3. Consistent Logging Across Modules (`other_module.py`)

A huge advantage of the `logging` module is its seamless integration across our entrire project. We don't need to configure logging in every file.

**How it works:**
1.  We configure logging once in your main script (like in `main.py`).
2.  When we import other modules (like `other_module`), they automatically use that same configuration.
3.  Any log calls from those modules will be output with the correct format and will correctly show their **own filename and line number**.

This is why the log file shows:
```bash
INFO (09/09/2025 02:09:43 PM): This is from: "other_module.py" (Line: 4 [other_module.py])
```

Even though the configuration was only done in `main.py`, the log from `other_module.py` correctly identifies itself.


## Example Output

After running `main.py`, the `my_logs.log` file will contain:
```bash
INFO (09/09/2025 02:09:43 PM): Hello, my name is Slim Shady! (Line: 12 [main.py])
WARNING (09/09/2025 02:09:43 PM): Oh no! You caught me! (Line: 13 [main.py])
INFO (09/09/2025 02:09:43 PM): This is from: "other_module.py" (Line: 4 [other_module.py])
```

## Key Takeaways

*   **Stop using `print()`** for anything other than your application's primary output.
*   **Start using `logging`** for all your debug, info, warning, and error messages.
*   **Use informative formats** that include the timestamp, level, filename, and line number.
*   **Configure once** in your main script; it works across all imported modules.


## Links

*   [Official Python logging documentation](https://docs.python.org/3/library/logging.html)
*   [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

---

