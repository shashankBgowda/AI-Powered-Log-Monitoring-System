# AI-Powered-Log-Monitoring-System
📌 Project Overview
This project builds an AI-powered DevOps log analysis system. Phase 1 focuses on collecting raw log data from multiple DevOps sources, transforming it into structured format using an ETL pipeline, and preparing it as JSON output ready for AI/ML model consumption in Phase 2.
---------------------------------------------------------PHASE-1-----------------------------------------------------------------
🗂️ Project Structure
Devops+AI_Project/
│
├── Raw_data_logs/                  # Raw input log files
│   ├── Application_logs
│   ├── Backend_logs
│   ├── Database_logs
│   ├── Docker_logs
│   ├── Kubernetes_logs
│   ├── Linux_system_logs
│   └── Monitoring_logs
│
├── ETL/                            # ETL pipeline scripts
│   ├── ingest.py                   # Step 1 - Read raw log files
│   ├── transform.py                # Step 2 - Parse & structure logs
│   ├── load.py                     # Step 3 - Save as JSON
│   └── pipeline.py                 # Main entry point
│
├── Output/                         # Processed JSON output files
│   ├── Application_logs.json
│   ├── Backend_logs.json
│   ├── Database_logs.json
│   ├── Docker_logs.json
│   ├── Kubernetes_logs.json
│   ├── Linux_system_logs.json
│   └── Monitoring_logs.json
│
└── README.md

⚙️ ETL Pipeline — How It Works
Raw_data_logs/          →       ETL Pipeline        →       Output/
(7 raw log files)               (Python scripts)            (7 JSON files)

  Application_logs  ──┐
  Backend_logs      ──┤    ingest.py            Application_logs.json
  Database_logs     ──┤    transform.py   ──►   Docker_logs.json
  Docker_logs       ──┼    load.py              Backend_logs.json
  Kubernetes_logs   ──┤    pipeline.py          ...and more
  Linux_system_logs ──┤
  Monitoring_logs   ──┘

📦 Output Format
Each log file is saved as a structured JSON array. Example:
json[
    {
        "timestamp": "2024-01-15 10:23:45",
        "level": "ERROR",
        "message": "Connection timeout on port 8080"
    },
    {
        "timestamp": "2024-01-15 10:24:01",
        "level": "INFO",
        "message": "Retrying connection..."
    }
]

🛠️ Prerequisites

Python 3.9+
No external libraries required — uses only Python standard library (os, re, json)


▶️ How to Run
1. Clone the repository:
bashgit clone https://github.com/yourusername/Devops+AI_Project.git
cd Devops+AI_Project
2. Navigate to the ETL folder:
bashcd ETL
3. Run the pipeline:
bashpython pipeline.py
4. Check the output:
Output/
├── Application_logs.json
├── Backend_logs.json
├── Database_logs.json
├── Docker_logs.json
├── Kubernetes_logs.json
├── Linux_system_logs.json
└── Monitoring_logs.json

✅ Terminal Output
==================================================
   DevOps+AI Log Pipeline Starting...
==================================================

[STEP 1] Ingesting logs...
  [Ingesting] Application_logs
  [Ingesting] Backend_logs
  [Ingesting] Database_logs
  [Ingesting] Docker_logs
  [Ingesting] Kubernetes_logs
  [Ingesting] Linux_system_logs
  [Ingesting] Monitoring_logs

[STEP 2 & 3] Transforming and Saving...
  [Saved] ..\Output\Application_logs.json
  [Saved] ..\Output\Backend_logs.json
  ...
==================================================
  Pipeline Completed!
  Files processed : 7
  Total log lines : 500+
==================================================
---------------------------------------------------------PHASE-2-----------------------------------------------------------------

What This Phase Does
Converts log messages into vector embeddings
Stores embeddings along with logs
Enables semantic search (finding similar logs based on meaning)
🧠 Key Concept
Embeddings: Numerical representation of text
Similar logs → similar vectors → better search & analysis
🧱 Project Structure
vector_db/
  ├── embed.py
  ├── store.py
  ├── query.py
  └── main.py
🔄 Data Flow
processed_logs.json → embeddings → stored data → similarity search
▶️ How to Run
cd vector_db
python main.py
📤 Output
Generates embeddings for each log
Returns most similar logs for a given query

Example:

Query: "database error"

Result:
- "Connection timeout in DB"
- "Query execution failed"
🚀 Why This Matters

This phase enables:

Intelligent log search
Faster debugging
Foundation for anomaly detection (next phase)


