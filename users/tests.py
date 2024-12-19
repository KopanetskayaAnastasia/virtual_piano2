import time
from .models import Students
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Teachers, Instruments


# class StudentsModelTest(TestCase):
#
#     def setUp(self):
#         # Создание тестового пользователя и инструмента для использования в записях
#         self.user = User.objects.create(username='testuser', password='testpassword')
#         self.instrument = Instruments.objects.create(name='Гитара')  # Предположим, у вас есть модель Instruments
#
#     def test_create_multiple_students(self):
#         start_time = time.time()  # Запоминаем время начала теста
#
#         # Внесение 1000 записей в базу данных
#         for i in range(1000):
#             Students.objects.create(
#                 name=f'Студент {i+1}',
#                 email=f'student{i+1}@example.com',
#                 grade_of_school=i+1,  # Пример: используем i+1 как год обучения
#                 user=self.user,
#                 instrument=self.instrument,
#                 created_at=timezone.now(),
#             )
#
#         # Проверка, что 10 записей действительно были добавлены
#         students_count = Students.objects.count()
#         self.assertEqual(students_count, 1000)
#
#         # Дополнительные проверки: можно проверить, что записи имеют ожидаемые значения
#         for i in range(1000):
#             student = Students.objects.get(name=f'Студент {i+1}')
#             self.assertEqual(student.email, f'student{i+1}@example.com')
#             self.assertEqual(student.grade_of_school, i+1)
#             self.assertEqual(student.user, self.user)
#             self.assertEqual(student.instrument, self.instrument)
#
#         end_time = time.time()  # Запоминаем время окончания теста
#         execution_time = end_time - start_time  # Вычисляем время выполнения теста
#         print(f"Время выполнения теста: {execution_time:.4f} секунд")


class TeachersModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестового пользователя
        UserModel = get_user_model()
        cls.user = UserModel.objects.create_user(username='testuser', password='testpass')

        # Создаем тестовый инструмент
        cls.instrument = Instruments.objects.create(name='Пиано')

        # Создаем тестового учителя
        cls.teacher = Teachers.objects.create(
            name='Иванов И.И.',
            user=cls.user,
            email='ivanov@example.com',
            instrument=cls.instrument
        )

    def test_teacher_creation(self):
        """Проверяем, что учитель создается правильно."""
        self.assertEqual(self.teacher.name, 'Иванов И.И.')
        self.assertEqual(self.teacher.user.username, 'testuser')
        self.assertEqual(self.teacher.email, 'ivanov@example.com')
        self.assertEqual(self.teacher.instrument.name, 'Пиано')
        self.assertIsNotNone(self.teacher.created_at)  # Проверяем, что created_at не None
        self.assertIsNotNone(self.teacher.updated)      # Проверяем, что updated не None

    def test_str_method(self):
        """Проверяем, что метод __str__ работает правильно."""
        self.assertEqual(str(self.teacher), 'Иванов И.И.')

    def test_get_absolute_url(self):
        """Проверяем работу метода get_absolute_url."""
        self.assertEqual(self.teacher.get_absolute_url(), f'/users/{self.teacher.id}')
