#!/usr/bin/env python3
"""
Job Search Automation - Coordinate Calibrator
Automatically calibrates all coordinates for job search automation scripts.
"""

import os
import re
import subprocess
import sys

# Coordinate descriptions for each script
COORDINATE_DESCRIPTIONS = {
    "focus_and_execute_console.applescript": [
        ("Console input field", "🔹 OPEN DEV TOOLS (Shift+Cmd+C) then hover at bottom of console where you type commands")
    ],
    "copy_console_results.applescript": [
        ("Console output area", "🔹 Hover in the LEFT COLUMN to the left of console text (where line numbers appear)")
    ],
    "navigate_google_search.applescript": [
        ("Page focus", "🔹 LOAD A GOOGLE SEARCH then hover at the TOP or where there ISN'T text to focus the page"),
        ("Next page", "🔹 SCROLL DOWN TO BOTTOM and hover over the 'Next' button")
    ]
}

def check_cliclick_installed():
    """Check if cliclick is installed and provide installation instructions"""
    try:
        result = subprocess.run(['which', 'cliclick'], capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            print("⚠️  cliclick is not installed!")
            print("\nTo install cliclick:")
            print("  brew install cliclick")
            print("\nOr download from: https://www.bluem.net/en/mac/cliclick/")
            print("\nWithout cliclick, coordinate calibration will not work.")
            return False
    except Exception as e:
        print(f"Error checking for cliclick: {e}")
        return False

def get_mouse_position():
    """Get current mouse position using cliclick"""
    try:
        result = subprocess.run(['cliclick', 'p:.'], capture_output=True, text=True)
        if result.returncode == 0:
            # Extract coordinates from output like "Current mouse position: 123,456"
            output = result.stdout.strip()
            coords = re.search(r'(\d+),(\d+)', output)
            if coords:
                return int(coords.group(1)), int(coords.group(2))
    except Exception as e:
        print(f"Error getting mouse position: {e}")
    return None

def find_coordinates_in_script(script_path):
    """Extract all coordinates from an AppleScript file"""
    with open(script_path, 'r') as f:
        content = f.read()

    # Find coordinates in format c:X,Y
    direct_coordinates = re.findall(r'c:(\d+),(\d+)', content)

    # Find variable-based coordinates
    variable_coordinates = []
    # Look for patterns like: set clicknextX to 568 and set clicknextY to 572
    x_matches = re.findall(r'set\s+(\w+X)\s+to\s+(\d+)', content)
    y_matches = re.findall(r'set\s+(\w+Y)\s+to\s+(\d+)', content)

    # Match X and Y variables that have the same prefix
    for x_var, x_val in x_matches:
        prefix = x_var[:-1]  # Remove 'X' from variable name
        for y_var, y_val in y_matches:
            if y_var == prefix + 'Y':
                variable_coordinates.append((x_val, y_val))
                break

    # Combine both types of coordinates
    coordinates = direct_coordinates + variable_coordinates
    return coordinates

def update_coordinates(script_path, old_coords, new_coords):
    """Update coordinates in AppleScript file"""
    with open(script_path, 'r') as f:
        content = f.read()

    # First update direct coordinates
    for old, new in zip(old_coords, new_coords):
        old_str = f"c:{old[0]},{old[1]}"
        new_str = f"c:{new[0]},{new[1]}"
        content = content.replace(old_str, new_str)

    # Then update variable-based coordinates
    # Find X and Y variables and update them
    x_vars = re.findall(r'set\s+(\w+X)\s+to\s+(\d+)', content)
    y_vars = re.findall(r'set\s+(\w+Y)\s+to\s+(\d+)', content)

    # We'll update the variables based on their order in the file
    # This assumes the variables are in the same order as the coordinates
    for i, (old, new) in enumerate(zip(old_coords, new_coords)):
        if i < len(x_vars):
            x_var, old_x = x_vars[i]
            content = re.sub(fr'set\s+{x_var}\s+to\s+{old_x}', f'set {x_var} to {new[0]}', content)
        if i < len(y_vars):
            y_var, old_y = y_vars[i]
            content = re.sub(fr'set\s+{y_var}\s+to\s+{old_y}', f'set {y_var} to {new[1]}', content)

    with open(script_path, 'w') as f:
        f.write(content)

def interactive_calibration_for_script(script_name, current_coords):
    """Interactive coordinate calibration for a specific script"""
    print(f"\n=== Calibrating {script_name} ===")

    descriptions = COORDINATE_DESCRIPTIONS.get(script_name, [])
    new_coords = []

    for i, coord in enumerate(current_coords):
        if i < len(descriptions):
            title, desc = descriptions[i]
            print(f"\n{i+1}. {title}")
            print(f"   Purpose: {desc}")
            print(f"   Current coordinates: ({coord[0]}, {coord[1]})")
        else:
            print(f"\n{i+1}. Unknown coordinate")
            print(f"   Current coordinates: ({coord[0]}, {coord[1]})")

        input("\n   Position the mouse at the new location and press ENTER...")

        pos = get_mouse_position()
        if pos:
            print(f"   New coordinates: ({pos[0]}, {pos[1]})")
            new_coords.append(pos)
        else:
            print("   Could not capture coordinates. Keeping original.")
            new_coords.append((coord[0], coord[1]))

    return new_coords

def open_google_chrome_test():
    """Open Google Chrome to a test search page"""
    print("\n🔧 Opening Google Chrome to test search...")
    try:
        subprocess.run(['open', '-a', 'Google Chrome', 'https://www.google.com/search?q=test+search+for+calibration'])
        print("✅ Google Chrome opened to test search page")
        print("\n📝 Instructions:")
        print("1. Make sure Chrome is the active window")
        print("2. For console scripts: Open Dev Tools (Shift+Cmd+C)")
        print("3. Follow the prompts to hover your mouse in each location")
    except Exception as e:
        print(f"❌ Could not open Google Chrome: {e}")

def main():
    """Main function - automatically calibrates all scripts"""
    print("=== Job Search Automation - Coordinate Calibrator ===")
    print("This tool will automatically calibrate all coordinates for your job search automation.")

    # Check if cliclick is installed
    if not check_cliclick_installed():
        print("\n❌ Please install cliclick first and then run this tool again.")
        return

    # Open Google Chrome to test search
    open_google_chrome_test()

    # Find all AppleScript files
    script_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_dir = os.path.join(script_dir, "../scripts")
    applescript_files = [f for f in os.listdir(scripts_dir) if f.endswith('.applescript') and f in COORDINATE_DESCRIPTIONS]

    if not applescript_files:
        print("\n❌ No AppleScript files found in scripts directory.")
        return

    print(f"\n📁 Found {len(applescript_files)} AppleScript files to calibrate:")
    for script in applescript_files:
        print(f"  - {script}")

    # Extract coordinates from each file
    all_coordinates = {}
    for script in applescript_files:
        script_path = os.path.join(scripts_dir, script)
        coords = find_coordinates_in_script(script_path)
        if coords:
            all_coordinates[script] = coords

    print("\n🚀 Starting calibration process...")
    input("Press ENTER when you're ready to begin calibration...")

    # Calibrate all scripts
    for script in applescript_files:
        if script in all_coordinates:
            new_coords = interactive_calibration_for_script(script, all_coordinates[script])

            # Update the script
            script_path = os.path.join(scripts_dir, script)
            update_coordinates(script_path, all_coordinates[script], new_coords)
            all_coordinates[script] = new_coords
            print(f"✅ {script} updated!")

    print("\n🎉 All scripts have been calibrated!")
    print("\n📋 Next steps:")
    print("1. Test the scripts by running them")
    print("2. If any coordinates need adjustment, run this tool again")
    print("3. Happy job searching! 🚀")

if __name__ == "__main__":
    main()