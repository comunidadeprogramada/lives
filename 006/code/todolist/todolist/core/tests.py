from django.test import TestCase


class TestViewIndex(TestCase):
    def test_simple_request(self):
        self.assertEqual(200, self.client.get('/').status_code)


class TestModelTodoItems(TestCase):
    def test_element_creation(self):
        TodoItems.objects.create(text='item de teste', done=False)
        self.assertTrue(TodoItems.objects.exists())


from .models import TodoItems


class TestViewApiInsert(TestCase):
    def test_database_insertion(self):
        self.assertEqual(200, self.client.post('/api/insert/',
                                               data={'text': 'item de teste'}).status_code)
        self.assertEqual(1, TodoItems.objects.count())
        self.assertEqual('item de teste', TodoItems.objects.first().text)


class TestViewApiRemove(TestCase):
    def test_database_remove(self):
        item = TodoItems.objects.create(text='teste', done=False)
        self.assertEqual(200, self.client.post('/api/remove/',
                                               data={'id': item.id}).status_code)
        self.assertEqual(0, TodoItems.objects.count())

    def test_item_not_found(self):
        self.assertEqual(404, self.client.post('/api/remove/',
                                               data={'id': 444}).status_code)


class TestViewApiCheck(TestCase):
    def test_checked_item(self):
        item = TodoItems.objects.create(text='teste', done=False)
        self.assertEqual(200, self.client.post('/api/check/',
                                               data={'id': item.id}).status_code)
        self.assertTrue(TodoItems.objects.filter(id=item.id).first().done)

    def test_unchecked_item(self):
        item = TodoItems.objects.create(text='teste', done=True)
        self.assertEqual(200, self.client.post('/api/check/',
                                               data={'id': item.id}).status_code)
        self.assertFalse(TodoItems.objects.filter(id=item.id).first().done)
