from flask import Flask, jsonify
import os
import redis

def create_app():
    app = Flask(__name__)
    
    # Configure Redis connection
    redis_host = os.environ.get("REDIS_HOST")
    redis_port = int(os.environ.get("REDIS_PORT"))
    redis_db = int(os.environ.get("REDIS_DB"))

    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db, decode_responses=True)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({
            "status": "success",
            "message": "Nebula Notes: Flask + Redis via Docker Compose",
            "description": "A small demo showing a Flask service talking to Redis."
        })

    @app.route("/hits", methods=["GET"])
    def hits():
        # Use Redis INCR to increment a counter atomically
        try:
            hits = r.incr("nebula:hits")  # increments and returns new value
        except Exception as e:
            return jsonify({"status": "error", "message": "Cannot connect to Redis", "error": str(e)}), 500

        return jsonify({"status": "success", "message": "Nebula Notes counter", "hits": int(hits)})

    @app.route("/health", methods=["GET"])
    def health():
        # Basic health: check redis ping too (optional)
        try:
            ok = r.ping()
            redis_status = "reachable" if ok else "unreachable"
        except Exception:
            redis_status = "unreachable"

        return jsonify({
            "status": "healthy" if redis_status == "reachable" else "degraded",
            "redis": redis_status
        })

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)