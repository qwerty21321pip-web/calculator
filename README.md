# Калькулятор на Python

Учебный проект по практической части лекции 1 о GitHub.
Поддерживает сложение, вычитание, умножение, деление и возведение в степень.
При делении на ноль вызывает `ValueError`.

## Установка

Требуется Python 3.9 или новее. В папке проекта выполните:

```bash
python -m pip install -e ".[test]"
```

## Пример

```python
from calculator.core import add, subtract, multiply, divide

print(add(2, 3))       # 5
print(subtract(2, 3))  # -1
print(multiply(2, 3))  # 6
print(divide(7, 2))    # 3.5

from calculator.core import power
print(power(2, 3))     # 8
```

## Запуск тестов

```bash
python -m pytest
```

## Структура

- `src/calculator/core.py` — арифметические функции.
- `src/calculator/__init__.py` — Python-пакет.
- `tests/test_core.py` — тесты.
- `pyproject.toml` — установка пакета и настройка тестов.
- `.gitignore` — исключения для Git.

## Работа с Git

Каждый этап оформлен отдельным осмысленным коммитом.
Функция возведения в степень разрабатывается в ветке `feature/power`
и переносится в `main` через Pull Request по заданию из лекции.

```bash
git log --oneline --all --graph
```
