from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .utils import get_ai_suggestions

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.doc_id = self.scope['url_route']['kwargs']['doc_id']
        self.group_name = f'document_{self.doc_id}'

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data.get('content', '')

        # Broadcast to group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'document_update',
                'content': content,
            }
        )

    async def document_update(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'content': event['content'],
        }))


async def receive(self, text_data):
    data = json.loads(text_data)
    content = data.get('content', '')

    suggestions = get_ai_suggestions(content)

    await self.channel_layer.group_send(
        self.group_name,
        {
            'type': 'document_update',
            'content': content,
            'suggestions': suggestions,
        }
    )
