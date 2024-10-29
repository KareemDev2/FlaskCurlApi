from flask import Blueprint, jsonify, request
from ..models.task import Task
from datetime import datetime,timezone


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

@tasks_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Recherche la tâche par ID
    task = next((task for task in tasks if task.id == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found!"}), 404
    
    return jsonify(task.to_dict()), 200


@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    print("Données reçues :", data)  # Log pour vérifier le contenu

    # Recherche la tâche par ID
    task = next((task for task in tasks if task.id == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found!"}), 404

    # Vérifie si le corps de la requête contient une nouvelle tâche
    if not data or 'task' not in data: 
        return jsonify({"error": "Task is required in request body!"}), 400

    # Met à jour la tâche
    task.task = data['task']
    task.updated_at = datetime.now(timezone.utc)  # Met à jour la date de modification en UTC

    return jsonify(task.to_dict()), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks  # vérifie la liste des tâches

    # Recherche la tâche par ID
    task = next((task for task in tasks if task.id == task_id), None)
    
    if task is None:
        return jsonify({"error": "Task not found!"}), 404

    # Supprime la tâche
    tasks = [t for t in tasks if t.id != task_id]
    
    return jsonify({"message": "Task deleted successfully!"}), 200


