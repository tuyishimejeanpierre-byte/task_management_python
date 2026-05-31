from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

tasks = []

add_task(
    tasks,
    "Finish Assignment",
    "Complete Python project",
    "2026-06-10"
)

view_pending_tasks(tasks)

mark_task_as_complete(tasks, 1)

print("Progress:", calculate_progress(tasks), "%")