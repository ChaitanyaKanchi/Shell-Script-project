# System Health Monitoring with Streamlit and Shell Commands

This is a **Streamlit** application designed to monitor system health metrics such as CPU info, memory usage, disk usage, network activity, and more. It uses shell commands to fetch system information and displays them in an optimized manner with asynchronous execution.

## Features

- **CPU Info**: Fetch detailed CPU information using the `lscpu` command.
- **Memory Info**: Display memory usage using the `free` command.
- **Node Health Monitoring**:
  - CPU Load
  - Memory Usage
  - Disk Usage
  - Network Activity
  - Top 5 CPU-consuming processes


## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/ChaitanyaKanchi/Shell-Script-project
   cd system-health-monitoring
2. Setup Environment
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Run the Code
   ```
   streamlit run app.py
