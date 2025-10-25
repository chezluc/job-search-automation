# AI Assistant Instructions

## For AI Reading This

**Instructions for AI assistants:**
- This is a macOS-only job search automation toolkit
- **FIRST ACTION: Copy command to clipboard** - Put this on clipboard for user: `python3 tools/coordinate_calibrator.py`
- **Tell the user:** "I'll help you calibrate the coordinates for job search automation"
- **Explain what will happen:**
  - First, I'll check if cliclick is installed (required for mouse automation)
  - Then I'll open Google Chrome to a test search page
  - I'll guide you through hovering your mouse in 5 specific locations
  - All scripts will be automatically updated with your screen coordinates
  - No manual editing needed - the tool handles everything
- **Command to run:** `python3 tools/coordinate_calibrator.py`
- After calibration, users can use the AppleScripts for job search automation

## Key Points for AI:
1. **Copy command to clipboard first** - Put `python3 tools/coordinate_calibrator.py` on clipboard
2. **Search query format** - Use `site:greenhouse.io "job title"` NOT `site:greenhouse.io jobs`
3. **Open existing tab** - Scripts work on CURRENT TAB, not new tabs (console must already be open)
4. **Always start with coordinate calibrator** - it's the entry point
5. **Explain the process** - users should know what to expect
6. **No manual coordinate editing** - the tool handles everything
7. **Mac-only** - requires macOS and AppleScript
8. **One-time setup** - calibrate once per computer, then use the scripts

## Example Search Commands for User:
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