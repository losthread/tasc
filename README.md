# tasc

A minimal task management CLI script in Python.

## Installation

```bash
git clone https://github.com/your-username/tasc.git
cd tasc
python3 -m venv venv
source venv/bin/activate
```

## Usage

```bash
# Add a task
python app.py add "Learn FastAPI"

# List tasks
python app.py list
python app.py list done
python app.py list in-progress

# Update task
python app.py update 1 "Master FastAPI"

# Mark status
python app.py mark-in-progress 1
python app.py mark-done 1

# Delete task
python app.py delete 1

# Help
python app.py h
```

## Storage

Tasks are saved in `tasks.json` (auto-created).

## Project

Based on [roadmap.sh Task Tracker](https://roadmap.sh/projects/task-tracker)