# Stop-Printing-Start-Logging-in-Python
# Stop Printing, Start Logging: A Practical Guide

Tired of using `print()` statements for debugging that you have to later clean up? Welcome to professional Python development. This repository demonstrates how to replace clunky print statements with a powerful, flexible, and built-in logging system.

## 📁 Repository Structure

.
├── main.py # Main application with detailed logging configuration
├── other_module.py # Example of logging from an imported module
├── samplelog.py # Basic logging example
└── my_logs.log # Generated log file (created after running main.py)


## 🚫 The Problem with `print()`

Using `print()` for debugging and tracking your application's behavior has major drawbacks:

*   **It's temporary:** You have to manually remove them before shipping code.
*   **It's messy:** Output is mixed with your program's actual output and other prints.
*   **It lacks context:** You get a message, but not *when* it happened or *where* it came from.
*   **It's inflexible:** You can't easily silence debug messages or send output to a file without changing your code.

## ✅ The Solution: Python's `logging` Module

The Python standard library includes a robust `logging` module that solves all these problems. Let's see how it works with the examples in this repo.

### 1. Basic Logging Setup (`samplelog.py`)

The file `samplelog.py` shows the absolute simplest way to get started. It configures logging to write messages to a file (`my_logs.log`) and demonstrates the five standard log levels.

**Key Concepts:**
*   **Levels:** `DEBUG` < `INFO` < `WARNING` < `ERROR` < `CRITICAL`. You set a threshold, and only messages of that level or higher are recorded.
*   **Persistence:** Messages are written to a file, so you can review them long after your program has finished running.

### 2. Professional, Informative Logs (`main.py`)

The `main.py` file takes logging to the next level with a custom format. This is where you see the real power.

**The magic is in the `format` string:**
*   `%(levelname)s`: The severity level (e.g., INFO, WARNING).
*   `%(asctime)s`: The timestamp, formatted by `datefmt`.
*   `%(message)s`: The log message you write.
*   `%(lineno)d`: The **line number** where the log call was made. Incredibly useful for debugging!
*   `%(filename)s`: The **source file** where the log call was made.

This format creates the rich, informative log entries you see in `my_logs.log`:
INFO (09/09/2025 02:09:43 PM): Hello, my name is Slim Shady! (Line: 12 [main.py])
WARNING (09/09/2025 02:09:43 PM): Oh no! You caught me! (Line: 13 [main.py])



### 3. Consistent Logging Across Modules (`other_module.py`)

A huge advantage of the `logging` module is its seamless integration across your entire project. You don't need to configure logging in every file.

**How it works:**
1.  You configure logging once in your main script (like in `main.py`).
2.  When you import other modules (like `other_module`), they automatically use that same configuration.
3.  Any log calls from those modules will be output with the correct format and will correctly show their **own filename and line number**.

This is why the log file shows:
INFO (09/09/2025 02:09:43 PM): This is from: "other_module.py" (Line: 4 [other_module.py])


Even though the configuration was only done in `main.py`, the log from `other_module.py` correctly identifies itself. This is a game-changer for debugging complex applications.

## 🚀 How to Use This Code

1.  Clone this repository
2.  Run the main application:
    ```bash
    python main.py
    ```
3.  Examine the generated log file:
    ```bash
    cat my_logs.log
    ```
4.  (Optional) Run the basic sample to compare:
    ```bash
    python samplelog.py
    ```

## 📋 Example Output

After running `main.py`, your `my_logs.log` file will contain:
INFO (09/09/2025 02:09:43 PM): Hello, my name is Slim Shady! (Line: 12 [main.py])
WARNING (09/09/2025 02:09:43 PM): Oh no! You caught me! (Line: 13 [main.py])
INFO (09/09/2025 02:09:43 PM): This is from: "other_module.py" (Line: 4 [other_module.py])


## 🎯 Key Takeaways

*   **Stop using `print()`** for anything other than your application's primary output.
*   **Start using `logging`** for all your debug, info, warning, and error messages.
*   **Use informative formats** that include the timestamp, level, filename, and line number.
*   **Configure once** in your main script; it works across all imported modules.

Embrace logging. It will make you a more efficient and professional developer.

## 📚 Learn More

*   [Official Python logging documentation](https://docs.python.org/3/library/logging.html)
*   [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)

---

