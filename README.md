# GeeksforGeeks Leaderboard Scraper

## Overview
This Python script allows you to fetch and search leaderboard data from GeeksforGeeks contests using cookies. It parses the contest link, extracts the necessary slug, and retrieves leaderboard information across multiple pages.

## Prerequisites
- Python 3.x installed on your system
- Necessary Python libraries (`requests`, `json`, `re`) installed. You can install them using pip:

  ```bash
  pip install requests
  ```

## Getting Your Cookies

### Step-by-Step Guide to Obtain Cookies
1. **Open GeeksforGeeks Leaderboard API URL:**

   - Navigate to the leaderboard API URL for your contest. For example:
     ```
     https://practiceapi.geeksforgeeks.org/api/latest/contest/gfg-weekly-159-rated-contest/leaderboard/?page=1
     ```

2. **Open Developer Tools (F12 or Ctrl+Shift+I):**
   - Open your browser's developer tools by pressing F12 or Ctrl+Shift+I.

3. **Navigate to the Network Tab:**
   - Click on the "Network" tab in the developer tools.

4. **Reload the Page:**
   - Reload the leaderboard API URL page to capture network requests.

5. **Find the API Request:**
   - Look for the request corresponding to `leaderboard/?page=1` in the network list. It should be listed under "Name" or "Path" columns.

6. **View Request Headers:**
   - Click on the API request to open its details.
   - Go to the "Headers" tab.
   - Scroll down to find the "Cookie" section.

7. **Copy Your Cookies:**
   - Copy the entire `Cookie` value. It should look something like:
     ```
     gfg_id5_identity=your_identity_value; csrftoken=your_csrf_token_value; gfg_nluid=your_nluid_value; ...
     ```

8. **Paste Your Cookies in the Script:**
   - Open the `leaderboard_scraper.py` file.
   - Replace the placeholder `cookies` variable with your copied cookies (e.g., `gfg_id5_identity`, `csrftoken`, etc.).

## Usage

### Running the Script
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/like-rounak/gfg-leaderboad-rank-searcher.git
   cd gfg-leaderboad-rank-searcher
   ```

2. Run the script from the terminal:
   ```bash
   python leaderboard_scraper.py
   ```

3. Write the `leaderboard_scraper.py` file:
   - Write up the variables `contest_link`, `handle_name`, and `total_pages` according to your requirements in terminal when prompted.

4. Follow the prompts in the terminal:
   - Enter the contest link when prompted.
   - Enter the handle name of the participant whose data you want to fetch.
   - Enter the total number of pages in the leaderboard.

5. The script will fetch and display leaderboard data for the specified contest and handle name.

### Example
Here's an example of how to set up and run the script:

```bash
# Clone the repository
git clone https://github.com/like-rounak/gfg-leaderboad-rank-searcher.git
cd gfg-leaderboad-rank-searcher

# Run the script
python leaderboard_scraper.py
```

