import pytest
from HW_task_manager.app.task_manager import TaskManager
import allure


@pytest.fixture
def task_manager():
    """
    Создаем экземпляр класса
    """
    return TaskManager()


@allure.feature('TaskManager')
@allure.story('Добавить задачу')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_task(task_manager):
    """
    Тест функции на добавление задачи в TaskManager с приоритетом
    """
    # task_manager.add_task('Task 10', 'high')
    # assert task["name"] == 'Task 10'
    # assert task['priority'] == 'high'
    # assert task['completed'] is False
    # assert len(task_manager.list_tasks()) == 1
    with allure.step('Добавление задачи с верным приоритетом'):
        task = task_manager.add_task('Task 10', 'high')
        assert task["name"] == 'Task 10'
        assert task['priority'] == 'high'
        assert task['completed'] is False
        assert len(task_manager.list_tasks()) == 1


@allure.feature('TaskManager')
@allure.story('Добавить задачу')
@allure.severity(allure.severity_level.NORMAL)
def test_add_task_without_priority(task_manager):
    """
    Тест функции на добавление задачи в TaskManager без указания приоритета
    """
    # task = task_manager.add_task('Task 20')
    # assert task['name'] == 'Task 20'
    # assert task['priority'] == 'normal'
    # assert task['completed'] is False
    # assert len(task_manager.list_tasks()) == 1
    with allure.step("Добавление задачи без приоритета"):
        task = task_manager.add_task('Task 20')
        assert task['name'] == 'Task 20'
        assert task['priority'] == 'normal'
        assert task['completed'] is False
        assert len(task_manager.list_tasks()) == 1


@allure.feature('TaskManager')
@allure.story('Добавить задачу')
@allure.severity(allure.severity_level.NORMAL)
def test_add_task_priority(task_manager):
    """
    Тест функции на добавление задачи в TaskManager с приоритетом не из списка
    """
    # with pytest.raises(ValueError, match="Приоритет должен быть 'low', 'normal' или 'high'"):
    #     task_manager.add_task("Task 10", "invalid")
    with allure.step('Добавление задачи с приоритетом не из списка'):
        with pytest.raises(ValueError, match="Приоритет должен быть 'low', 'normal' или 'high'"):
            task_manager.add_task("Task 10", "invalid")


@allure.feature('TaskManager')
@allure.story('Возвращение списка задач')
@allure.severity(allure.severity_level.NORMAL)
def test_list_tasks(task_manager):
    """
    Тест возвращения списка всех задач
    """
    # task_manager.add_task("Task 10", "high")
    # task_manager.add_task("Task 20", "low")
    # tasks = task_manager.list_tasks()
    # assert len(tasks) == 2
    # assert tasks[0]["name"] == "Task 10"
    # assert tasks[1]["name"] == "Task 20"
    with allure.step('Возвращение списка задач'):
        task_manager.add_task("Task 10", "high")
        task_manager.add_task("Task 20", "low")
        tasks = task_manager.list_tasks()
        assert len(tasks) == 2
        assert tasks[0]["name"] == "Task 10"
        assert tasks[1]["name"] == "Task 20"


@allure.feature('TaskManager')
@allure.story('Выполненная задача')
@allure.severity(allure.severity_level.NORMAL)
def test_mark_task_completed(task_manager):
    """
    Тест функции изменение статуса на выполненную
    """
    # task_manager.add_task('Task 10')
    # task = task_manager.mark_task_completed("Task 10")
    # assert task['completed'] is True
    # assert task['name'] == 'Task 10'
    with allure.step('Отмечаем задачу как выполненную'):
        task_manager.add_task('Task 10')
        task = task_manager.mark_task_completed("Task 10")
        assert task['completed'] is True
        assert task['name'] == 'Task 10'


@allure.feature('TaskManager')
@allure.story('Удалить задачу')
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_task(task_manager):
    """
    Тест функции на удаление задач из списка
    """
    # task_manager.add_task("Task 10")
    # removed = task_manager.remove_task("Task 10")
    # assert removed["name"] == "Task 10", "Название удалённой задачи некорректно"
    # assert removed not in task_manager.list_tasks(), "Задача не была удалена из списка"
    with allure.step('Удаляем задачу из списка'):
        task_manager.add_task("Task 10")
        removed = task_manager.remove_task("Task 10")
        assert removed["name"] == "Task 10", "Название удалённой задачи некорректно"
        assert removed not in task_manager.list_tasks(), "Задача не была удалена из списка"
