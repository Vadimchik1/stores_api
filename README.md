# stores_api
Rest api для магазинов, товаров и их категорий.

Задание:
создать модели для Магазина, категорий товаров и товара создать между ними нужные связи.
Создать endpoint который на get запрос выдает все товары из категории магазина. 
Например 'http://localhost:8000/12/categories/2' где 12 это айди магазина, 2 это айди категории 12го магазина.
Ответ должен выглядеть так [{'id':1, name: 'qwe'}, {'id':2, name: 'qwe'}].
Post запрос должен создать новый товар в категории принимает от клиента json [{name:'qwe'}, {'name':'ewr'}]. Из json array создаются новые товары. 
Также создать
Endpoint по примеру 'http://localhost:8000/{id shop}/categories/{id category}/{id goods}'  http://localhost:8000/12/categories/2/1.
На Get запрос отдается единственный товар с айди который указан в url. Put запрос должен изменять название товара.
Принимается json {'name': 'ewq'}. Изменения объекта доожно производиться с помощью метода update сериалайзера. 
Все задание должно быть выполнено с помощью django и django rest_framework.

Для запуска:
 1. Клонировать проект git clone https://github.com/Vadimchik1/stores_api.git
 2. Применить миграции python manage.py migrate
 3. Запустить python manage.py runserver
 
 По адресу http://127.0.0.1:8000/swagger/ Будет доступна swagger документация к api 
 
 Также для удобства были разработаны: CRUD api для моделей Store и ProductCategory.
 Чтобы они отобразились в swagger документации нужно в файле api/urls.py откомментировать пути.
