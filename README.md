<h1 align="center">API Chain store</h1>

---

<h3 align="center">API интерфейс сервиса по продажи электроники</h3>
<p>В проекте реализована регистрация/авторизация,
эндпоинты доступны только аутентифицированным сотрудникам.
Ниже есть подробная таблица с эндпоинтами и их описанием.

---
<h3 align="center">Стек</h3>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10-yellow?&logo=appveyor" alt="">
<img src="https://img.shields.io/badge/PostgreSQL-15.1-orange?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Django-4.2.2-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/DRF-3.14.0-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Docker-blue?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Docker-compose-blue?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Gunicorn-20.1.0-green?logo=appveyor" alt="">
<img src="https://img.shields.io/badge/Pytest django-4.5.2-green?logo=appveyor" alt="">
</p>

---

<h3 align="center">Все доступные эндоинты можно посмотреть на странице swagger.</h3>

    example.com/api/docs/

---

<h3 align="center">Доступные эндпоинты</h3>
<table>
  <thead>
    <tr>
      <th>Сущность</th>
      <th>Действие</th>
      <th>Метод запроса</th>
      <th>Эндпоинт</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Поставщик</td>
      <td>Создать нового поставщика</td>
      <td>POST</td>
      <td>/api/providers/</td>
    </tr>
    <tr>
      <td>Поставщик</td>
      <td>Получить всех поставщиков</td>
      <td>GET</td>
      <td>/api/providers/</td>
    </tr>
    <tr>
      <td>Поставщик</td>
      <td>Получить конкретного поставщика</td>
      <td>GET</td>
      <td>/api/providers/{id}</td>
    </tr>
    <tr>
      <td>Поставщик</td>
      <td>Обновить данные поставщика</td>
      <td>PUT</td>
      <td>/api/providers/{id}</td>
    </tr>
    <tr>
      <td>Поставщик</td>
      <td>Частично обновить данные поставщика</td>
      <td>PATCH</td>
      <td>/api/providers/{id}</td>
    </tr>
    <tr>
      <td>Поставщик</td>
      <td>Удалить поставщика</td>
      <td>DELETE</td>
      <td>/api/providers/{id}</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Создать новый контакт</td>
      <td>POST</td>
      <td>/api/contacts/</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Получить все контакты</td>
      <td>GET</td>
      <td>/api/contacts/</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Получить конкретный контакт</td>
      <td>GET</td>
      <td>/api/contacts/{id}</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Обновить данные контакта</td>
      <td>PUT</td>
      <td>/api/contacts/{id}</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Частично обновить данные контакта</td>
      <td>PATCH</td>
      <td>/api/contacts/{id}</td>
    </tr>
    <tr>
      <td>Контакты</td>
      <td>Удалить контакт</td>
      <td>DELETE</td>
      <td>/api/contacts/{id}</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Создать новый продукт</td>
      <td>POST</td>
      <td>/api/products/</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Получить все продукты</td>
      <td>GET</td>
      <td>/api/products/</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Получить конкретный продукт</td>
      <td>GET</td>
      <td>/api/products/{id}</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Обновить данные продукта</td>
      <td>PUT</td>
      <td>/api/products/{id}</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Частично обновить данные продукта</td>
      <td>PATCH</td>
      <td>/api/products/{id}</td>
    </tr>
    <tr>
      <td>Продукты</td>
      <td>Удалить продукт</td>
      <td>DELETE</td>
      <td>/api/products/{id}</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Создать нового сотрудника</td>
      <td>POST</td>
      <td>/api/employees/signup/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Войти в профиль</td>
      <td>POST</td>
      <td>/api/employees/login/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Выйти из профиля</td>
      <td>DELETE</td>
      <td>/api/employees/logout/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Получить свой профиль</td>
      <td>GET</td>
      <td>/api/employees/profile/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Обновить данные своего профиля</td>
      <td>PUT</td>
      <td>/api/employees/profile/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Частично обновить данные своего профиля</td>
      <td>PATCH</td>
      <td>/api/employees/profile/</td>
    </tr>
    <tr>
      <td>Сотрудники</td>
      <td>Удалить свой профиль</td>
      <td>DELETE</td>
      <td>/api/employees/profile/</td>
    </tr>
  </tbody>
</table>

---

<h3 align="center">Установка проекта</h3>

### 1. Склонируйте репозиторий
    git clone https://github.com/jjEnokenti/chain_store.git

### 2. Настройте окружение
#### 1. создайте файл .env по примеру .env.example

### 3. Можете запускать приложение
    make up
### 4. Для остановки контейнеров
    make down

---
<h3 align="center">Тесты</h3>

### 1. Для старта тестов
    make run tests

### 2. Для просмотра результата тестов
    make show results

### 3. Для удаления контейнеров с тестами
    make down tests
