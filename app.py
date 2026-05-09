from flask import Flask, request, jsonify
from load_balancer import ConsistentHashLoadBalancer
from logger import log_request

app = Flask(__name__)

# Initial Nodes
nodes = ["Node-A", "Node-B", "Node-C"]

# Create Load Balancer
lb = ConsistentHashLoadBalancer(nodes)


@app.route("/")
def home():
    return jsonify({
        "message": "Consistent Hashing Load Balancer Running"
    })


@app.route("/route")
def route_ip():

    ip = request.args.get("ip")

    if not ip:
        return jsonify({
            "error": "IP address required"
        }), 400

    node = lb.get_node(ip)

    log_request(ip, node)

    return jsonify({
        "ip": ip,
        "node": node
    })


@app.route("/add-node", methods=["POST"])
def add_node():

    data = request.get_json()

    node = data.get("node")

    if not node:
        return jsonify({
            "error": "Node name required"
        }), 400

    lb.add_node(node)

    return jsonify({
        "message": f"{node} added successfully",
        "nodes": lb.nodes
    })


@app.route("/remove-node", methods=["POST"])
def remove_node():

    data = request.get_json()

    node = data.get("node")

    if not node:
        return jsonify({
            "error": "Node name required"
        }), 400

    lb.remove_node(node)

    return jsonify({
        "message": f"{node} removed successfully",
        "nodes": lb.nodes
    })


@app.route("/nodes")
def get_nodes():

    return jsonify({
        "nodes": lb.nodes
    })


if __name__ == "__main__":
    app.run(debug=True)