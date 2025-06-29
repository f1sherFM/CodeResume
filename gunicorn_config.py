bind = "0.0.0.0:5001"  # Используем переменную окружения
workers = 2
timeout = 30

# Упрощенная конфигурация логгера
accesslog = "-"  # Логи доступа в stdout
errorlog = "-"   # Логи ошибок в stdout
loglevel = "info"  # Уровень логирования