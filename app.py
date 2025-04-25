from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
initialIdTask = 1

@app.route('/tasks', methods=['POST'])
def createTask():
    global initialIdTask

    body = request.get_json()
    newTask = Task(id=initialIdTask, title=body.get("title"), description=body.get("description"))
    initialIdTask += 1
    tasks.append(newTask)
    return jsonify({
        "task" : newTask.to_dict(),
        "message" : "Nova tarefa criada com sucesso."
        }), 201

@app.route('/tasks', methods=['GET'])
def getTasks():
    tasksList = [task.to_dict() for task in tasks]

    return jsonify({
        "tasks" : tasksList,
        "totalTasks" : len(tasksList)
    })

@app.route('/tasks/<int:id>', methods=['GET'])
def getTaskById(id):
    for task in tasks:
        if task.id == id:
            return jsonify(task.to_dict())
    
    return jsonify({ "message" : "Nenhuma task foi encontrada." }), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def updateTaskById(id):
    updatedTask = None

    for task in tasks:
        if task.id == id:
            updatedTask = task

    if updatedTask == None:
        return jsonify({ "message" : "Nenhuma task foi encontrada." }), 404
    
    body = request.get_json()

    updatedTask.title = body.get("title")
    updatedTask.description = body.get("description")
    updatedTask.isCompleted = body.get("isCompleted")

    return jsonify({ "message" : "Task atualizada com sucesso." })

@app.route('/tasks/<int:id>', methods=["DELETE"])
def deleteTaskById(id):
    deletedTask = None

    for task in tasks:
        if task.id == id:
            deletedTask = task

    if not deletedTask:
        return jsonify({ "message" : "Task não encontrada." }), 404
    
    tasks.remove(deletedTask)

    return jsonify({ "message" : "Task removida com sucesso." })


if __name__ == "__main__":
    app.run(debug=True)