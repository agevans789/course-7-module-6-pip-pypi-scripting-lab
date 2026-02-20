from datetime import datetime
import os

# Ensure this is defined so the script can find it if run directly
log_data = ["User logged in", "User updated profile", "Report exported"]

def generate_log(data):
    # STEP 1: Validate input (MUST raise ValueError for the test)
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")

    # STEP 2: Generate filename
    date_str = datetime.now().strftime("%Y%m%d")
    filename = f"log_{date_str}.txt"

    # STEP 3: Write entries
    try:
        with open(filename, "w") as file:
            for entry in data:
                file.write(f"{entry}\n")
        
        # STEP 4: Return the filename so the test knows what to look for!
        print(f"Log has been generated and saved as {filename}")
        return filename

    except Exception as e:
        print(f"An error occurred: {e}")
        raise # Re-raise so the test runner knows the process failed
if __name__ == "__main__":
    generate_log(log_data)
