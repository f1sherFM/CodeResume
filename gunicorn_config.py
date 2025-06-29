bind = "0.0.0.0:$PORT"  # Используем переменную окружения
workers = 2
timeout = 120

# Упрощенная конфигурация логгера
logconfig = None  # Отключаем стандартную конфигурацию
accesslog = "-"  # Логи доступа в stdout
errorlog = "-"   # Логи ошибок в stdout
loglevel = "info"  # Уровень логирования