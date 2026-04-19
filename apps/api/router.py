from providers import providers

def route_request(payload):
    best = None
    best_score = -999

    for p in providers:
        score = (p["quality"] * 0.6) - (p["cost"] * 0.3) - (p["latency"] * 0.1)

        if score > best_score:
            best_score = score
            best = p

    return {
        "provider": best["name"],
        "cost_saved": best["savings"]
    }