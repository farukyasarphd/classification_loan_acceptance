# API Overview  

## Start the Server
```bash
poetry run uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Access Swagger UI
http://localhost:8000/docs

## Supported Features
- Prediction for multiple customers at once
- Probability outputs for predictions


## Example

**Input:** 
```json
{
  "features": [
    [45, 100000, 5, 1, 1, 1, 0, 0, 1, 1, 0],
    [50, 120000, 3, 0, 2, 0, 1, 1, 0, 0, 0],
    [35, 90000, 3, 1, 0, 2, 0, 1, 1, 1, 0]
  ]
}
```

**Output:**
```json
{
  "predictions": [
    1,
    1,
    1
  ],
  "probabilities": [
    0.9999530273938793,
    0.9999899265919541,
    0.9994081409953709
  ]
}
```

