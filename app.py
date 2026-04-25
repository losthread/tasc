import sys
import os
import json
from datetime import datetime

def loadTasks():
  if not os.path.exists('tasks.json'):
    return []
  with open('tasks.json', 'r') as file:
    try:
      return json.load(file)
    except:
      return []

def saveTasks(tasks):
  with open('tasks.json', 'w') as file:
    json.dump(tasks, file, indent=2)

# list tasks
def listTasks(status = None):
  if not os.path.exists('tasks.json'):
    print("The data file does not exist! Please create it...\n")
    return

  tasks = loadTasks()

  for task in tasks:
    # apply filter only if provided
    if status is not None and task['status'] != status:
      continue

    print("ID:", task['id'])
    print("Task Name:", task['description'])
    print("Status:", task['status'])
    print("Created At:", task['createdAt'])
    print("Updated At:", task['updatedAt'])
    print("------")

# add task
def addTask(description):
  tasks = loadTasks()

  # find id of new task
  if not tasks:
    id = 1 
  else: 
    id = max(task['id'] for task in tasks) + 1

  # create task
  t = {
    'id': id,
    'description': description,
    'status': 'todo',
    'createdAt': datetime.now().isoformat(),
    'updatedAt': datetime.now().isoformat()
  }
  
  # append to list
  tasks.append(t)

  # save to file
  saveTasks(tasks)

  print("Task Added Successfully\n")

# mark in progress
def markInProgress(id):
    if not os.path.exists('tasks.json'):
      print("The data file does not exist! Please create it...\n")
      return

    tasks = loadTasks()

    found = False

    for task in tasks:
      if task['id'] == int(id):
        task['status'] = 'in-progress'
        task['updatedAt'] = datetime.now().isoformat()
        found = True
        break

    if not found:
      print("Task not found! Please enter a valid task ID\n")
      return

    saveTasks(tasks)

    print("Task updated successfully")

# mark as done
def markAsDone(id):
  if not os.path.exists('tasks.json'):
    print("The data file does not exist! Please create it...\n")
    return
  
  tasks = loadTasks()

  found = False

  for task in tasks:
    if task['id'] == int(id):
      task['status'] = 'done'
      task['updatedAt'] = datetime.now().isoformat()
      found = True
      break

  if not found:
    print("Task not found! Please enter a valid task ID\n")
    return
    
  saveTasks(tasks)

  print("Task updated successfully")

# update task
def updateTask(id, description):
  if not os.path.exists('tasks.json'):
    print("The data file does not exist! Please create it...")
    return
  
  tasks = loadTasks()
  
  found = False

  for task in tasks:
    if task['id'] == int(id):
      task['description'] = description
      task['updatedAt'] = datetime.now().isoformat()
      found = True
      break

  if not found:
    print("Task not found! Please enter valid task ID\n")
    return

  saveTasks(tasks)

  print("Task updated successfully!\n")

# delete tasks
def deleteTask(id):
  if not os.path.exists('tasks.json'):
    print("The data file does not exist! Please create one...\n")
    return
  
  tasks = loadTasks()

  found = False

  for i, task in enumerate(tasks):
    if task['id'] == int(id):
      tasks.pop(i)
      found = True
      break

  if not found:
    print("Task not found! Please enter valid task ID\n")
    return
  
  saveTasks(tasks)

  print("Task deleted successfully\n")

if len(sys.argv) == 1:
  print("Invalid command! run app.py h for help")
  sys.exit()

# help
if sys.argv[1] == 'h':
  print("------ List of commands ------")
  print("add <taskname>")
  print("update <id> <taskname>")
  print("delete <id>")
  print("mark-in-progress <id>")
  print("mark-done <id>")
  print("list")
  print("list done")
  print("list todo")
  print("list in-progress\n")
  sys.exit()

# adding tasks
if sys.argv[1] == 'add':
  if len(sys.argv) < 3:
    print("Usage: add <taskname>")
    sys.exit()
  description = sys.argv[2]
  addTask(description)

# updating tasks
elif sys.argv[1] == 'update':
  if len(sys.argv) < 4:
    print("Usage: update <id> <taskname>")
    sys.exit()
  id = sys.argv[2]
  description = sys.argv[3]
  updateTask(id, description)

# deleting tasks
elif sys.argv[1] == 'delete':
  if len(sys.argv) < 3:
    print("Usage: delete <id>")
    sys.exit()
  id = sys.argv[2]
  deleteTask(id)

# mark in progress
elif sys.argv[1] == 'mark-in-progress':
  if len(sys.argv) < 3:
    print("Usage: mark-in-progress <id>")
    sys.exit()
  id = sys.argv[2]
  markInProgress(id)

# mark done
elif sys.argv[1] == 'mark-done':
  if len(sys.argv) < 3:
    print("Usage: mark-done <id>")
    sys.exit()
  id = sys.argv[2]
  markAsDone(id)

# listing all tasks
elif sys.argv[1] == 'list':
  if len(sys.argv) > 2:
    listTasks(sys.argv[2])
  else:
    listTasks()

else:
  print("Invalid command! Please enter valid arguments\n")