# Time Calculator

## Overview
This project implements a Python function called `add_time` that calculates the new time after adding a given duration to a start time in the 12-hour clock format. The function also optionally accepts a starting day of the week and returns the day of the week of the result.

## Function Signature
```python
def add_time(start, duration, day=None):
    """
    Add the given duration to the start time and return the result.

    Parameters:
    - start (str): Start time in the format "HH:MM AM/PM".
    - duration (str): Duration time in the format "HH:MM".
    - day (str, optional): Starting day of the week (case insensitive).

    Returns:
    str: The new time in the format "HH:MM AM/PM (optional: day of the week, optional: next day / n days later)".
    """
```

## Usage
To use the `add_time` function, call it with the start time, duration time, and optionally the starting day of the week:

```python
new_time = add_time("11:30 AM", "2:32", "Monday")
print(new_time)  # Output: 2:02 PM, Monday
```

## Examples
Here are some examples of using the `add_time` function:

```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
```

## Development
The function has been thoroughly tested to ensure correct behavior in various scenarios. However, if you encounter any issues or have suggestions for improvement, feel free to contribute to the project.

## Limitations
- The function assumes valid input format for start time and duration time.
- The function does not handle time zone conversions.

## Dependencies
None. The function does not rely on any external libraries.
