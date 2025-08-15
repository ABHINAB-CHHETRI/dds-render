# Drone Dispatch System (DDS) — Render Ready (No Mapbox)

Minimal deployable demo:
- Dashboard (active deliveries)
- Create Delivery (payload, priority, click canvas for drop-off)
- Live Tracking (Canvas animation, ETA)
- Internal model (no external maps)

## Deploy with Render Blueprint
1) Push to GitHub.
2) In Render: New → Blueprint → select this repo.
3) Render reads `render.yaml` and creates:
   - dds-backend (Python/Flask)
   - dds-frontend (Static Site)
4) After backend is live, copy its URL and edit `frontend/config.js`:
```js
window.BACKEND_URL = "https://YOUR-BACKEND.onrender.com";
```
Commit to GitHub; Render auto-deploys frontend.

## Local Dev
```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py  # http://localhost:5000

# Frontend
# Open frontend/index.html in a browser
# Edit frontend/config.js to http://localhost:5000
```

## API
- GET /deliveries
- GET /deliveries/<id>
- POST /create_delivery
  body: {"payload":"Blood","priority":"High","dropoff":[70,80]}

Canvas coordinates are 0..100. Start is [10,10].
