# tasc
A minimal task management CLI tool written in Python.

## Features
- Add tasks
- Update tasks
- Delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status

## Requirements
- Python 

## Installation

Clone the repository:
git clone https://github.com/your-username/tasc.git
cd tasc

(Optional but recommended) Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Usage

Run the CLI using:
python app.py <command>

## Commands

### Add a task
python app.py add "Task name"

### Update a task
python app.py update <id> "New task name"

### Delete a task
python app.py delete <id>

### Mark task as in-progress
python app.py mark-in-progress <id>

### Mark task as done
python app.py mark-done <id>

### List tasks
python app.py list

### List by status
python app.py list todo  
python app.py list in-progress  
python app.py list done  

### Help
python app.py h

## Data Storage

- Tasks are stored in a local file: `tasks.json`
- Automatically created when you add your first task

## Example

python app.py add "Learn Python"
python app.py list
python app.py mark-done 1

## Notes

- IDs are auto-incremented
- Dates are stored in ISO format
- No external dependencies required

## Project reference url
https://roadmap.sh/projects/task-tracker