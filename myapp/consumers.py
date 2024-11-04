import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Подключаемся к группе для уведомлений
        await self.channel_layer.group_add("notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Отключаемся от группы
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        # Отправляем сообщение клиенту
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))