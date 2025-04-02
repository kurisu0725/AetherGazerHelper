import os
from pathlib import Path

def get_project_root():
    return Path(__file__).parent.parent

def sync_dirs_from_tasks_to_assets():
    project_root = get_project_root()
    tasks_dir = project_root / "tasks"
    assets_dir = project_root / "assets"

    tasks_dir.mkdir(exist_ok=True)
    assets_dir.mkdir(exist_ok=True)

    task_subdirs = [d for d in tasks_dir.iterdir() if d.is_dir()]

    created_count = 0
    for task_subdir in task_subdirs:
        target_dir = assets_dir / task_subdir.name
        if not target_dir.exists():
            target_dir.mkdir()
            print(f"Created directory: {target_dir}")
            created_count += 1
        else:
            print(f"Directory alread exists : {target_dir}")
    print(f"\nOpraetion complete. Created {created_count} new directories.")

if __name__ == "__main__":
    sync_dirs_from_tasks_to_assets()