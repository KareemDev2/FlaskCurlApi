from flask import Blueprint, jsonify, request
from ..models.task import Task

tasks_bp = Blueprint('tasks', __name__)

# Stocke la donnée en mémoire (TEMPORAIRE!)
tasks = []
task_id_ctr = 1

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks])

@tasks_bp.route('/tasks', methods=['POST'])
def create_tasks():
    global task_id_ctr
    data = request.get_json()

    if not data or 'task' not in data: 
        return jsonify({"error": "task is required is request body!"}), 400

    task = Task(task=data['task'])
    task.id = task_id_ctr
    task_id_ctr += 1

    tasks.append(task)
    return jsonify(task.to_dict()), 201