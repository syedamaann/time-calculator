    def add_time(start, duration, day=None):
    # Split the start time into hours, minutes, and period (AM/PM)
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Split the duration time into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Convert start time to 24-hour format for easier calculation
    if period == 'PM':
        start_hours += 12

    # Calculate total minutes
    total_minutes = start_minutes + duration_minutes
    additional_hours = total_minutes // 60
    total_minutes %= 60

    # Calculate total hours
    total_hours = start_hours + duration_hours + additional_hours
    total_days = total_hours // 24
    total_hours %= 24

    # Determine new period (AM/PM)
    new_period = 'AM' if total_hours < 12 else 'PM'

    # Convert total hours back to 12-hour format
    if total_hours == 0:
        total_hours = 12
    elif total_hours > 12:
        total_hours -= 12

    # Format the result time
    new_time = f"{total_hours}:{total_minutes:02d} {new_period}"

    # Format additional information (next day / n days later, day of the week)
    if total_days == 1:
        new_time += " (next day)"
    elif total_days > 1:
        new_time += f" ({total_days} days later)"

    if day:
        day = day.capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(day)
        new_day_index = (start_day_index + total_days) % 7
        new_time += f", {days_of_week[new_day_index]}"

    return new_time
