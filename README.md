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

# Deployment Link

```txt
https://infollion-asg.onrender.com/
```

---

# Verification Steps

## 1. Check Server Status

Open:

```txt
https://infollion-asg.onrender.com/
```

Expected Response:

```json
{
    "message": "Consistent Hashing Load Balancer Running"
}
```

---

## 2. Verify Consistent Routing

Open:

```txt
https://infollion-asg.onrender.com/route?ip=192.168.1.1
```

Refresh multiple times.

Observation:

```txt
Same IP -> Same Node
```

---

## 3. Verify Different IP Routing

Try:

```txt
https://infollion-asg.onrender.com/route?ip=8.8.8.8
```

and

```txt
https://infollion-asg.onrender.com/route?ip=1.1.1.1
```

Different IPs may map to different nodes.

---

## 4. Verify Current Nodes

Open:

```txt
https://infollion-asg.onrender.com/nodes
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


# High Level overview
<img width="1578" height="974" alt="image" src="https://github.com/user-attachments/assets/be543065-3eff-4771-9e6a-f962ebda7f1e" />

