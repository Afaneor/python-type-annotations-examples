# Python Type Annotations & mypy Examples

## 📚 О репозитории

Этот репозиторий содержит примеры использования аннотаций типов в Python и инструмента статического анализа mypy. Примеры структурированы по темам и соответствуют материалу из видео о типизации в Python.

## 🧭 Содержание

- **a/typed_vs_untyped.py** - Сравнение кода с типами и без типов
- **b/simple_types.py** - Базовые типы и их использование
- **c/new_types.py** - Продвинутые типы (TypedDict, Protocol, NewType, Literal)
- **d/callable.py** - Типизация функций и интерфейсов (Callable, Awaitable)
- **e/classes.py** - Типизация классов и атрибутов (ClassVar)
- **f/generic.py** - Дженерики с новым синтаксисом Python 3.12+
- **g/decorator.py** - Типизация декораторов с использованием ParamSpec
- **h/overload.py** - Перегрузка функций (@overload)
- **mypy_example.py** - Простой пример для демонстрации mypy
- **monkeytype_example.py**, **main.py** - Пример для демонстрации MonkeyType

## ⚙️ Требования

- Python 3.12+ (для новых возможностей типизации)
- mypy 1.8.0+ (для проверки типов)
- MonkeyType (опционально, для демонстрации автоматического добавления типов)

## 🔧 Установка

1. Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/python-typing-examples.git
cd python-typing-examples
```

2. Установить зависимости:
```bash
pip install mypy monkeytype
```

## 🚀 Использование

### Проверка типов с mypy

Вы можете проверить типы в примерах с помощью mypy:

```bash
# Проверка одного файла
mypy mypy_example.py

# Проверка директории
mypy a/

# Проверка всего проекта
mypy .
```

Попробуйте запустить mypy на файле с ошибкой типа:
```bash
mypy mypy_example.py
```

Вы должны увидеть ошибку:
```
mypy_example.py:5: error: Argument 1 to "greet" has incompatible type "int"; expected "str"
```

### Использование MonkeyType

MonkeyType позволяет автоматически добавлять аннотации типов на основе реального использования:

```bash
# Запуск приложения и сбор данных о типах
monkeytype run main.py

# Применение собранных типов
monkeytype apply monkeytype_example.greet
```

### Конфигурация mypy

Для проекта можно настроить mypy с помощью файла `pyproject.toml`:

```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = false
disallow_incomplete_defs = false

[[tool.mypy.overrides]]
module = "tests.*"
ignore_missing_imports = true
```

## 📐 Структура примеров

### Сравнение типизированного и нетипизированного кода (a/typed_vs_untyped.py)

Демонстрирует, как добавление типов делает код более понятным и позволяет находить ошибки на этапе проверки.

### Базовые типы (b/simple_types.py)

Показывает использование основных типов в Python:
- Простые типы: `str`, `int`, `float`, `bool`
- Коллекции: `list`, `dict`, `tuple`
- Optional и Union типы
- Типизация функций

### Продвинутые типы (c/new_types.py)

Демонстрирует более сложные типовые конструкции:
- `Literal` для ограничения возможных значений
- `TypedDict` для словарей с определенной структурой
- `Protocol` для структурной типизации
- `NewType` для создания новых семантических типов

### Типизация функций (d/callable.py)

Примеры использования `Callable` и `Awaitable` для типизации функций и корутин.

### Типизация классов (e/classes.py)

Демонстрация различных способов типизации атрибутов класса.

### Дженерики (f/generic.py)

Примеры использования дженериков (Generic Types) с новым синтаксисом Python 3.12+.

### Типизация декораторов (g/decorator.py)

Показывает, как правильно типизировать декораторы с сохранением типов аргументов и возвращаемого значения.

### Перегрузка функций (h/overload.py)

Демонстрирует использование `@overload` для указания различных сигнатур функции в зависимости от типов аргументов.

## 📚 Дополнительные ресурсы

- [Документация по типизации в Python](https://docs.python.org/3/library/typing.html)
- [Документация mypy](https://mypy.readthedocs.io/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [PEP 585 - Type Hinting Generics In Standard Collections](https://www.python.org/dev/peps/pep-0585/)
- [PEP 604 - Allow writing union types as X | Y](https://www.python.org/dev/peps/pep-0604/)
- [PEP 695 - Type Parameter Syntax](https://peps.python.org/pep-0695/)

## 📝 Лицензия

MIT

## 🔗 Полезные ссылки

- [Мой Telegram-канал](https://t.me/pavlin_share)
- [Boosty с дополнительными материалами](https://boosty.to/nikolay-pavlin)
- [YouTube-канал с обучающими видео](https://www.youtube.com/channel/UC2da0IeXHw5kTu-Q_qDFMeQ)
- [FastAPI шаблон с типизацией](https://t.me/pavlin_share/179)
