# 📊 Benchmark Report - Automated Log File Analysis

This is an English translation of the great French-language repository [here](https://github.com/DCx14/sysbench-graph-report) by [@DCx14](https://github.com/DCx14/).


This project offers a Python script that automatically analyzes log files from benchmarks, extracts essential metrics, and generates an interactive HTML report with graphs.

## 🚀 Features

- **Data Extraction:**
  - Scans all `.log` files in a given directory.
  - Automatically identifies the load type (OLTP Read Only, OLTP Write Only, etc.).
  - Extracts key metrics: total number of queries, transactions, latencies (min, avg, max), events per second, etc.

- **Graph Generation:**
  - Creates interactive graphs for each load type.
  - Compares the different metrics extracted for each log file.

- **HTML Report:**
  - Compiles all graphs into an HTML report ready to be viewed in a browser.

## 🛠️ Prerequisites

Before running the script, make sure you have installed:

- **Python 3.x**
- **Python Libraries:**
  - `pandas` for data manipulation.
  - `plotly` for generating interactive graphs.

```bash
pip3 install pandas plotly
```

## 📂 Directory Structure

- `your_script.py`: The main script for extraction and analysis.
- `data_extracted.csv`: Generated CSV file containing the extracted data.
- `report.html`: Interactive HTML report with graphs for each load type.

## 📝 Usage Instructions

1. **Preparation:**
   - Place your `.log` files in the same directory as the script or modify the `LOG_DIR` variable to specify another directory.

2. **Running the Script:**

   - Place your sysbench log files in this format:
  
     ```bash
      oltp_update_non_index  ## make sure to change to the tested oltp
      SQL statistics:
          queries performed:
              read:                            0
              write:                           68
              other:                           865
              total:                           933
          transactions:                        933    (15.55 per sec.)
          queries:                             933    (15.55 per sec.)
          ignored errors:                      0      (0.00 per sec.)
          reconnects:                          0      (0.00 per sec.)
      
      Throughput:
          events/s (eps):                      15.5477
          time elapsed:                        60.0088s
          total number of events:              933
      
      Latency (ms):
               min:                                   58.99
               avg:                                   64.31
               max:                                  223.48
               95th percentile:                       78.60
               sum:                                60000.52
      
      Threads fairness:
          events (avg/stddev):           933.0000/0.00
          execution time (avg/stddev):   60.0005/0.00
     ```

   - Run the script using the following command:
     ```bash
     ./your_script.py
     ```
   - A `data_extracted.csv` file will be generated with the extracted data.
  
4. **Generating the Report:**
   - The script also produces a `report.html` file containing an interactive report with graphs. You can open it directly in your preferred browser.

![](https://i.imgur.com/T2ts60J.png)

## ⚙️ Customization

- **Log Directory:**
  - Modify the `LOG_DIR` variable in the script to change the directory containing the log files.

- **Load Types:**
  - The script detects several load types (OLTP Read Only, OLTP Write Only, etc.). If your logs contain different load types, adjust the conditions in the corresponding section of the script.

## 🤝 Contributions

Contributions are welcome! If you have improvement ideas, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it as you see fit.

---

*Thank you for using this tool for your benchmark analyses!* 🎉
