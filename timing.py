# Import modules:
import time
import atexit
import threading
from itertools import cycle
try:
    from termcolor import colored
except ImportError:
    print('Consider installing `termcolor` for colored outputs.')


# Class to time the execution of a block of code:
class timer:

    """
    Class to time the execution of a block of code.

    Attributes:
    ----------
    message : str
        The message to be displayed before the timer.
    start : float
        The time at which the timer started.
    _stop_event : threading.Event
        The event to stop the timer.
    thread : threading.Thread
        The thread to run the timer.
    spinner : itertools.cycle
        The spinner to be displayed while the timer is running.
    
    Methods:
    -------
    _show_time()
        Displays the elapsed time.
    __enter__()
        Starts the timer.
    __exit__()
        Stops the timer.
    """

    # Initialize the class:
    def __init__(self, message):
        # Set the message:
        self.message = message
        # Initialize the timer:
        self.start = None
        # Initialize the stop event:
        self._stop_event = threading.Event()
        # Initialize the thread:
        self.thread = threading.Thread(target=self._show_time)
        # Initialize the spinner:
        self.spinner = cycle(['♩', '♪', '♫', '♬'])

    # Function to show the time:
    def _show_time(self):
        # Loop until the stop event is set:
        while not self._stop_event.is_set():
            # Get the elapsed time:
            elapsed_time = time.time() - self.start
            # Convert the elapsed time to hours, minutes, and seconds:
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            # Get the spinner character:
            spinner_char = next(self.spinner)
            # Format the time string:
            time_str = f"{str(int(hours)).zfill(2)}:{str(int(minutes)).zfill(2)}:{str(int(seconds)).zfill(2)}"
            # Print the message, spinner, and time:
            print(f"\r{self.message} {colored(spinner_char, 'blue')} {colored(time_str, 'light_cyan')}", end="")
            # Wait for 0.2 seconds:
            time.sleep(0.2)

    # Function to start the timer:
    def __enter__(self):
        # Start the timer:
        self.start = time.time()
        # Start the thread:
        self.thread.start()

    # Function to stop the timer:
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # Set the stop event:
        self._stop_event.set()
        # Join the thread:
        self.thread.join()



# Define the script timer class:
class script_timer:

    """
    This class is used to display the runtime of the script at the end.
    
    Attributes:
    ----------
    start_time : float
        The time at which the script started.
    
    Methods:
    -------
    display_runtime()
        Displays the runtime of the script.
    """

    # Define the constructor:
    def __init__(self):
        # Get the start time:
        self.start_time = time.time()
        # Register the display_runtime() method to be called at the end of the script:
        atexit.register(self.display_runtime)

    # Define the display_runtime() method:
    def display_runtime(self):
        # Get the runtime:
        runtime = time.time() - self.start_time
        # Convert the runtime to hours, minutes, and seconds:
        hours, remainder = divmod(runtime, 3600)
        minutes, seconds = divmod(remainder, 60)
        # Format the time string:
        time_str = f"{str(int(hours)).zfill(2)}:{str(int(minutes)).zfill(2)}:{str(int(seconds)).zfill(2)}"
        # Print the runtime:
        print(colored(f"\nTOTAL RUNTIME ▶   {time_str}", 'cyan', attrs=['bold']))
        print('==========================================================================================')