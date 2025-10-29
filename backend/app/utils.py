"""
utils.py — Funciones auxiliares varias.
"""
import datetime

def now_iso():
    return datetime.datetime.utcnow().isoformat() + "Z"
