# Job Search Automation Toolkit

> **⚠️ Mac Only** - This toolkit requires macOS and uses AppleScript for automation

This toolkit helps automate job searching across multiple job boards using AppleScript automation.

## Project Structure

```
job_search_automation/
├── README.md                    # This documentation
├── scripts/                     # AppleScript automation files
│   ├── focus_and_execute_console.applescript
│   ├── navigate_google_search.applescript
│   └── copy_console_results.applescript
├── tools/                       # Python utilities
│   ├── coordinate_calibrator.py
│   └── requirements.txt
└── data/                       # Data files
    └── job_boards_complete_list.txt
```

## Files Included

### AppleScripts (`scripts/`)
- **`focus_and_execute_console.applescript`** - Pastes and executes JavaScript from clipboard in Chrome console
- **`navigate_google_search.applescript`** - Navigates through Google search results (scrolling + next page)
- **`copy_console_results.applescript`** - Copies console output to clipboard

### Data Files (`data/`)
- **`job_boards_complete_list.txt`** - Comprehensive list of job boards by region and search method

### Tools (`tools/`)
- **`coordinate_calibrator.py`** - Interactive tool to find and update XY coordinates for different computers

## Setup Instructions

### 1. Install Dependencies
```bash
# Install cliclick for mouse automation
brew install cliclick

# Install Python dependencies (if needed)
pip3 install -r requirements.txt
```

### 2. Calibrate Coordinates
Run the coordinate calibrator - it will automatically:
1. Check if cliclick is installed
2. Open Google Chrome to a test search page
3. Guide you through calibrating all coordinates

```bash
cd job-search-automation
python3 tools/coordinate_calibrator.py
```

**What will happen:**
- The tool will check for required dependencies
- Google Chrome will open to a test search page
- You'll be guided to hover your mouse in 5 locations:
  - Console input field (for JavaScript execution)
  - Console output area (for copying results)
  - Google search page focus area
  - Google search "Next" button
- All scripts will be automatically updated with new coordinates

### 3. Update Scripts
After calibration, update the coordinates in the AppleScript files:
- `paste_execute_console.applescript` - Console click coordinates
- `google_search_navigation.applescript` - Search result click coordinates

## Usage Workflow

### Basic Job Search
1. **Navigate to Google search** for job boards using `site:` operator
2. **Run navigation script** to browse through results
3. **Extract job links** using console automation
4. **Copy results** to clipboard for processing

### Example Search Commands
```javascript
// Extract greenhouse.io job links
const jobLinks = Array.from(document.querySelectorAll("a[href*=\"greenhouse.io\"]"))
  .filter(link => link.href.includes("/jobs/") && !link.href.includes("google.com"))
  .map(link => ({
    title: link.textContent.trim(),
    url: link.href,
    company: link.href.split("/")[3]
  }));

console.log("Found", jobLinks.length, "job links:");
jobLinks.forEach(link => console.log(link.company, "-", link.title, "-", link.url));
```

## Supported Job Boards

### Sites that work with `site:` operator:
- greenhouse.io
- myworkdayjobs.com
- workable.com
- smartrecruiters.com
- indeed.com
- linkedin.com
- glassdoor.com

### Sites that need manual search:
- lever.co
- bamboohr.com
- oracle.com/taleo
- sap.com/successfactors

## Tips

- Use Google search filters like `tbs=qdr:w` (last week) or `num=50` (more results)
- Test coordinates on each new computer using the calibrator
- Combine multiple job board searches for comprehensive results
- Use clipboard as temporary storage between scripts

## Troubleshooting

- **Coordinates don't work**: Run the coordinate calibrator on the new computer
- **Scripts fail**: Check that Chrome is the active application
- **No results**: Verify the search query and that you're on the correct page
- **cliclick not found**: Install via `brew install cliclick`