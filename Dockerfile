FROM python:3.11-slim AS builder
WORKDIR /build
COPY auditor_completo.py .
RUN pip install --no-cache-dir --upgrade pip 2>/dev/null || true

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /build/auditor_completo.py .
CMD ["python3", "auditor_completo.py", "."]
