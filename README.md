# Consistent Hashing Load Balancer

Simple Flask-based load balancer using Consistent Hashing.

---

# Setup

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

Server will start at:

```txt
http://127.0.0.1:5000
```

---

# Verify Application

## 1. Check Server Status

Open:

```txt
http://127.0.0.1:5000/
```

Expected Output:

```json
{
    "message": "Consistent Hashing Load Balancer Running"
}
```

---

## 2. Route an IP

Open:

```txt
http://127.0.0.1:5000/route?ip=192.168.1.1
```

Expected Output:

```json
{
    "ip": "192.168.1.1",
    "node": "Node-B"
}
```

Refresh the same URL multiple times.

Observation:

```txt
Same IP -> Same Node
```

---

## 3. View Current Nodes

Open:

```txt
http://127.0.0.1:5000/nodes
```

---

## 4. Add a Node

Endpoint:

```txt
POST http://127.0.0.1:5000/add-node
```

Request Body:

```json
{
    "node": "Node-D"
}
```

---

## 5. Remove a Node

Endpoint:

```txt
POST http://127.0.0.1:5000/remove-node
```

Request Body:

```json
{
    "node": "Node-B"
}
```

---

# Logging

Terminal logs each request.

Example:

```txt
Incoming IP: 192.168.1.1 -> Routed to: Node-B
```

---

# Tech Stack

* Python
* Flask
* Consistent Hashing
