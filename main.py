from flask import Flask, jsonify
import docker

app = Flask(__name__)

@app.route('/api/getcontainers', methods=['GET'])
def get_tasks():
    client = docker.from_env()
    containers = client.containers.list()

    containerIds = " ".join(container.id for container in containers)

    return jsonify({'containers': containerIds})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
    # app.run(debug=True)